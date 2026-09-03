# pylint: disable=C0302
"""Drolta abstract syntax tree implementation."""

from __future__ import annotations

import enum
import logging
from abc import ABC
from typing import Any, Optional, cast

import antlr4

from drolta.parsing.DroltaLexer import DroltaLexer
from drolta.parsing.DroltaParser import DroltaParser
from drolta.parsing.DroltaParserVisitor import DroltaParserVisitor

_logger = logging.getLogger(__name__)


class NodeType(enum.IntEnum):
    """All expressions supported by drolta scripts."""

    PROGRAM = enum.auto()
    ALIAS_DECLARATION = enum.auto()
    RULE_DECLARATION = enum.auto()
    QUERY = enum.auto()
    FIND_CLAUSE = enum.auto()
    DEFINE_CLAUSE = enum.auto()
    WHERE_CLAUSE = enum.auto()
    ORDERING_TERM = enum.auto()
    ORDERING_TERM_LIST = enum.auto()
    ORDER_BY_CLAUSE = enum.auto()
    GROUP_BY_CLAUSE = enum.auto()
    LIMIT_CLAUSE = enum.auto()
    PREDICATE_EXPR = enum.auto()
    PREDICATE_NEGATION_EXPR = enum.auto()
    NAMED_PARAM = enum.auto()
    NAMED_PARAM_LIST = enum.auto()
    POSITIONAL_PARAM_LIST = enum.auto()
    VARIABLE = enum.auto()
    VARIABLE_LIST = enum.auto()
    INT_LITERAL = enum.auto()
    FLOAT_LITERAL = enum.auto()
    STRING_LITERAL = enum.auto()
    BOOL_LITERAL = enum.auto()
    NULL_LITERAL = enum.auto()
    ATOM_LIST = enum.auto()
    OR_FILTER_EXPR = enum.auto()
    AND_FILTER_EXPR = enum.auto()
    NOT_FILTER_EXPR = enum.auto()
    COMPARISON_FILTER = enum.auto()
    MEMBERSHIP_FILTER = enum.auto()
    RESULT_VARIABLE = enum.auto()
    RESULT_VARIABLE_LIST = enum.auto()


class ComparisonOp(enum.IntEnum):
    """Comparison operators."""

    LT = enum.auto()
    GT = enum.auto()
    LTE = enum.auto()
    GTE = enum.auto()
    EQ = enum.auto()
    NEQ = enum.auto()


class ASTNode(ABC):
    """Abstract base class for all nodes in the abstract syntax tree."""

    __slots__ = ("_node_type",)

    _node_type: NodeType

    def __init__(self, node_type: NodeType) -> None:
        self._node_type = node_type

    def get_type(self) -> NodeType:
        return self._node_type


class AtomNode(ASTNode):
    """Parent node for all atom and literal nodes."""


class AtomListNode(ASTNode):
    """A list of atoms."""

    __slots__ = ("items",)

    items: list[AtomNode]

    def __init__(self, items: list[AtomNode]) -> None:
        super().__init__(NodeType.ATOM_LIST)
        self.items = items


class VariableNode(AtomNode):
    """A node containing the name of a variable."""

    __slots__ = ("value",)

    value: str

    def __init__(self, variable: str) -> None:
        super().__init__(NodeType.VARIABLE)
        self.value = variable

    def __str__(self) -> str:
        return self.value


class IntLiteralNode(AtomNode):
    """A node containing a single integer value."""

    __slots__ = ("value",)

    value: int

    def __init__(self, value: int) -> None:
        super().__init__(NodeType.INT_LITERAL)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class FloatLiteralNode(AtomNode):
    """A node containing a single float value."""

    __slots__ = ("value",)

    value: float

    def __init__(self, value: float) -> None:
        super().__init__(NodeType.FLOAT_LITERAL)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class StringLiteralNode(AtomNode):
    """A node containing a single string value."""

    __slots__ = ("value",)

    value: str

    def __init__(self, value: str) -> None:
        super().__init__(NodeType.STRING_LITERAL)
        self.value = value

    def __str__(self) -> str:
        return f"'{self.value}'"

class BoolLiteralNode(AtomNode):
    """A node containing a single boolean value."""

    __slots__ = ("value",)

    value: bool

    def __init__(self, value: bool) -> None:
        super().__init__(NodeType.BOOL_LITERAL)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class NullLiteralNode(AtomNode):
    """A null expression"""

    def __init__(self) -> None:
        super().__init__(NodeType.NULL_LITERAL)

    def __str__(self) -> str:
        return "NULL"


class NamedParamNode(ASTNode):
    """A single named parameter within a predicate call."""

    __slots__ = ("column_name", "value")

    column_name: str
    value: AtomNode

    def __init__(self, column_name: str, value: AtomNode) -> None:
        super().__init__(NodeType.NAMED_PARAM)
        self.column_name = column_name
        self.value = value


class NamedParamListNode(ASTNode):
    """A list of named params within a predicate call."""

    __slots__ = ("params",)

    params: list[NamedParamNode]

    def __init__(self, params: list[NamedParamNode]) -> None:
        super().__init__(NodeType.NAMED_PARAM_LIST)
        self.params = params


class PositionalParamListNode(ASTNode):
    """A list of positional parameters within a predicate call."""

    __slots__ = ("params",)

    params: list[AtomNode]

    def __init__(self, params: list[AtomNode]) -> None:
        super().__init__(NodeType.POSITIONAL_PARAM_LIST)
        self.params = params


class WhereStmtNode(ASTNode):
    """Base class for all where statement nodes."""


class FilterExprNode(ASTNode):
    """Base class for all filter expression nodes."""


class NOTFilterExprNode(FilterExprNode):
    """Logical-NOT filter expression."""

    __slots__ = ("expr",)

    expr: FilterExprNode

    def __init__(self, expr: FilterExprNode) -> None:
        super().__init__(NodeType.NOT_FILTER_EXPR)
        self.expr = expr


class ORFilterExprNode(FilterExprNode):
    """Logical-OR filter expressions."""

    __slots__ = ("left", "right")

    left: FilterExprNode
    right: FilterExprNode

    def __init__(self, left: FilterExprNode, right: FilterExprNode) -> None:
        super().__init__(NodeType.OR_FILTER_EXPR)
        self.left = left
        self.right = right


class ANDFilterExprNode(FilterExprNode):
    """Logical-AND filter expressions."""

    __slots__ = ("left", "right")

    left: FilterExprNode
    right: FilterExprNode

    def __init__(self, left: FilterExprNode, right: FilterExprNode) -> None:
        super().__init__(NodeType.AND_FILTER_EXPR)
        self.left = left
        self.right = right


class ComparisonFilterExprNode(FilterExprNode):
    """Comparison filter expressions."""

    __slots__ = ("op", "left", "right")

    op: ComparisonOp
    left: FilterExprNode
    right: FilterExprNode

    def __init__(
        self, left: FilterExprNode, right: FilterExprNode, op: ComparisonOp
    ) -> None:
        super().__init__(NodeType.COMPARISON_FILTER)
        self.left = left
        self.right = right
        self.op = op


class MembershipFilterExprNode(FilterExprNode):
    """Membership checking filter expression."""

    __slots__ = ("left", "is_negated", "values")

    left: VariableNode
    is_negated: bool
    values: AtomListNode

    def __init__(
        self, is_negated: bool, left: VariableNode, values: AtomListNode
    ) -> None:
        super().__init__(NodeType.MEMBERSHIP_FILTER)
        self.is_negated = is_negated
        self.left = left
        self.values = values


class PredicateExprNode(ASTNode):
    """A predicate expression."""

    __slots__ = ("name", "positional_params", "named_params")

    name: str
    positional_params: Optional[PositionalParamListNode]
    named_params: Optional[NamedParamListNode]

    def __init__(
        self,
        name: str,
        positional_params: Optional[PositionalParamListNode],
        named_params: Optional[NamedParamListNode],
    ) -> None:
        super().__init__(NodeType.PREDICATE_EXPR)
        self.name = name
        self.positional_params = positional_params
        self.named_params = named_params


class PredicateNegationExprNode(ASTNode):
    """Not predicate expression."""

    __slots__ = ("expr",)

    expr: PredicateExprNode

    def __init__(self, expr: PredicateExprNode) -> None:
        super().__init__(NodeType.PREDICATE_NEGATION_EXPR)
        self.expr = expr


class SortDirection(enum.IntEnum):
    """Sorting order for columns in an ORDER BY clause."""

    NONE = enum.auto()
    ASC = enum.auto()
    DESC = enum.auto()


class NullsSortDirection(enum.IntEnum):
    """Sorting order for NULL values in an ORDER BY clause."""

    NONE = enum.auto()
    FIRST = enum.auto()
    LAST = enum.auto()


class OrderingTermNode(ASTNode):
    """A term used to order query output."""

    __slots__ = ("variable", "sort_dir", "nulls_sort_dir")

    variable: VariableNode
    sort_dir: SortDirection
    nulls_sort_dir: NullsSortDirection

    def __init__(
        self,
        variable: VariableNode,
        sort_dir: SortDirection = SortDirection.NONE,
        nulls_sort_dir: NullsSortDirection = NullsSortDirection.NONE,
    ) -> None:
        super().__init__(NodeType.ORDERING_TERM)
        self.variable = variable
        self.sort_dir = sort_dir
        self.nulls_sort_dir = nulls_sort_dir


class OrderingTermListNode(ASTNode):
    """A list of ordering terms for a ORDER BY clause."""

    __slots__ = ("items",)

    items: list[OrderingTermNode]

    def __init__(
        self,
        items: list[OrderingTermNode],
    ) -> None:
        super().__init__(NodeType.ORDERING_TERM_LIST)
        self.items = items


class OrderByClauseNode(ASTNode):
    """Order by expression."""

    __slots__ = ("terms",)

    terms: OrderingTermListNode

    def __init__(self, terms: OrderingTermListNode) -> None:
        super().__init__(NodeType.ORDER_BY_CLAUSE)
        self.terms = terms


class VariableListNode(ASTNode):
    """A list of variables."""

    __slots__ = ("items",)

    items: list[VariableNode]

    def __init__(
        self,
        items: list[VariableNode],
    ) -> None:
        super().__init__(NodeType.VARIABLE_LIST)
        self.items = items


class GroupByClauseNode(ASTNode):
    """Group by expression."""

    __slots__ = ("grouping_terms",)

    grouping_terms: VariableListNode

    def __init__(self, grouping_terms: VariableListNode) -> None:
        super().__init__(NodeType.GROUP_BY_CLAUSE)
        self.grouping_terms = grouping_terms


class LimitClauseNode(ASTNode):
    """Limit expression."""

    __slots__ = ("value", "offset")

    value: int
    offset: int

    def __init__(self, value: int, offset: int = -1) -> None:
        super().__init__(NodeType.LIMIT_CLAUSE)
        self.value = value
        self.offset = offset


class ProgramStmtNode(ASTNode):
    """Base class for all program-level statements."""


class AliasDeclarationNode(ProgramStmtNode):
    """A node that declares a new predicate alias."""

    __slots__ = ("original_name", "alias")

    original_name: str
    alias: str

    def __init__(self, original_name: str, alias: str) -> None:
        super().__init__(NodeType.ALIAS_DECLARATION)
        self.original_name = original_name
        self.alias = alias


class ResultVariableNode(ASTNode):
    """A variable returned by a rule or query."""

    __slots__ = ("aggregate_name", "variable", "alias")

    aggregate_name: str
    variable: VariableNode
    alias: str

    def __init__(
        self, variable: VariableNode, aggregate_name: str = "", alias: str = ""
    ) -> None:
        super().__init__(NodeType.RESULT_VARIABLE)
        self.variable = variable
        self.aggregate_name = aggregate_name
        self.alias = alias


class ResultVariableListNode(ASTNode):
    """A list of result variables within a DEFINE or FIND clause."""

    __slots__ = ("items",)

    items: list[ResultVariableNode]

    def __init__(
        self,
        items: list[ResultVariableNode],
    ) -> None:
        super().__init__(NodeType.RESULT_VARIABLE_LIST)
        self.items = items


class DefineClauseNode(ASTNode):
    """The DEFINE clause of a rule declaration."""

    __slots__ = (
        "name",
        "result_vars",
    )

    name: str
    result_vars: ResultVariableListNode

    def __init__(
        self,
        name: str,
        result_vars: ResultVariableListNode,
    ) -> None:
        super().__init__(NodeType.DEFINE_CLAUSE)
        self.name = name
        self.result_vars = result_vars


class WhereClauseNode(ASTNode):
    """The WHERE clause of a rule declaration or query expression."""

    __slots__ = ("statements",)

    statements: list[WhereStmtNode]

    def __init__(self, statements: list[WhereStmtNode]) -> None:
        super().__init__(NodeType.WHERE_CLAUSE)
        self.statements = statements


class RuleDeclarationNode(ProgramStmtNode):
    """Declares a new Drolta rule."""

    __slots__ = (
        "define_clause",
        "where_clause",
        "order_by",
        "group_by",
        "limit",
    )

    define_clause: DefineClauseNode
    where_clause: WhereClauseNode
    order_by: Optional[OrderByClauseNode]
    group_by: Optional[GroupByClauseNode]
    limit: Optional[LimitClauseNode]

    def __init__(
        self,
        define_clause: DefineClauseNode,
        where_clause: WhereClauseNode,
        order_by: Optional[OrderByClauseNode] = None,
        group_by: Optional[GroupByClauseNode] = None,
        limit: Optional[LimitClauseNode] = None,
    ) -> None:
        super().__init__(NodeType.RULE_DECLARATION)
        self.define_clause = define_clause
        self.where_clause = where_clause
        self.order_by = order_by
        self.group_by = group_by
        self.limit = limit


class FindClauseNode(ASTNode):
    """The FIND clause of a query expression."""

    __slots__ = ("result_vars",)

    result_vars: ResultVariableListNode

    def __init__(
        self,
        result_vars: ResultVariableListNode,
    ) -> None:
        super().__init__(NodeType.FIND_CLAUSE)
        self.result_vars = result_vars


class QueryExprNode(ProgramStmtNode):
    """A query expression."""

    __slots__ = ("find_clause", "where_clause", "order_by", "group_by", "limit")

    find_clause: FindClauseNode
    where_clause: WhereClauseNode
    order_by: Optional[OrderByClauseNode]
    group_by: Optional[GroupByClauseNode]
    limit: Optional[LimitClauseNode]

    def __init__(
        self,
        find_clause: FindClauseNode,
        where_clause: WhereClauseNode,
        order_by: Optional[OrderByClauseNode] = None,
        group_by: Optional[GroupByClauseNode] = None,
        limit: Optional[LimitClauseNode] = None,
    ) -> None:
        super().__init__(NodeType.QUERY)
        self.find_clause = find_clause
        self.where_clause = where_clause
        self.order_by = order_by
        self.group_by = group_by
        self.limit = limit


class ProgramNode(ASTNode):
    """The root node of Drolta ASTs."""

    __slots__ = ("children",)

    children: list[ProgramStmtNode]

    def __init__(self, children: list[ProgramStmtNode]) -> None:
        super().__init__(NodeType.PROGRAM)
        self.children = children


class _SyntaxErrorListener(antlr4.DiagnosticErrorListener):
    __slots__ = ("error_count", "error_messages")

    error_count: int
    error_messages: list[str]

    def __init__(self) -> None:
        super().__init__()
        self.error_count = 0
        self.error_messages = []

    def syntaxError(
        self,
        recognizer: Any,
        offendingSymbol: Any,
        line: int,
        column: int,
        msg: str,
        e: Any,
    ) -> None:
        self.error_count += 1
        self.error_messages.append(f"line {line}:{column} {msg}")

    def clear(self) -> None:
        """Clear all cached errors."""
        self.error_count = 0
        self.error_messages.clear()


class ASTBuilderVisitor(DroltaParserVisitor):
    """A parse tree visitor that builds a Drolta abstract syntax tree."""

    def visitProg(self, ctx: DroltaParser.ProgContext):  # type: ignore
        return ProgramNode([self.visit(s) for s in ctx.drolta_stmt_list().drolta_stmt()])  # type: ignore

    def visitDeclare_alias_stmt(self, ctx: DroltaParser.Declare_alias_stmtContext | Any):  # type: ignore
        return AliasDeclarationNode(
            alias=str(ctx.alias.text),  # type: ignore
            original_name=str(ctx.original.text),  # type: ignore
        )

    def visitDeclare_rule_stmt(self, ctx: DroltaParser.Declare_rule_stmtContext):  # type: ignore
        node = RuleDeclarationNode(
            define_clause=cast(DefineClauseNode, self.visit(ctx.define_clause())),  # type: ignore
            where_clause=cast(WhereClauseNode, self.visit(ctx.where_clause())),  # type: ignore
        )

        if ctx.group_by_clause() is not None:
            node.group_by = self.visit(ctx.group_by_clause())  # type: ignore

        if ctx.order_by_clause() is not None:
            node.order_by = self.visit(ctx.order_by_clause())  # type: ignore

        if ctx.limit_clause() is not None:
            node.limit = self.visit(ctx.limit_clause())  # type: ignore

        return node

    def visitQuery_stmt(self, ctx: DroltaParser.Query_stmtContext):  # type: ignore
        node = QueryExprNode(
            find_clause=cast(FindClauseNode, self.visit(ctx.find_clause())),  # type: ignore
            where_clause=cast(WhereClauseNode, self.visit(ctx.where_clause())),  # type: ignore
        )

        if ctx.group_by_clause() is not None:
            node.group_by = self.visit(ctx.group_by_clause())  # type: ignore

        if ctx.order_by_clause() is not None:
            node.order_by = self.visit(ctx.order_by_clause())  # type: ignore

        if ctx.limit_clause() is not None:
            node.limit = self.visit(ctx.limit_clause())  # type: ignore

        return node

    def visitDefine_clause(self, ctx: DroltaParser.Define_clauseContext):  # type: ignore
        return DefineClauseNode(str(ctx.ruleName.text), self.visit(ctx.result_var_list()))  # type: ignore

    def visitFind_clause(self, ctx: DroltaParser.Find_clauseContext):  # type: ignore
        varList: ResultVariableListNode = (
            self.visit(ctx.result_var_list())  # type: ignore
            if ctx.result_var_list() is not None
            else None
        )
        return FindClauseNode(varList)

    def visitResult_var_list(self, ctx: DroltaParser.Result_var_listContext):  # type: ignore
        return ResultVariableListNode([self.visit(n) for n in ctx.result_var()])  # type: ignore

    def visitResult_var(self, ctx: DroltaParser.Result_varContext):  # type: ignore
        node = ResultVariableNode(self.visit(ctx.variable()))  # type: ignore

        if ctx.aggregateName is not None:
            node.aggregate_name = ctx.aggregateName.text

        if ctx.variable_alias() is not None:
            node.alias = ctx.variable_alias().alias.text  # type: ignore

        return node

    def visitWhere_clause(self, ctx: DroltaParser.Where_clauseContext):  # type: ignore
        return WhereClauseNode([self.visit(n) for n in ctx.where_stmt()])  # type: ignore

    def visitOrder_by_clause(self, ctx: DroltaParser.Order_by_clauseContext):  # type: ignore
        return OrderByClauseNode(self.visit(ctx.ordering_term_list()))  # type: ignore

    def visitOrdering_term_list(self, ctx: DroltaParser.Ordering_term_listContext):  # type: ignore
        orderingTerms: list[OrderingTermNode] = [self.visit(n) for n in ctx.ordering_term()]  # type: ignore
        return OrderingTermListNode(orderingTerms)

    def visitOrdering_term(self, ctx: DroltaParser.Ordering_termContext):  # type: ignore
        variable: VariableNode = self.visit(ctx.variable())  # type: ignore

        sortDirection = SortDirection.NONE
        nullsOrder = NullsSortDirection.NONE

        if ctx.ASC() is not None:
            sortDirection = SortDirection.ASC
        elif ctx.DESC() is not None:
            sortDirection = SortDirection.DESC

        if ctx.FIRST() is not None:
            nullsOrder = NullsSortDirection.FIRST
        elif ctx.LAST() is not None:
            nullsOrder = NullsSortDirection.LAST

        return OrderingTermNode(variable, sortDirection, nullsOrder)

    def visitGroup_by_clause(self, ctx: DroltaParser.Group_by_clauseContext):  # type: ignore
        return GroupByClauseNode(self.visit(ctx.variable_list()))  # type: ignore

    def visitVariable_list(self, ctx: DroltaParser.Variable_listContext):  # type: ignore
        variables: list[VariableNode] = [self.visit(n) for n in ctx.variable()]  # type: ignore
        return VariableListNode(variables)

    def visitLimit_clause(self, ctx: DroltaParser.Limit_clauseContext):  # type: ignore
        limit = int(ctx.limitVal.text)  # type: ignore
        offset = int(ctx.offsetVal.text) if ctx.offsetVal is not None else -1
        return LimitClauseNode(limit, offset)

    def visitPredicate_neg_stmt(self, ctx: DroltaParser.Predicate_neg_stmtContext | Any):  # type: ignore
        return PredicateNegationExprNode(
            cast(PredicateExprNode, self.visit(ctx.predicate_stmt()))  # type: ignore
        )

    def visitPredicate_stmt(self, ctx: DroltaParser.Predicate_stmtContext | Any):  # type: ignore
        return PredicateExprNode(
            name=str(ctx.IDENTIFIER().getText()),  # type: ignore
            positional_params=(
                cast(PositionalParamListNode, self.visit(ctx.positional_param_list()))  # type: ignore
                if ctx.positional_param_list() is not None
                else None
            ),
            named_params=(
                cast(NamedParamListNode, self.visit(ctx.named_param_list()))  # type: ignore
                if ctx.named_param_list() is not None
                else None
            ),
        )

    def visitPositional_param_list(self, ctx: DroltaParser.Positional_param_listContext | Any):  # type: ignore
        return PositionalParamListNode(
            params=[cast(AtomNode, self.visit(child)) for child in ctx.atom()]  # type: ignore
        )

    def visitNamed_param_list(self, ctx: DroltaParser.Named_param_listContext | Any):  # type: ignore
        return NamedParamListNode(
            params=[cast(NamedParamNode, self.visit(child)) for child in ctx.named_param()]  # type: ignore
        )

    def visitNamed_param(self, ctx: DroltaParser.Named_paramContext | Any):  # type: ignore
        return NamedParamNode(
            column_name=str(ctx.IDENTIFIER().getText()),  # type: ignore, # type: ignore
            value=cast(AtomNode, self.visit(ctx.atom())),  # type: ignore
        )

    def visitComparisonFilterStmt(self, ctx: DroltaParser.ComparisonFilterStmtContext | Any):  # type: ignore
        return ComparisonFilterExprNode(
            left=cast(VariableNode, self.visit(ctx.left)),  # type: ignore
            right=cast(AtomNode, self.visit(ctx.right)),  # type: ignore
            op=self.parse_comparison_op(ctx.op.getText()),  # type: ignore
        )

    def visitMembershipFilterStmt(self, ctx: DroltaParser.MembershipFilterStmtContext | Any):  # type: ignore
        return MembershipFilterExprNode(
            left=cast(VariableNode, self.visit(ctx.left)),  # type: ignore
            is_negated=ctx.NOT() != None,
            values=cast(AtomListNode, self.visit(ctx.atom_list())),  # type: ignore
        )

    def visitAndFilterStmt(self, ctx: DroltaParser.OrFilterStmtContext | Any):  # type: ignore
        return ANDFilterExprNode(
            left=cast(FilterExprNode, self.visit(ctx.left)),  # type: ignore
            right=cast(FilterExprNode, self.visit(ctx.right)),  # type: ignore
        )

    def visitOrFilterStmt(self, ctx: DroltaParser.OrFilterStmtContext | Any):  # type: ignore
        return ORFilterExprNode(
            left=cast(FilterExprNode, self.visit(ctx.left)),  # type: ignore
            right=cast(FilterExprNode, self.visit(ctx.right)),  # type: ignore
        )

    def visitNotFilterStmt(self, ctx: DroltaParser.NotFilterStmtContext | Any):  # type: ignore
        return NOTFilterExprNode(cast(NOTFilterExprNode, self.visit(ctx.filter_stmt())))  # type: ignore

    def visitInt_literal(self, ctx: DroltaParser.Int_literalContext | Any):  # type: ignore
        return IntLiteralNode(int(ctx.getText()))

    def visitFloat_literal(self, ctx: DroltaParser.Float_literalContext | Any):  # type: ignore
        return FloatLiteralNode(float(ctx.getText()))

    def visitString_literal(self, ctx: DroltaParser.String_literalContext | Any):  # type: ignore
        return StringLiteralNode(ctx.getText()[1:-1])

    def visitNull_literal(self, ctx: DroltaParser.Null_literalContext | Any):  # type: ignore
        return NullLiteralNode()

    def visitBool_literal(self, ctx: DroltaParser.Bool_literalContext | Any):  # type: ignore
        text = ctx.getText().lower()
        return BoolLiteralNode(text == "true")

    def visitVariable(self, ctx: DroltaParser.VariableContext | Any):  # type: ignore
        return VariableNode(ctx.getText()[1:]) # Get the name without '?' prefix

    @staticmethod
    def parse_comparison_op(text: str) -> ComparisonOp:
        """Convert text to a comparison operation"""
        if text == "=":
            return ComparisonOp.EQ
        if text == "!=":
            return ComparisonOp.NEQ
        if text == "<=":
            return ComparisonOp.LTE
        if text == "<":
            return ComparisonOp.LT
        if text == ">=":
            return ComparisonOp.GTE
        if text == ">":
            return ComparisonOp.GT

        raise ValueError(f"Unrecognized comparison operator: '{text}'.")


def generate_ast(script_text: str) -> ASTNode:
    """Generate a Drolta AST from the given script text."""

    input_stream = antlr4.InputStream(script_text)
    lexer = DroltaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = DroltaParser(stream)
    error_listener = _SyntaxErrorListener()

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)  # type: ignore

    tree = parser.prog()

    if error_listener.error_count:
        error_message = "Syntax errors found in drolta script:\n"
        for msg in error_listener.error_messages:
            error_message += msg + "\n"

        _logger.error(error_message)

        raise SyntaxError(error_message)

    visitor = ASTBuilderVisitor()
    ast_root = visitor.visitProg(tree)

    return ast_root
