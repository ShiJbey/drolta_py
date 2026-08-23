parser grammar DroltaParser;

options {
    tokenVocab = DroltaLexer;
}

// Parser Rules

prog
    : drolta_stmt_list EOF
    ;

drolta_stmt_list
    : drolta_stmt (S_COL drolta_stmt?)*
    ;

drolta_stmt
    : declare_alias_stmt
    | declare_rule_stmt
    | query_stmt
    ;

declare_alias_stmt
    : ALIAS original = IDENTIFIER AS alias = IDENTIFIER
    ;

declare_rule_stmt
    : define_clause where_clause group_by_clause? order_by_clause? limit_clause?
    ;

define_clause
    : DEFINE ruleName = IDENTIFIER OPEN_PAR result_var_list? CLOSE_PAR
    ;

result_var_list
    : result_var (COMMA result_var)*
    ;

query_stmt
    : find_clause where_clause group_by_clause? order_by_clause? limit_clause?
    ;

find_clause
    : FIND result_var_list?
    ;

result_var
    : aggregateName = IDENTIFIER OPEN_PAR variable CLOSE_PAR variable_alias?
    | variable variable_alias?
    ;

variable_alias
    : AS alias = IDENTIFIER
    ;

where_clause
    : WHERE where_stmt+
    ;

order_by_clause
    : ORDER BY ordering_term_list
    ;

ordering_term_list
    : ordering_term (COMMA ordering_term)*
    ;

ordering_term
    : variable (ASC | DESC)? (NULLS (FIRST | LAST))?
    ;

group_by_clause
    : GROUP BY variable_list
    ;

variable_list
    : variable (COMMA variable)*
    ;

limit_clause
    : LIMIT limitVal = INT_LITERAL (OFFSET offsetVal = INT_LITERAL)?
    ;

where_stmt
    : filter_stmt
    | predicate_neg_stmt
    | predicate_stmt
    ;

filter_stmt
    : OPEN_PAR left = variable op = comparison_operator right = atom CLOSE_PAR	# ComparisonFilterStmt
    | OPEN_PAR left = variable NOT? IN atom_list CLOSE_PAR						# MembershipFilterStmt
    | OPEN_PAR left = filter_stmt AND right = filter_stmt CLOSE_PAR	            # AndFilterStmt
    | OPEN_PAR left = filter_stmt OR right = filter_stmt CLOSE_PAR	            # OrFilterStmt
    | OPEN_PAR NOT filter_stmt CLOSE_PAR									    # NotFilterStmt
    ;

atom_list
    : BRACKET_L (atom (COMMA atom)*)? BRACKET_R
    ;

comparison_operator
    : GT
    | GTE
    | LT
    | LTE
    | EQ
    | NEQ
    ;

predicate_neg_stmt
    : NOT predicate_stmt
    ;

predicate_stmt
    : PredicateName = IDENTIFIER OPEN_PAR positional_param_list CLOSE_PAR
    | PredicateName = IDENTIFIER OPEN_PAR named_param_list CLOSE_PAR
    | PredicateName = IDENTIFIER OPEN_PAR positional_param_list COMMA named_param_list CLOSE_PAR
    ;

positional_param_list
    : atom (COMMA atom)*
    ;

named_param_list
    : named_param (COMMA named_param)*
    ;

named_param
    : IDENTIFIER EQ atom
    ;

atom
    : variable          # variable_atom
    | INT_LITERAL       # int_literal
    | FLOAT_LITERAL     # float_literal
    | STRING_LITERAL    # string_literal
    | NULL              # null_literal
    | (TRUE | FALSE)    # bool_literal
    ;

variable
    : VAR_PREFIX IDENTIFIER
    ;
