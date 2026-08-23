lexer grammar DroltaLexer;

options {
    caseInsensitive = true;
}

S_COL: ';';
DOT: '.';
OPEN_PAR: '(';
CLOSE_PAR: ')';
BRACKET_L: '[';
BRACKET_R: ']';
DBL_COL: '::';
COMMA: ',';
FIND: 'FIND';
WHERE: 'WHERE';
OR: 'OR';
AND: 'AND';
NOT: 'NOT';
LIMIT: 'LIMIT';
BY: 'BY';
IN: 'IN';
ORDER: 'ORDER';
GROUP: 'GROUP';
USING: 'USING';
DEFINE: 'DEFINE';
ALIAS: 'ALIAS';
AS: 'AS';
EQ: '=';
NEQ: '!=';
LTE: '<=';
LT: '<';
GTE: '>=';
GT: '>';
ASC: 'ASC';
DESC: 'DESC';
OFFSET: 'OFFSET';
FIRST: 'FIRST';
LAST: 'LAST';
NULLS: 'NULLS';
NULL: 'NULL';
TRUE: 'TRUE';
FALSE: 'FALSE';
VAR_PREFIX: '?';

IDENTIFIER: [a-z_\u007F-\uFFFF] [a-z_0-9\u007F-\uFFFF]*;

INT_LITERAL: [-+]? [1-9][0-9]*;

FLOAT_LITERAL: [-+]? [0-9]* '.' [0-9]* [1-9];

STRING_LITERAL: '"' ( '\\"' | ~('"'))* '"';

SINGLE_LINE_COMMENT: '--' ~[\r\n]* (('\r'? '\n') | EOF) -> channel(HIDDEN);

MULTILINE_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

WHITESPACE: [ \u000B\t\r\n] -> channel(HIDDEN);

fragment HEX_DIGIT : [0-9A-F];
fragment DIGIT     : [0-9];
