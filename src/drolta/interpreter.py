"""Drolta Interpreter."""

from __future__ import annotations

import logging
import re
import sqlite3
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Generator, Iterable, Optional, cast

import sqlparse

from drolta.ast import (
    AliasDeclarationNode,
    ANDFilterExprNode,
    ASTNode,
    AtomNode,
    ComparisonFilterExprNode,
    ComparisonOp,
    FilterExprNode,
    GroupByClauseNode,
    LimitClauseNode,
    MembershipFilterExprNode,
    NodeType,
    NOTFilterExprNode,
    NullsSortDirection,
    OrderByClauseNode,
    OrderingTermNode,
    ORFilterExprNode,
    PredicateExprNode,
    PredicateNegationExprNode,
    ProgramNode,
    QueryExprNode,
    RuleDeclarationNode,
    SortDirection,
    VariableNode,
    WhereClauseNode,
    WhereStmtNode,
    generate_ast,
)
from drolta.db import SQLiteDatabase
from drolta.errors import DroltaError

_logger = logging.getLogger(__name__)


def limit_clause_to_str(node: LimitClauseNode) -> str:
    offset_expr = f" OFFSET {node.offset}" if node.offset > 0 else ""
    return f"LIMIT {node.value}{offset_expr}"


def group_by_to_str(node: GroupByClauseNode) -> str:
    term_list_str = ", ".join(term.value for term in node.grouping_terms.items)
    return f"GROUP BY {term_list_str}"


def order_by_to_str(node: OrderByClauseNode) -> str:
    term_list_str = ", ".join(ordering_term_to_str(term) for term in node.terms.items)
    return f"ORDER BY {term_list_str}"


def ordering_term_to_str(node: OrderingTermNode) -> str:
    asc_desc = ""
    if node.sort_dir != SortDirection.NONE:
        asc_desc = " ASC" if node.sort_dir == SortDirection.ASC else " DESC"

    nulls_order = ""
    if node.nulls_sort_dir != NullsSortDirection.NONE:
        nulls_order = (
            " NULLS FIRST"
            if node.nulls_sort_dir == NullsSortDirection.FIRST
            else " NULLS LAST"
        )

    return f"{node.variable.value}{asc_desc}{nulls_order}"


class FilterExprNodeVisitor:
    """Walks an AST subtree starting at a filter expression and returns a string."""

    def visit(self, node: ASTNode) -> str:
        if isinstance(node, ORFilterExprNode):
            return self.visit_or_filter_expr(node)
        elif isinstance(node, ANDFilterExprNode):
            return self.visit_and_filter_expr(node)
        elif isinstance(node, NOTFilterExprNode):
            return self.visit_not_filter_expr(node)
        elif isinstance(node, ComparisonFilterExprNode):
            return self.visit_comparison_filter_expr(node)
        elif isinstance(node, MembershipFilterExprNode):
            return self.visit_membership_filter_expr(node)
        elif isinstance(node, AtomNode):
            return str(node)

        raise DroltaError(f'Unsupported node type: {type(node)}')

    def visit_comparison_filter_expr(self, node: ComparisonFilterExprNode) -> str:
        operator_map = {
            ComparisonOp.GT: '>',
            ComparisonOp.LT: '<',
            ComparisonOp.GTE: '>=',
            ComparisonOp.LTE: '<=',
            ComparisonOp.EQ: '=',
            ComparisonOp.NEQ: '!=',
        }

        null_operator_map = {
            ComparisonOp.EQ: 'IS',
            ComparisonOp.NEQ: 'IS NOT',
        }

        if node.right.get_type() == NodeType.NULL_LITERAL:
            op_str = null_operator_map[node.op]
        else:
            op_str = operator_map[node.op]

        left_str = self.visit(node.left)

        right_str = self.visit(node.right)

        return f"({left_str} {op_str} {right_str})"

    def visit_membership_filter_expr(self, node: MembershipFilterExprNode) -> str:
        value_list = ", ".join(str(v) for v in node.values.items)
        expression_op = "NOT IN" if node.is_negated else "IN"
        return f"({node.left.value} {expression_op} ({value_list}))"

    def visit_and_filter_expr(self, node: ANDFilterExprNode) -> str:
        return f"({self.visit(node.left)} AND {self.visit(node.right)})"

    def visit_or_filter_expr(self, node: ORFilterExprNode) -> str:
        return f"({self.visit(node.left)} OR {self.visit(node.right)})"

    def visit_not_filter_expr(self, node: NOTFilterExprNode):
        return f"(NOT {self.visit(node.expr)})"


def is_filter_expression(node: ASTNode) -> bool:
    """Check if the given node is a valid filter expression."""
    return isinstance(node, FilterExprNode)


def get_execution_order(node: ASTNode) -> int:
    """Get the order number of the expression (Lower is higher priority)."""
    expression_type = node.get_type()

    if expression_type == NodeType.PREDICATE_EXPR:
        return 0

    if is_filter_expression(node):
        return 1

    if expression_type == NodeType.PREDICATE_NEGATION_EXPR:
        return 1

    return 2


def cycle_check_dfs(
    aliases: dict[str, str], value: str, visited: set[str], stack: list[str]
) -> tuple[bool, str]:
    """Perform Depth-First Search to check for cycles."""

    if value not in visited:
        visited.add(value)
        stack.append(value)

        if value in aliases:
            target = aliases[value]

            if target not in visited:
                result = cycle_check_dfs(aliases, target, visited, stack)
                if result[0] is True:
                    return result

            if target in stack:
                return True, target

    stack.pop()
    return False, ""


def has_alias_cycle(aliases: dict[str, str]) -> tuple[bool, str]:
    """Check if the alias dictionary has a cycle."""

    stack: list[str] = []
    visited: set[str] = set()

    for alias in aliases.keys():
        if alias not in visited:
            result = cycle_check_dfs(aliases, alias, visited, stack)
            if result[0] is True:
                return result

    return False, ""


def find_connected_components(
    rule: str,
    dependency_dict: dict[str, set[str]],
    disc: dict[str, int],
    low: dict[str, int],
    in_stack: dict[str, bool],
    stack: list[str],
    timer: list[int],
    connected_components: list[set[str]],
) -> None:

    timer[0] += 1
    disc[rule] = low[rule] = timer[0]

    stack.append(rule)
    in_stack[rule] = True

    for other_rule in dependency_dict[rule]:

        if disc[other_rule] == -1:

            find_connected_components(
                other_rule,
                dependency_dict,
                disc,
                low,
                in_stack,
                stack,
                timer,
                connected_components,
            )

            low[rule] = min(low[rule], low[other_rule])

        elif in_stack[other_rule]:
            low[rule] = min(low[rule], disc[other_rule])

    if low[rule] == disc[rule]:

        components: set[str] = set()

        while True:
            rule_name = stack.pop()
            in_stack[rule_name] = False
            components.add(rule_name)

            if rule_name == rule:
                break

        connected_components.append(components)


def get_connected_components(dependency_dict: dict[str, set[str]]) -> list[set[str]]:
    connected_components: list[set[str]] = []

    disc: dict[str, int] = {k: -1 for k in dependency_dict.keys()}
    low: dict[str, int] = {k: -1 for k in dependency_dict.keys()}
    in_stack: dict[str, bool] = {k: False for k in dependency_dict.keys()}

    stack: list[str] = []
    timer: list[int] = [0]

    for rule in dependency_dict.keys():

        if disc[rule] == -1:
            find_connected_components(
                rule,
                dependency_dict,
                disc,
                low,
                in_stack,
                stack,
                timer,
                connected_components,
            )

    return connected_components


def get_referenced_predicates(node: WhereStmtNode) -> list[str]:
    """Get the names of predicates referenced by the given node."""

    if node.get_type() == NodeType.PREDICATE_EXPR:
        return [cast(PredicateExprNode, node).name]
    elif node.get_type() == NodeType.PREDICATE_NEGATION_EXPR:
        return [cast(PredicateNegationExprNode, node).expr.name]
    return []


def build_rule_dependency_graph(rules: dict[str, Rule]) -> dict[str, set[str]]:
    """Create a dependency graph of dependencies between Drolta rules."""

    dependency_graph: dict[str, set[str]] = {name: set() for name in rules}

    for _, rule in rules.items():
        for rule in rule.variants:
            for stmt_node in rule.where_expressions.statements:
                for pred_name in get_referenced_predicates(stmt_node):
                    if pred_name in rules:
                        dependency_graph[rule.name].add(pred_name)

    return dependency_graph


def sqlite_dtype_to_py(d_type: str) -> str:
    """Convert SQLite data type name to python type name."""

    if d_type == "INT":
        return "int"
    elif d_type == "TEXT":
        return "str"
    elif d_type == "REAL":
        return "float"

    return "object"


@dataclass(frozen=True, slots=True)
class TempTable:
    """A temp table containing intermediate results of a query."""

    name: str
    """The name of the temporary table with this result's data"""
    column_names: set[str]
    """The column names of the temp table"""

    @staticmethod
    def get_common_columns(b: TempTable, a: TempTable) -> list[str]:
        """Get common columns between two temp tables."""
        return sorted(a.column_names.intersection(b.column_names))


@dataclass(frozen=True, slots=True)
class ColumnInfo:
    """Information about a column in a table."""

    name: str
    """The name of the column."""
    d_type: str
    """The data type (int | str)."""


class DroltaResult:
    """The result of a Drolta Query.

    This class wraps a sqlite3 Cursor object to ensure that all temporary
    tables are removed at the start of a new query.
    """

    __slots__ = ("_column_info", "_has_read_data", "_cursor", "_db", "_result_table")

    _column_info: list[ColumnInfo]
    _has_read_data: bool
    _result_table: TempTable
    _db: SQLiteDatabase
    _cursor: Optional[sqlite3.Cursor]

    def __init__(
        self,
        columns: list[ColumnInfo],
        db: SQLiteDatabase,
        result_table: TempTable,
        cursor: Optional[sqlite3.Cursor] = None,
    ) -> None:
        self._column_info = [*columns]
        self._has_read_data = False
        self._cursor = cursor
        self._db = db
        self._result_table = result_table

    @property
    def result_table(self) -> TempTable:
        return self._result_table

    @property
    def description(self) -> Iterable[ColumnInfo]:
        """Get information about the columns in the result."""
        return [*self._column_info]

    def fetch_all(self) -> list[Any]:
        """Get all results from the last query."""

        if self._has_read_data:
            raise RuntimeError("Data already fetched from this result.")

        self._has_read_data = True

        if self._cursor is None:
            return []

        result = self._cursor.fetchall()

        self.destroy()

        return result

    def fetch_chunks(self, size: int) -> Generator[list[Any], Any, None]:
        """Fetch the next batch of results."""

        if self._has_read_data:
            raise RuntimeError("Data already fetched from this result.")

        self._has_read_data = True

        if self._cursor is None:
            yield []
            return

        next_batch = self._cursor.fetchmany(size)

        while next_batch:
            yield next_batch
            next_batch = self._cursor.fetchmany(size)

        self.destroy()

    def destroy(self):
        """Destroy this result, freeing resources."""
        if self._cursor:
            self._cursor.close()
            self._db.drop_table(self._result_table.name)
            self._cursor = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):
        self.destroy()


class FormattedSqlString:
    """Represents a SQL string."""

    __slots__ = ("raw_sql",)

    raw_sql: str

    def __init__(self, raw_sql: str) -> None:
        self.raw_sql = raw_sql

    def __str__(self) -> str:
        formatted_str = sqlparse.format(
            self.raw_sql,
            reindent=True,
            reindent_aligned=True,
            keyword_case="upper",
            indent_columns=True,
            indent_after_first=True,
        )
        return f"\n{formatted_str}"


class ASTVisitor(ABC):
    """Abstract base class implemented by visitors that traverse ASTs."""

    def visit_program(self, node: ProgramNode) -> None:
        """Visit Program Node."""
        for child in node.children:
            self.visit(child)

    @abstractmethod
    def visit_declare_alias(self, node: AliasDeclarationNode) -> None:
        """Visit DeclareAliasNode."""
        raise NotImplementedError()

    @abstractmethod
    def visit_declare_rule(self, node: RuleDeclarationNode) -> None:
        """Visit DeclareRuleNode."""
        raise NotImplementedError()

    @abstractmethod
    def visit_query(self, node: QueryExprNode) -> None:
        """Visit QueryExpression."""
        raise NotImplementedError()

    def visit(self, node: ASTNode) -> None:
        """Dynamic dispatch by node type."""
        expression_type = node.get_type()

        if expression_type == NodeType.PROGRAM:
            return self.visit_program(cast(ProgramNode, node))

        if expression_type == NodeType.ALIAS_DECLARATION:
            return self.visit_declare_alias(cast(AliasDeclarationNode, node))

        if expression_type == NodeType.RULE_DECLARATION:
            return self.visit_declare_rule(cast(RuleDeclarationNode, node))

        if expression_type == NodeType.QUERY:
            return self.visit_query(cast(QueryExprNode, node))

        raise TypeError(f"Unsupported node expression type: {expression_type.name}")


# class ASTValidator(ASTVisitor):
#     """Validates that the AST conforms to language rules."""

#     def visit_declare_rule(self, node: RuleDeclarationNode) -> None:
#         if len(node.where_expressions) == 0:
#             raise ProgrammingError(
#                 "WHERE section of rule declaration is missing statements."
#             )

#         if len(node.result_vars) == 0:
#             raise ProgrammingError("Rule declaration is missing result variables.")

#     def visit_query(self, node: QueryExprNode) -> None:
#         if len(node.where_expressions) == 0:
#             raise ProgrammingError("WHERE section of query is missing statements.")

#         if len(node.result_vars) == 0:
#             raise ProgrammingError("Query is missing result variables.")

#     def validate_membership_filter(node: MembershipFilterExprNode) -> None:
#             """Validate this expression's fields."""
#             expression_op = "NOT IN" if self.is_inverted else "IN"

#             if self.expr.get_type() != NodeType.VARIABLE:
#                 raise ProgrammingError(
#                     f"Expected variable for left side of '{expression_op}'"
#                 )

#             for entry in self.values:
#                 expr_type = entry.get_type()
#                 if expr_type == NodeType.VARIABLE:
#                     raise ProgrammingError(
#                         f"Value list in '{expression_op}'-expression cannot contain variables."
#                     )
#                 if expr_type == NodeType.NULL_LITERAL:
#                     raise ProgrammingError(
#                         f"Value list in '{expression_op}'-expression cannot contain NULL."
#                     )


@dataclass(slots=True)
class ResultVariable:
    """A query rule result variable."""

    var_name: str
    aggregate_name: str = ""
    alias: str = ""

    def clone(self) -> ResultVariable:
        return ResultVariable(
            var_name=self.var_name, aggregate_name=self.aggregate_name, alias=self.alias
        )

    def get_final_name(self) -> str:
        if self.alias:
            return self.alias
        return self.var_name

    def __str__(self):
        final_str = self.var_name

        if self.aggregate_name:
            final_str = f"{self.aggregate_name}({final_str})"

        if self.alias:
            final_str = f'{final_str} AS "{self.alias}"'

        return final_str


@dataclass(slots=True)
class RuleVariant:
    """A Drolta query rule."""

    name: str
    result_vars: list[ResultVariable]
    where_expressions: WhereClauseNode
    order_by: Optional[OrderByClauseNode]
    group_by: Optional[GroupByClauseNode]
    limit: Optional[LimitClauseNode]

    def get_arity(self) -> int:
        return len(self.result_vars)


@dataclass(slots=True)
class Rule:

    name: str
    result_vars: list[ResultVariable] = field(default_factory=list[ResultVariable])
    variants: list[RuleVariant] = field(default_factory=list[RuleVariant])

    def get_arity(self) -> int:
        return len(self.result_vars)

    def check_variables_match(self, rule_variant: RuleVariant) -> bool:
        """Check if the variables in the given variant are compatible."""
        for i in range(self.get_arity()):
            if (
                self.result_vars[i].get_final_name()
                != rule_variant.result_vars[i].get_final_name()
            ):
                return False

        return True


@dataclass(slots=True)
class Scope:
    """Information about the current variable scope of the query."""

    scope_id: int
    """The ID of the current scope."""
    output_vars: list[ResultVariable] = field(default_factory=list[ResultVariable])
    """Variables output by this scope."""
    tables: list[TempTable] = field(default_factory=list[TempTable])
    """Temporary result tables."""
    next_table_id: int = 1
    """The ID assigned to the next table in this scope."""


SUPPORTED_AGGREGATES: set[str] = {"COUNT", "MAX", "MIN", "AVG", "SUM"}
"""Aggregate functions supported by Drolta."""


class DroltaInterpreter(ASTVisitor):
    """Interpreter used for queries."""

    TEMP_TABLE_PREFIX = "temp__"
    """Name prefix for all temporary tables created by the query engine."""

    __slots__ = (
        "db",
        "_aliases",
        "_rules",
        "_sccs",
        "_scope_stack",
        "result",
        "bindings",
        "_materialized_this_query",
        "_table_column_name_cache",
        "_alias_resolution_cache",
        "_next_query_id",
        "_filter_expr_visitor",
    )

    db: SQLiteDatabase
    """Database connection."""
    _aliases: dict[str, str]
    """Predicate alias names mapped to their target names."""
    _rules: dict[str, Rule]
    """Registered query rules."""
    _sccs: list[set[str]]
    """Strongly connected components derived from query rule dependencies."""
    _scope_stack: list[Scope]
    """Stack of scopes used during query evaluation."""
    result: Optional[DroltaResult]
    """Cursor with results."""
    bindings: dict[str, Any]
    """Variable bindings supplied by the user."""
    _materialized_this_query: set[str]
    """Names of recursive rules that were resolved during the current query."""
    _table_column_name_cache: dict[str, list[str]]
    """Table names mapped to a list containing its column names."""
    _alias_resolution_cache: dict[str, str]
    """Aliases mapped to their final resolved name."""
    _next_query_id: int
    """Gives each query a unique ID to prevent table name clashes."""
    _filter_expr_visitor: FilterExprNodeVisitor
    """Builds query strings from filter expression nodes."""

    def __init__(self, db: SQLiteDatabase) -> None:
        super().__init__()
        self.db = db
        self._aliases = dict()
        self._rules = dict()
        self._sccs = list()
        self._scope_stack = []
        self.result = None
        self.bindings = {}
        self._materialized_this_query = set()
        self._table_column_name_cache = dict()
        self._alias_resolution_cache = dict()
        self._next_query_id = 0
        self._filter_expr_visitor = FilterExprNodeVisitor()

    def execute_script(self, drolta_script: str) -> None:
        """Load rules and aliases from a Drolta script.

        Parameters
        ----------
        drolta_script : str
            Drolta script text containing rule and alias definitions.
        """

        drolta_ast = generate_ast(drolta_script)
        self.visit(drolta_ast)

    def query(
        self,
        drolta_query: str,
        bindings: Optional[dict[str, Any]] = None,
    ) -> Optional[DroltaResult]:
        """Query the SQLite database and return a cursor to the results.

        Parameters
        ----------
        drolta_query : str
            Text defining a Drolta query.
        bindings: dict[str, Any]
            Bindings of query variables to values.

        Returns
        -------
        DroltaResult
            The result of the query.
        """
        self.bindings = bindings if bindings is not None else {}
        drolta_ast = generate_ast(drolta_query)
        self.visit(drolta_ast)
        return self.result

    def visit_declare_alias(self, node: AliasDeclarationNode):
        new_alias_dict = {**self._aliases, node.alias: node.original_name}

        has_cycle, cycled_alias = has_alias_cycle(new_alias_dict)

        if has_cycle:
            raise DroltaError(f"Circular aliases for: {cycled_alias}.")

        self._aliases[node.alias] = node.original_name

        _logger.debug("Declared alias: %s -> %s", node.alias, node.original_name)

    def visit_declare_rule(self, node: RuleDeclarationNode):
        result_vars: list[ResultVariable] = []
        for entry in node.define_clause.result_vars.items:
            result_vars.append(
                ResultVariable(
                    var_name=entry.variable.value,
                    aggregate_name=entry.aggregate_name,
                    alias=entry.alias,
                )
            )

        rule_variant = RuleVariant(
            name=node.define_clause.name,
            result_vars=result_vars,
            where_expressions=node.where_clause,
            group_by=node.group_by,
            order_by=node.order_by,
            limit=node.limit,
        )

        if rule_variant.name not in self._rules:
            self._rules[rule_variant.name] = Rule(
                name=rule_variant.name,
                result_vars=[v.clone() for v in rule_variant.result_vars],
            )

            _logger.debug("Declared new rule: %s", rule_variant.name)

        rule_entry = self._rules[rule_variant.name]

        if rule_entry.get_arity() != rule_variant.get_arity():
            raise DroltaError(
                f"Expected arity {rule_entry.get_arity()} but was {rule_variant.get_arity()} for rule: "
                + rule_variant.name
            )

        if rule_entry.check_variables_match(rule_variant) is False:
            raise DroltaError("Mismatched rule names for rule: " + rule_variant.name)

        rule_entry.variants.append(rule_variant)

        self._refresh_connected_components()

        _logger.debug("Added rule variant for: %s", rule_variant.name)

    def visit_query(self, node: QueryExprNode):
        self._next_query_id += 1
        self.clear_scope_stack()
        self.clear_query_cache()

        _logger.debug("Starting query evaluation...")

        self._push_scope([
            ResultVariable(
                var_name=v.variable.value,
                aggregate_name=v.aggregate_name,
                alias=v.alias,
            ) for v in node.find_clause.result_vars.items
        ])

        # Sort expressions to push filters and not-predicate expressions
        # to the end of the query.
        where_expressions = sorted(
            node.where_clause.statements, key=get_execution_order
        )

        for expr in where_expressions:
            expression_type = expr.get_type()

            if expression_type == NodeType.PREDICATE_EXPR:
                self.visit_predicate(cast(PredicateExprNode, expr))

            elif is_filter_expression(expr):
                self.visit_filter(cast(FilterExprNode, expr))

            elif expression_type == NodeType.PREDICATE_NEGATION_EXPR:
                self.visit_not_predicate(cast(PredicateNegationExprNode, expr))

            self._join_tables_with_shared_vars()

        result_table = self._cross_join_tables_in_scope(self.get_scope())

        # For the end of the query, we want to select from the result table
        # all the variables in output vars and assign them to any aliases

        output_cols: list[str] = []
        for entry in self.get_scope().output_vars:
            if entry.aggregate_name:
                if entry.aggregate_name not in SUPPORTED_AGGREGATES:
                    raise DroltaError(f"Use of unsupported aggregate: {entry}")

            output_cols.append(str(entry))

        sql_stmt_lines: list[str] = [
            f"SELECT DISTINCT {', '.join(output_cols)}",
            f"FROM {result_table.name}",
        ]

        if self.bindings:
            where_statements: list[str] = []
            for var_name, value in self.bindings.items():
                if value is None:
                    where_statements.append(f"{var_name[1:]} IS NULL")
                elif isinstance(value, str):
                    where_statements.append(f'{var_name[1:]} = "{value}"')
                else:
                    where_statements.append(f"{var_name[1:]} = {value}")

            sql_stmt_lines.append(f"WHERE {' AND '.join(where_statements)}")

        if node.group_by:
            sql_stmt_lines.append(f"{group_by_to_str(node.group_by)}")

        if node.order_by:
            sql_stmt_lines.append(f"{order_by_to_str(node.order_by)}")

        if node.limit:
            sql_stmt_lines.append(f"{limit_clause_to_str(node.limit)}")

        sql_stmt_lines.append(";")

        sql_stmt = "\n".join(sql_stmt_lines)

        _logger.debug("Calculating final query output...")
        _logger.debug(FormattedSqlString(sql_stmt))

        cursor = self.db.conn.cursor()

        try:
            result = cursor.execute(sql_stmt)
        except sqlite3.OperationalError as ex:
            if match := re.match(r"^no such column: ([a-zA-z0-9]+)$", str(ex)):
                raise DroltaError(
                    f"Parameter ?{match.group(1)} does not appear in WHERE section of the query."
                ) from ex
            else:
                raise ex

        column_info_cursor = self.db.conn.cursor()

        raw_column_data: dict[str, str] = {
            k: v
            for k, v in column_info_cursor.execute(
                f"SELECT name, type FROM pragma_table_info('{result_table.name}')"
            ).fetchall()
        }

        column_info: list[ColumnInfo] = []
        for entry in self.get_scope().output_vars:
            if entry.var_name in raw_column_data:
                if entry.alias:
                    column_info.append(
                        ColumnInfo(
                            entry.alias,
                            sqlite_dtype_to_py(raw_column_data[entry.var_name]),
                        )
                    )
                else:
                    column_info.append(
                        ColumnInfo(
                            entry.var_name,
                            sqlite_dtype_to_py(raw_column_data[entry.var_name]),
                        )
                    )

        _logger.debug("Query Evaluation complete...")

        self.result = DroltaResult(
            columns=column_info, db=self.db, result_table=result_table, cursor=result
        )

    def visit_predicate(self, node: PredicateExprNode):
        """Evaluate the given predicate expression."""

        # Resolve the actual predicate name by checking against registered aliases
        resolved_predicate_name = self.resolve_predicate_name(node.name)

        # If the resolved predicate name is not mapped to a rule, then we assume
        # it must be an existing table within SQLite. So, we can run the predicate
        # directly on the table.
        if resolved_predicate_name not in self._rules:
            self.execute_predicate_sql(resolved_predicate_name, node)
            return

        # At this point, we know that the resolved predicate name is mapped to
        # a rule. Therefore, we must determine if the rule is self-recursive or
        # belongs to a recursive connected set of rules (strongly connected component)
        # containing more than one rule.
        scc = self._get_scc_for(resolved_predicate_name)

        # The following exception should never be raised unless the interpreter
        # never recalculated SCCs after defining a new rule variant.
        if scc is None:
            raise DroltaError(
                f"Connected component not found for rule: {resolved_predicate_name}"
            )

        # Check if a rule is indirectly recursive (within an SCC with more than one node)
        # or if the rule is directly self recursive and references itself.
        if len(scc) > 1 or self._check_rule_has_self_loop(resolved_predicate_name):
            if not scc.issubset(self._materialized_this_query):
                self._evaluate_scc(scc)
                self._materialized_this_query.update(scc)

            # At this point the '__full' table for the given rule should have been
            # evaluated and stored as a temporary table that we can directly run
            # SQL against just like a normal predicate.
            self.execute_predicate_sql(f"{resolved_predicate_name}__full", node)

        # At this point, we know that the rule is not recursive in any way. First,
        # we check if the rule has already been expanded previously during this query.
        # If not, we expand the rule to make the '<rule_name>__full' table available
        # in the database.
        else:
            if not resolved_predicate_name in self._materialized_this_query:
                self._expand_non_recursive_rule(resolved_predicate_name)
                self._materialized_this_query.add(resolved_predicate_name)

            # At this point the '__full' table for the given rule should have been
            # evaluated and stored as a temporary table that we can directly run
            # SQL against just like a normal predicate.
            self.execute_predicate_sql(f"{resolved_predicate_name}__full", node)

    def _expand_non_recursive_rule(self, rule_name: str):
            """Evaluate all instances of a rule and produce complete answer sets.

            This method produces `__full` tables for the given rule and all rules
            it depends on. Since the rules are not recursive, they are not expanded
            together as connected components
            """

            rule = self._rules[rule_name]

            # We start by making a new scope to hold the tables produced during
            # this process.
            self._push_scope([v.clone() for v in rule.result_vars])

            # Iterate through all variants of the given rule and generate a `__full` table
            # by taking the union of each of their results.
            for i, rule_variant in enumerate(rule.variants):

                self._push_scope()

                # Sort expressions to push filters and not-predicate expressions
                # to the end of the query.
                where_expressions = sorted(
                    rule_variant.where_expressions.statements, key=get_execution_order
                )

                # Loop through the statements in the where expression, joining
                # together tables with common variables if possible
                for expr in where_expressions:
                    expression_type = expr.get_type()

                    if expression_type == NodeType.PREDICATE_EXPR:
                        self.visit_predicate(cast(PredicateExprNode, expr))

                    elif is_filter_expression(expr):
                        self.visit_filter(cast(FilterExprNode, expr))

                    elif expression_type == NodeType.PREDICATE_NEGATION_EXPR:
                        temp_table = self._cross_join_tables_in_scope(self.get_scope())
                        self.get_scope().tables.append(temp_table)
                        self.visit_not_predicate(cast(PredicateNegationExprNode, expr))

                    self._join_tables_with_shared_vars()

                # Cross join the remaining tables to get one table to perform the SQL
                temp_table = self._cross_join_tables_in_scope(self.get_scope())

                # This should add the table to the top level scope.
                result_table = self._execute_rule_variant_sql(temp_table, rule_variant, i)
                self.pop_scope()
                self.db.drop_table(temp_table.name)
                self.get_scope().tables.append(result_table)

            # Now, union all the tables together to create the fully expanded table.
            # We do not store the table within the scope because we do not want it
            # to be dropped when the scope is dropped.
            self._union_tables_in_scope(self.get_scope(), f"{rule_name}__full")

            # Remember to pop the scope created while expanding this rule.
            self.pop_scope()

    def visit_filter(self, node: FilterExprNode):
        """Evaluate predicate expression."""

        # This function forces all the previous tables to join and performs a filter
        # on them.
        prev_result_table = self._cross_join_tables_in_scope(self.get_scope())

        table_name = self.get_temp_table_name()

        new_result_table = TempTable(table_name, set(prev_result_table.column_names))

        filter_str = self._filter_expr_visitor.visit(node)

        sql_temp_table_statement = (
            f"CREATE TEMPORARY TABLE {table_name} AS "
            f"SELECT * FROM {prev_result_table.name} WHERE {filter_str};"
        )

        _logger.debug("Executing filter...")
        _logger.debug(FormattedSqlString(sql_temp_table_statement))

        self.db.execute(sql_temp_table_statement)

        # delete the old temp_table
        self.db.drop_table(prev_result_table.name)

        self.get_scope().tables.append(new_result_table)

    def visit_not_predicate(self, node: PredicateNegationExprNode):
        """Evaluate predicate expression."""

        self._push_scope()

        expression_type = node.expr.get_type()

        if expression_type == NodeType.PREDICATE_EXPR:
            self.visit_predicate(node.expr)

        else:
            raise DroltaError("Not statement expects a predicate or rule.")

        result_table = self.get_scope().tables.pop()

        self.pop_scope()

        last_table = self.get_scope().tables.pop()

        table_name = self.get_temp_table_name()

        not_join_result = TempTable(
            name=table_name, column_names=set(last_table.column_names)
        )

        shared_vars = TempTable.get_common_columns(last_table, result_table)

        if shared_vars:
            where_filters = " AND ".join(
                f"({result_table.name}.{v} = {last_table.name}.{v})"
                for v in shared_vars
            )

            sql_statement = f"""
                SELECT *
                FROM {last_table.name}
                WHERE
                  NOT EXISTS (
                    SELECT 1
                    FROM {result_table.name}
                    WHERE {where_filters}
                  )
                """

            sql_temp_table_statement = (
                f"CREATE TEMPORARY TABLE {table_name} AS {sql_statement};"
            )

            _logger.debug("Executing negation...")
            _logger.debug(FormattedSqlString(sql_temp_table_statement))

            self.db.execute(sql_temp_table_statement)

            self.db.drop_table(result_table.name)

            self.db.drop_table(last_table.name)

            self.get_scope().tables.append(not_join_result)

    def _cross_join_tables_in_scope(self, scope: Scope) -> TempTable:
        """Cross joins all the tables in the current scope, removing the old tables."""

        result_table_name = self.get_temp_table_name()

        sql_stmt_lines: list[str] = [
            f"CREATE TEMPORARY TABLE {result_table_name} AS",
        ]

        output_columns: set[str] = set()

        last_table = scope.tables[-1]

        sql_stmt_lines.append(f"SELECT * FROM {last_table.name}")

        output_columns.update(last_table.column_names)

        for other_table in scope.tables[:-1]:
            shared_column_names = TempTable.get_common_columns(last_table, other_table)

            output_columns.update(other_table.column_names)

            if shared_column_names:
                join_cols = " AND ".join(
                    f"({other_table.name}.{v} = {last_table.name}.{v})"
                    for v in shared_column_names
                )

                sql_stmt_lines.append(f"JOIN {other_table.name} ON {join_cols}")
            else:
                sql_stmt_lines.append(f"CROSS JOIN {other_table.name}")

        sql_stmt_lines.append(";")

        sql_stmt = "\n".join(sql_stmt_lines)

        _logger.debug("Joining all tables in given scope...")
        _logger.debug(FormattedSqlString(sql_stmt))

        self.db.execute(sql_stmt)

        self._destroy_tables_in_scope(scope)

        return TempTable(result_table_name, output_columns)

    def _join_tables_with_shared_vars(self) -> None:
        """Try to join the latest table with any existing ones."""
        current_scope = self.get_scope()
        if len(current_scope.tables) > 1:
            # Check if the last table has common vars with any
            # of the previous tables
            last_table = current_scope.tables[-1]

            shared_table_indexes: set[int] = set()
            output_vars: set[str] = set(last_table.column_names)
            have_shared: list[tuple[int, list[str]]] = []

            for table_idx, other_table in enumerate(current_scope.tables[:-1]):
                shared_vars = TempTable.get_common_columns(last_table, other_table)
                if shared_vars:
                    have_shared.append((table_idx, shared_vars))
                    shared_table_indexes.add(table_idx)
                    output_vars = output_vars.union(other_table.column_names)

            if have_shared:
                # Create a large join under a new temp_table.

                table_name = self.get_temp_table_name()

                sql_stmt_lines: list[str] = [
                    f"CREATE TEMPORARY TABLE {table_name} AS",
                    f"SELECT * FROM {last_table.name}",
                ]

                for idx, var_names in have_shared:
                    temp_table = current_scope.tables[idx]

                    join_cols = " AND ".join(
                        f"({temp_table.name}.{v} = {last_table.name}.{v})"
                        for v in var_names
                    )

                    sql_stmt_lines.append(
                        f"JOIN {temp_table.name} ON {join_cols}"
                    )

                sql_stmt_lines.append(";")

                sql_stmt = "\n".join(sql_stmt_lines)

                _logger.debug("Joining temp tables...")
                _logger.debug(FormattedSqlString(sql_stmt))

                self.db.execute(sql_stmt)

                # Remove all tables involved with the join
                for idx in range(len(current_scope.tables), -1, -1):
                    if (
                        idx == len(current_scope.tables) - 1
                        or idx in shared_table_indexes
                    ):
                        table = current_scope.tables.pop(idx)

                        self.db.drop_table(table.name)

                current_scope.tables.append(
                    TempTable(name=table_name, column_names=output_vars)
                )

    def _union_tables_in_scope(self, scope: Scope, table_name: str) -> TempTable:
        """Union all the tables in the given scope.

        This method does a SQL Union operation across all the tables in the given
        scope. It then drops all the tables involved and clears their temp table
        entries from the scope.

        Parameters
        ----------
        scope
            The scope to perform the union over.
        table_name
            The name of the table that will hold the union.

        Returns
        -------
        Temporary table data corresponding to the union-ed table in SQLite.

        Notes
        -----
        This method should only be called when attempting to union
        the temp tables containing the variants of the same rule.
        """

        sql_stmt_lines: list[str] = [
            f"CREATE TEMP TABLE {table_name} AS",
        ]

        # Place UNION between blanket SELECT statements over the tables
        # in the scope. The last table should not have a 'UNION' after it.
        num_tables = len(scope.tables)
        for i, table in enumerate(scope.tables):
            sql_stmt_lines.append(f"SELECT * FROM {table.name}")
            if i < num_tables - 1:
                sql_stmt_lines.append("UNION")

        sql_stmt_lines.append(";")

        sql_stmt = "\n".join(sql_stmt_lines)

        self.db.execute(sql_stmt)

        _logger.debug("Performing UNION on all tables in scope...")
        _logger.debug(FormattedSqlString(sql_stmt))

        # Clean up all the tables in this scope.
        self._destroy_tables_in_scope(scope)

        return TempTable(table_name, set(self._get_table_column_names(table_name)))

    def execute_predicate_sql(self, table_name: str, node: PredicateExprNode) -> None:
        """Execute SQL query for a predicate expression."""

        output_vars: set[str] = set()
        column_statements: list[str] = []
        where_statements: list[str] = []

        table_column_names = self._get_table_column_names(table_name)
        valid_column_names = set(table_column_names)
        available_column_names = set(table_column_names)

        if node.positional_params:

            if len(node.positional_params.params) > len(table_column_names):
                raise DroltaError(
                    f"Too many positional parameters provided for rule: {table_name}"
                )

            for i, param_node in enumerate(node.positional_params.params):
                column_name = table_column_names[i]
                available_column_names.remove(column_name)

                if param_node.get_type() == NodeType.VARIABLE:
                    # Variable nodes represent columns that should unify with the current scope.
                    # So, these are treated as the columns within the SQL SELECT statement
                    column_statements.append(
                        f"{column_name} AS [{param_node}]"
                    )
                    output_vars.add(cast(VariableNode, param_node).value)

                elif param_node.get_type() == NodeType.NULL_LITERAL:
                    where_statements.append(
                        f"{column_name} IS {param_node}"
                    )

                else:
                    where_statements.append(
                        f"{column_name} = {param_node}"
                    )

        if node.named_params:

            for param_node in node.named_params.params:
                column_name, expr = param_node.column_name, param_node.value

                if column_name not in valid_column_names:
                    raise DroltaError(f"{column_name} is not a column in {table_name}")

                if column_name not in available_column_names:
                    raise DroltaError(
                        f"Column name has already been assigned to positional param: {column_name}"
                    )

                if expr.get_type() == NodeType.VARIABLE:
                    column_statements.append(f"{column_name} AS [{expr}]")
                    output_vars.add(str(expr))
                else:
                    if expr.get_type() == NodeType.NULL_LITERAL:
                        where_statements.append(
                            f"{column_name} IS {expr}"
                        )
                    else:
                        where_statements.append(f"{column_name} = {expr}")

        if len(column_statements) == 0:
            raise DroltaError(f"Predicate '{node}' expects one output variable.")

        if where_statements:
            select_expr = f"""
                SELECT {', '.join(column_statements)}
                FROM {table_name}
                WHERE {' AND '.join(where_statements)}
                """
        else:
            select_expr = f"SELECT {', '.join(column_statements)} FROM {table_name} "

        temp_table_name = self.get_temp_table_name()

        sql_statement = f"CREATE TEMPORARY TABLE {temp_table_name} AS {select_expr};"

        _logger.debug("Executing SQL query on table...")
        _logger.debug(FormattedSqlString(sql_statement))

        self.db.execute(sql_statement)

        self.get_scope().tables.append(TempTable(temp_table_name, output_vars))

    def _eval_rule_variant(self, rule_name: str, rule_variant: RuleVariant, recursive_ref: str, scc: set[str]) -> None:
        pass

    def _execute_rule_variant_sql(self, table: TempTable, rule_variant: RuleVariant, key: int) -> TempTable:
        """Execute a SQL query against the given table with the given rule."""

        # The variables output by this rules
        output_vars: set[str] = set()
        # Column selection statements
        column_statements: list[str] = []

        for entry in rule_variant.result_vars:
            if entry.aggregate_name and entry.aggregate_name not in SUPPORTED_AGGREGATES:
                raise DroltaError(f"Use of unsupported aggregate: {entry}")

            column_statements.append(str(entry))
            output_vars.add(entry.var_name)

        # result_table_name = self.get_temp_table_name()
        result_table_name = f"temp__{rule_variant.name}_{key}"

        sql_stmt_lines: list[str] = [
            f"CREATE TEMPORARY TABLE {result_table_name} AS",
            f"SELECT {', '.join(column_statements)}",
            f"FROM {table.name}",
        ]

        if rule_variant.group_by:
            sql_stmt_lines.append(group_by_to_str(rule_variant.group_by))

        if rule_variant.order_by:
            sql_stmt_lines.append(order_by_to_str(rule_variant.order_by))

        if rule_variant.limit:
            sql_stmt_lines.append(limit_clause_to_str(rule_variant.limit))

        sql_stmt_lines.append(";")

        sql_stmt = "\n".join(sql_stmt_lines)

        _logger.debug("Executing Rule SQL...")
        _logger.debug(FormattedSqlString(sql_stmt))

        self.db.execute(sql_stmt)

        return TempTable(result_table_name, output_vars)

    def resolve_predicate_name(self, name: str) -> str:
        """Resolve the final name of a predicate from a potential alias."""

        if name in self._alias_resolution_cache:
            return self._alias_resolution_cache[name]

        final_name = name
        # Maintain a list of all aliases visited during resolution.
        resolution_path: list[str] = []

        while final_name in self._aliases:
            resolution_path.append(final_name)
            final_name = self._aliases[final_name]

        # Update the cache for all aliases visited along the way
        for visited_name in resolution_path:
            self._alias_resolution_cache[visited_name] = final_name

        return final_name

    def get_temp_table_name(self) -> str:
        """Generate a name for the next temporary table."""
        current_scope = self.get_scope()

        table_name = (
            self.TEMP_TABLE_PREFIX
            + f"{self._next_query_id}_"
            + f"{current_scope.scope_id}_"
            + str(current_scope.next_table_id)
        )

        current_scope.next_table_id += 1

        return table_name

    def get_scope(self) -> Scope:
        """Get the current scope."""
        if self._scope_stack:
            return self._scope_stack[-1]

        return self._push_scope()

    def _push_scope(self, output_vars: Optional[list[ResultVariable]] = None) -> Scope:
        """Push a new scope on the stack."""
        if self._scope_stack:
            scope = Scope(scope_id=self._scope_stack[-1].scope_id + 1)
        else:
            scope = Scope(scope_id=0)

        if output_vars:
            scope.output_vars = output_vars

        self._scope_stack.append(scope)
        return scope

    def pop_scope(self) -> Scope:
        """Pop the current scope."""
        scope = self._scope_stack.pop()
        self._destroy_tables_in_scope(scope)
        return scope

    def clear_scope_stack(self) -> None:
        """Clear all scopes from the stack."""

        while self._scope_stack:
            self.pop_scope()

    def _destroy_tables_in_scope(self, scope: Scope) -> None:
        """Destroy all temporary tables at the given scope."""

        while scope.tables:
            table = scope.tables.pop()
            self.db.drop_table(table.name)

        scope.tables.clear()

    def clear_query_cache(self) -> None:
        """Clear all internal caches related to query execution."""

        if self.result:
            self.result.destroy()
            self.result = None

        for rule_name in self._materialized_this_query:
            self.db.drop_table(f"{rule_name}__full")

        self._materialized_this_query.clear()
        self._table_column_name_cache.clear()
        self._alias_resolution_cache.clear()

    def _refresh_connected_components(self) -> None:
        """Recalculate the strongly connected components between rules."""
        dependency_graph = build_rule_dependency_graph(self._rules)
        connected_components = get_connected_components(dependency_graph)
        self.sccs = connected_components

    def _exec(self, sql_str: str) -> None:
        """Execute the given SQL string on the database."""
        self.db.execute(sql_str)

    def _get_table_column_names(self, table_name: str) -> list[str]:
        """Get the column names of the given table sorted by definition order."""
        if table_name in self._table_column_name_cache:
            return self._table_column_name_cache[table_name]

        cursor = self.db.conn.cursor()
        result: list[tuple[str,]] = cursor.execute(f"""
            SELECT name
            FROM pragma_table_info('{table_name}')
            ORDER BY cid;
            """).fetchall()
        cursor.close()
        column_names = [x[0] for x in result]
        self._table_column_name_cache[table_name] = column_names
        return column_names

    def _row_count(self, table_name: str) -> int:
        """Get the number of rows in a table."""

        # Raise key error because no table was found with the given name
        raise KeyError(table_name)

    def _get_scc_for(self, name: str) -> Optional[set[str]]:
        """Get the strongly connected component containing the given rule name."""
        for group in self.sccs:
            if name in group:
                return group

        return None

    def _check_rule_has_self_loop(self, rule_name: str) -> bool:
        """Check if the rule with the given name has a self loop.

        Parameters
        ----------
        rule_name
            The name of the rule to check.

        Returns
        -------
        bool
            True if the rule has a self loop, False otherwise.

        Raises
        ------
        KeyError
            No rule exists with the given name.
        """
        if rule_name not in self._rules:
            raise KeyError(f"No rule found with the name: {rule_name}")

        rule = self._rules[rule_name]

        for rule_variant in rule.variants:
            for where_stmt in rule_variant.where_expressions.statements:
                if isinstance(where_stmt, PredicateExprNode):
                    resolved_rule_name = self.resolve_predicate_name(where_stmt.name)
                    if resolved_rule_name == rule_name:
                        return True
                elif isinstance(where_stmt, PredicateNegationExprNode):
                    resolved_rule_name = self.resolve_predicate_name(
                        where_stmt.expr.name
                    )
                    if resolved_rule_name == rule_name:
                        return True

        return False

    def _copy_table(self, destination_name: str, source_name: str) -> None:
        """Copy the contents of one table to another table."""
        pass

    def _union_into(self, destination_name: str, source_name: str, create_dest: bool = True) -> None:
        """Union the contents of the source table into the destination_table.

        Parameters
        ----------
        destination_name
            The name of the table to union into.
        source_name
            The name of the table to union from.
        create_dest
            If True, create the destination table if none exist with the given name.
        """
        pass

    def _scc_refs_in_clause(self, rule_variant: RuleVariant, scc: set[str]) -> list[str]:
        return []

    def _evaluate_scc(self, scc: set[str]) -> None:
        """Evaluate all the rules in given SCC and create temp tables for their results."""

        for name in scc:
            # self._create_empty(f"{name}__full")
            self._run_seed_rules(
                name, self._rules[name].variants, scc
            )  # clauses with no ref into scc
            self._copy_table(f"{name}__full_new", f"{name}__delta")
            self._union_into(f"{name}__full", f"{name}__full_new")

        changed = True
        while changed:
            changed = False
            for name in scc:
                # self._create_empty(f"{name}__new")
                for rule_variant in self._rules[name].variants:
                    if not self._check_rule_references_scc(rule_variant, scc):
                        continue  # already handled in seeding

                    for recursive_ref in self._scc_refs_in_clause(rule_variant, scc):
                        # evaluate this clause with recursive_ref bound to its __delta,
                        # all other scc members bound to their __full
                        self._eval_rule_variant(name, rule_variant, recursive_ref, scc)

                # new tuples = new - full (this is the diff that drives termination)
                self._exec(f"""
                    CREATE TEMP TABLE "{name}__diff" AS
                    SELECT * FROM "{name}__new"
                    EXCEPT
                    SELECT * FROM "{name}__full"
                """)
                if self._row_count(f"{name}__diff") > 0:
                    changed = True

            # promote diffs to full/delta only after all group members computed
            for name in scc:
                self._exec(f'INSERT INTO "{name}__full" SELECT * FROM "{name}__diff"')
                self._exec(f'DROP TABLE "{name}__delta"')
                self._exec(f'ALTER TABLE "{name}__diff" RENAME TO "{name}__delta"')
                self._exec(f'DROP TABLE "{name}__new"')

    def _check_rule_references_scc(
        self, rule_variant: RuleVariant, scc: set[str]
    ) -> bool:
        """Return true if any expressions within the rule variant reference the given scc."""

        # Loop through all the where statements, specifically looking for predicates
        # and predicate negation statements. The names of the referenced predicates
        # are resolved and checked against the scc.
        for where_stmt in rule_variant.where_expressions.statements:

            if where_stmt.get_type() == NodeType.PREDICATE_EXPR:
                predicate_node = cast(PredicateExprNode, where_stmt)
                resolved_predicate_name = self.resolve_predicate_name(
                    predicate_node.name
                )
                if resolved_predicate_name in scc:
                    return True

            elif where_stmt.get_type() == NodeType.PREDICATE_NEGATION_EXPR:
                predicate_node = cast(PredicateExprNode, where_stmt)
                resolved_predicate_name = self.resolve_predicate_name(
                    predicate_node.name
                )
                if resolved_predicate_name in scc:
                    return True

        return False

    def _run_seed_rules(
        self, name: str, rule_variants: list[RuleVariant], scc: set[str]
    ) -> None:
        """Evaluate all non-recursive rules for a rule and union results
        into '{name}__full_new', the seed data for the fixpoint loop."""

        seed_rules = [
            clause
            for clause in rule_variants
            if not self._check_rule_references_scc(clause, scc)
        ]

        if not seed_rules:
            raise DroltaError(
                f"Recursive rule '{name}' has no non-recursive base case."
            )

        for rule_variant in seed_rules:
            self._push_scope([v.clone() for v in rule_variant.result_vars])

            where_expressions = sorted(
                rule_variant.where_expressions.statements, key=get_execution_order
            )

            for expr in where_expressions:
                expr_type = expr.get_type()
                if expr_type == NodeType.PREDICATE_EXPR:
                    self.visit_predicate(cast(PredicateExprNode, expr))
                elif is_filter_expression(expr):
                    self.visit_filter(cast(FilterExprNode, expr))
                elif expr_type == NodeType.PREDICATE_NEGATION_EXPR:
                    self.visit_not_predicate(cast(PredicateNegationExprNode, expr))
                self._join_tables_with_shared_vars()

            self._cross_join_tables_in_scope(self.get_scope())
            clause_result_table = self.get_scope().tables.pop()

            self._exec(f"""
                INSERT INTO "{name}__full_new"
                SELECT DISTINCT * FROM "{clause_result_table.name}"
            """)
