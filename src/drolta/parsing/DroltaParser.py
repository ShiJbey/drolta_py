# Generated from DroltaParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,1,1,1,1,1,3,1,65,8,1,5,1,67,8,
        1,10,1,12,1,70,9,1,1,2,1,2,1,2,3,2,75,8,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,3,4,85,8,4,1,4,3,4,88,8,4,1,4,3,4,91,8,4,1,5,1,5,1,5,1,
        5,3,5,97,8,5,1,5,1,5,1,6,1,6,1,6,5,6,104,8,6,10,6,12,6,107,9,6,1,
        7,1,7,1,7,3,7,112,8,7,1,7,3,7,115,8,7,1,7,3,7,118,8,7,1,8,1,8,3,
        8,122,8,8,1,9,1,9,1,9,1,9,1,9,3,9,129,8,9,1,9,1,9,3,9,133,8,9,3,
        9,135,8,9,1,10,1,10,1,10,1,11,1,11,4,11,142,8,11,11,11,12,11,143,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,5,13,153,8,13,10,13,12,13,156,
        9,13,1,14,1,14,3,14,160,8,14,1,14,1,14,3,14,164,8,14,1,15,1,15,1,
        15,1,15,1,16,1,16,1,16,5,16,173,8,16,10,16,12,16,176,9,16,1,17,1,
        17,1,17,1,17,3,17,182,8,17,1,18,1,18,1,18,3,18,187,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,198,8,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,3,19,221,8,19,1,20,1,20,1,20,1,20,5,20,
        227,8,20,10,20,12,20,230,9,20,3,20,232,8,20,1,20,1,20,1,21,1,21,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,258,8,23,1,24,1,24,1,24,
        5,24,263,8,24,10,24,12,24,266,9,24,1,25,1,25,1,25,5,25,271,8,25,
        10,25,12,25,274,9,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,3,27,286,8,27,1,28,1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,
        4,1,0,29,30,1,0,32,33,1,0,23,28,1,0,36,37,301,0,58,1,0,0,0,2,61,
        1,0,0,0,4,74,1,0,0,0,6,76,1,0,0,0,8,81,1,0,0,0,10,92,1,0,0,0,12,
        100,1,0,0,0,14,108,1,0,0,0,16,119,1,0,0,0,18,134,1,0,0,0,20,136,
        1,0,0,0,22,139,1,0,0,0,24,145,1,0,0,0,26,149,1,0,0,0,28,157,1,0,
        0,0,30,165,1,0,0,0,32,169,1,0,0,0,34,177,1,0,0,0,36,186,1,0,0,0,
        38,220,1,0,0,0,40,222,1,0,0,0,42,235,1,0,0,0,44,237,1,0,0,0,46,257,
        1,0,0,0,48,259,1,0,0,0,50,267,1,0,0,0,52,275,1,0,0,0,54,285,1,0,
        0,0,56,287,1,0,0,0,58,59,3,2,1,0,59,60,5,0,0,1,60,1,1,0,0,0,61,68,
        3,4,2,0,62,64,5,1,0,0,63,65,3,4,2,0,64,63,1,0,0,0,64,65,1,0,0,0,
        65,67,1,0,0,0,66,62,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,3,1,0,0,0,70,68,1,0,0,0,71,75,3,6,3,0,72,75,3,8,4,0,73,
        75,3,14,7,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,5,1,0,0,
        0,76,77,5,21,0,0,77,78,5,39,0,0,78,79,5,22,0,0,79,80,5,39,0,0,80,
        7,1,0,0,0,81,82,3,10,5,0,82,84,3,22,11,0,83,85,3,30,15,0,84,83,1,
        0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,3,24,12,0,87,86,1,0,0,0,
        87,88,1,0,0,0,88,90,1,0,0,0,89,91,3,34,17,0,90,89,1,0,0,0,90,91,
        1,0,0,0,91,9,1,0,0,0,92,93,5,20,0,0,93,94,5,39,0,0,94,96,5,3,0,0,
        95,97,3,12,6,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,
        4,0,0,99,11,1,0,0,0,100,105,3,18,9,0,101,102,5,8,0,0,102,104,3,18,
        9,0,103,101,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,
        0,0,106,13,1,0,0,0,107,105,1,0,0,0,108,109,3,16,8,0,109,111,3,22,
        11,0,110,112,3,30,15,0,111,110,1,0,0,0,111,112,1,0,0,0,112,114,1,
        0,0,0,113,115,3,24,12,0,114,113,1,0,0,0,114,115,1,0,0,0,115,117,
        1,0,0,0,116,118,3,34,17,0,117,116,1,0,0,0,117,118,1,0,0,0,118,15,
        1,0,0,0,119,121,5,9,0,0,120,122,3,12,6,0,121,120,1,0,0,0,121,122,
        1,0,0,0,122,17,1,0,0,0,123,124,5,39,0,0,124,125,5,3,0,0,125,126,
        3,56,28,0,126,128,5,4,0,0,127,129,3,20,10,0,128,127,1,0,0,0,128,
        129,1,0,0,0,129,135,1,0,0,0,130,132,3,56,28,0,131,133,3,20,10,0,
        132,131,1,0,0,0,132,133,1,0,0,0,133,135,1,0,0,0,134,123,1,0,0,0,
        134,130,1,0,0,0,135,19,1,0,0,0,136,137,5,22,0,0,137,138,5,39,0,0,
        138,21,1,0,0,0,139,141,5,10,0,0,140,142,3,36,18,0,141,140,1,0,0,
        0,142,143,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,23,1,0,0,0,
        145,146,5,17,0,0,146,147,5,15,0,0,147,148,3,26,13,0,148,25,1,0,0,
        0,149,154,3,28,14,0,150,151,5,8,0,0,151,153,3,28,14,0,152,150,1,
        0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,27,1,0,
        0,0,156,154,1,0,0,0,157,159,3,56,28,0,158,160,7,0,0,0,159,158,1,
        0,0,0,159,160,1,0,0,0,160,163,1,0,0,0,161,162,5,34,0,0,162,164,7,
        1,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,29,1,0,0,0,165,166,5,18,
        0,0,166,167,5,15,0,0,167,168,3,32,16,0,168,31,1,0,0,0,169,174,3,
        56,28,0,170,171,5,8,0,0,171,173,3,56,28,0,172,170,1,0,0,0,173,176,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,33,1,0,0,0,176,174,1,
        0,0,0,177,178,5,14,0,0,178,181,5,40,0,0,179,180,5,31,0,0,180,182,
        5,40,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,35,1,0,0,0,183,187,
        3,38,19,0,184,187,3,44,22,0,185,187,3,46,23,0,186,183,1,0,0,0,186,
        184,1,0,0,0,186,185,1,0,0,0,187,37,1,0,0,0,188,189,5,3,0,0,189,190,
        3,56,28,0,190,191,3,42,21,0,191,192,3,54,27,0,192,193,5,4,0,0,193,
        221,1,0,0,0,194,195,5,3,0,0,195,197,3,56,28,0,196,198,5,13,0,0,197,
        196,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,5,16,0,0,200,
        201,3,40,20,0,201,202,5,4,0,0,202,221,1,0,0,0,203,204,5,3,0,0,204,
        205,3,38,19,0,205,206,5,12,0,0,206,207,3,38,19,0,207,208,5,4,0,0,
        208,221,1,0,0,0,209,210,5,3,0,0,210,211,3,38,19,0,211,212,5,11,0,
        0,212,213,3,38,19,0,213,214,5,4,0,0,214,221,1,0,0,0,215,216,5,3,
        0,0,216,217,5,13,0,0,217,218,3,38,19,0,218,219,5,4,0,0,219,221,1,
        0,0,0,220,188,1,0,0,0,220,194,1,0,0,0,220,203,1,0,0,0,220,209,1,
        0,0,0,220,215,1,0,0,0,221,39,1,0,0,0,222,231,5,5,0,0,223,228,3,54,
        27,0,224,225,5,8,0,0,225,227,3,54,27,0,226,224,1,0,0,0,227,230,1,
        0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,232,1,0,0,0,230,228,1,
        0,0,0,231,223,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,234,5,
        6,0,0,234,41,1,0,0,0,235,236,7,2,0,0,236,43,1,0,0,0,237,238,5,13,
        0,0,238,239,3,46,23,0,239,45,1,0,0,0,240,241,5,39,0,0,241,242,5,
        3,0,0,242,243,3,48,24,0,243,244,5,4,0,0,244,258,1,0,0,0,245,246,
        5,39,0,0,246,247,5,3,0,0,247,248,3,50,25,0,248,249,5,4,0,0,249,258,
        1,0,0,0,250,251,5,39,0,0,251,252,5,3,0,0,252,253,3,48,24,0,253,254,
        5,8,0,0,254,255,3,50,25,0,255,256,5,4,0,0,256,258,1,0,0,0,257,240,
        1,0,0,0,257,245,1,0,0,0,257,250,1,0,0,0,258,47,1,0,0,0,259,264,3,
        54,27,0,260,261,5,8,0,0,261,263,3,54,27,0,262,260,1,0,0,0,263,266,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,49,1,0,0,0,266,264,1,
        0,0,0,267,272,3,52,26,0,268,269,5,8,0,0,269,271,3,52,26,0,270,268,
        1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,51,1,
        0,0,0,274,272,1,0,0,0,275,276,5,39,0,0,276,277,5,23,0,0,277,278,
        3,54,27,0,278,53,1,0,0,0,279,286,3,56,28,0,280,286,5,40,0,0,281,
        286,5,41,0,0,282,286,5,42,0,0,283,286,5,35,0,0,284,286,7,3,0,0,285,
        279,1,0,0,0,285,280,1,0,0,0,285,281,1,0,0,0,285,282,1,0,0,0,285,
        283,1,0,0,0,285,284,1,0,0,0,286,55,1,0,0,0,287,288,5,38,0,0,288,
        289,5,39,0,0,289,57,1,0,0,0,30,64,68,74,84,87,90,96,105,111,114,
        117,121,128,132,134,143,154,159,163,174,181,186,197,220,228,231,
        257,264,272,285
    ]

class DroltaParser ( Parser ):

    grammarFileName = "DroltaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "'('", "')'", "'['", "']'", 
                     "'::'", "','", "'FIND'", "'WHERE'", "'OR'", "'AND'", 
                     "'NOT'", "'LIMIT'", "'BY'", "'IN'", "'ORDER'", "'GROUP'", 
                     "'USING'", "'DEFINE'", "'ALIAS'", "'AS'", "'='", "'!='", 
                     "'<='", "'<'", "'>='", "'>'", "'ASC'", "'DESC'", "'OFFSET'", 
                     "'FIRST'", "'LAST'", "'NULLS'", "'NULL'", "'TRUE'", 
                     "'FALSE'", "'?'" ]

    symbolicNames = [ "<INVALID>", "S_COL", "DOT", "OPEN_PAR", "CLOSE_PAR", 
                      "BRACKET_L", "BRACKET_R", "DBL_COL", "COMMA", "FIND", 
                      "WHERE", "OR", "AND", "NOT", "LIMIT", "BY", "IN", 
                      "ORDER", "GROUP", "USING", "DEFINE", "ALIAS", "AS", 
                      "EQ", "NEQ", "LTE", "LT", "GTE", "GT", "ASC", "DESC", 
                      "OFFSET", "FIRST", "LAST", "NULLS", "NULL", "TRUE", 
                      "FALSE", "VAR_PREFIX", "IDENTIFIER", "INT_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "SINGLE_LINE_COMMENT", 
                      "MULTILINE_COMMENT", "WHITESPACE" ]

    RULE_prog = 0
    RULE_drolta_stmt_list = 1
    RULE_drolta_stmt = 2
    RULE_declare_alias_stmt = 3
    RULE_declare_rule_stmt = 4
    RULE_define_clause = 5
    RULE_result_var_list = 6
    RULE_query_stmt = 7
    RULE_find_clause = 8
    RULE_result_var = 9
    RULE_variable_alias = 10
    RULE_where_clause = 11
    RULE_order_by_clause = 12
    RULE_ordering_term_list = 13
    RULE_ordering_term = 14
    RULE_group_by_clause = 15
    RULE_variable_list = 16
    RULE_limit_clause = 17
    RULE_where_stmt = 18
    RULE_filter_stmt = 19
    RULE_atom_list = 20
    RULE_comparison_operator = 21
    RULE_predicate_neg_stmt = 22
    RULE_predicate_stmt = 23
    RULE_positional_param_list = 24
    RULE_named_param_list = 25
    RULE_named_param = 26
    RULE_atom = 27
    RULE_variable = 28

    ruleNames =  [ "prog", "drolta_stmt_list", "drolta_stmt", "declare_alias_stmt", 
                   "declare_rule_stmt", "define_clause", "result_var_list", 
                   "query_stmt", "find_clause", "result_var", "variable_alias", 
                   "where_clause", "order_by_clause", "ordering_term_list", 
                   "ordering_term", "group_by_clause", "variable_list", 
                   "limit_clause", "where_stmt", "filter_stmt", "atom_list", 
                   "comparison_operator", "predicate_neg_stmt", "predicate_stmt", 
                   "positional_param_list", "named_param_list", "named_param", 
                   "atom", "variable" ]

    EOF = Token.EOF
    S_COL=1
    DOT=2
    OPEN_PAR=3
    CLOSE_PAR=4
    BRACKET_L=5
    BRACKET_R=6
    DBL_COL=7
    COMMA=8
    FIND=9
    WHERE=10
    OR=11
    AND=12
    NOT=13
    LIMIT=14
    BY=15
    IN=16
    ORDER=17
    GROUP=18
    USING=19
    DEFINE=20
    ALIAS=21
    AS=22
    EQ=23
    NEQ=24
    LTE=25
    LT=26
    GTE=27
    GT=28
    ASC=29
    DESC=30
    OFFSET=31
    FIRST=32
    LAST=33
    NULLS=34
    NULL=35
    TRUE=36
    FALSE=37
    VAR_PREFIX=38
    IDENTIFIER=39
    INT_LITERAL=40
    FLOAT_LITERAL=41
    STRING_LITERAL=42
    SINGLE_LINE_COMMENT=43
    MULTILINE_COMMENT=44
    WHITESPACE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def drolta_stmt_list(self):
            return self.getTypedRuleContext(DroltaParser.Drolta_stmt_listContext,0)


        def EOF(self):
            return self.getToken(DroltaParser.EOF, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = DroltaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.drolta_stmt_list()
            self.state = 59
            self.match(DroltaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Drolta_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def drolta_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Drolta_stmtContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Drolta_stmtContext,i)


        def S_COL(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.S_COL)
            else:
                return self.getToken(DroltaParser.S_COL, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_drolta_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrolta_stmt_list" ):
                return visitor.visitDrolta_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def drolta_stmt_list(self):

        localctx = DroltaParser.Drolta_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_drolta_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.drolta_stmt()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 62
                self.match(DroltaParser.S_COL)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3146240) != 0):
                    self.state = 63
                    self.drolta_stmt()


                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Drolta_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_alias_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Declare_alias_stmtContext,0)


        def declare_rule_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Declare_rule_stmtContext,0)


        def query_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Query_stmtContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_drolta_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrolta_stmt" ):
                return visitor.visitDrolta_stmt(self)
            else:
                return visitor.visitChildren(self)




    def drolta_stmt(self):

        localctx = DroltaParser.Drolta_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_drolta_stmt)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.declare_alias_stmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.declare_rule_stmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.query_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_alias_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.original = None # Token
            self.alias = None # Token

        def ALIAS(self):
            return self.getToken(DroltaParser.ALIAS, 0)

        def AS(self):
            return self.getToken(DroltaParser.AS, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.IDENTIFIER)
            else:
                return self.getToken(DroltaParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_declare_alias_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_alias_stmt" ):
                return visitor.visitDeclare_alias_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declare_alias_stmt(self):

        localctx = DroltaParser.Declare_alias_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declare_alias_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(DroltaParser.ALIAS)
            self.state = 77
            localctx.original = self.match(DroltaParser.IDENTIFIER)
            self.state = 78
            self.match(DroltaParser.AS)
            self.state = 79
            localctx.alias = self.match(DroltaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_rule_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_clause(self):
            return self.getTypedRuleContext(DroltaParser.Define_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(DroltaParser.Where_clauseContext,0)


        def group_by_clause(self):
            return self.getTypedRuleContext(DroltaParser.Group_by_clauseContext,0)


        def order_by_clause(self):
            return self.getTypedRuleContext(DroltaParser.Order_by_clauseContext,0)


        def limit_clause(self):
            return self.getTypedRuleContext(DroltaParser.Limit_clauseContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_declare_rule_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_rule_stmt" ):
                return visitor.visitDeclare_rule_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declare_rule_stmt(self):

        localctx = DroltaParser.Declare_rule_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare_rule_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.define_clause()
            self.state = 82
            self.where_clause()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 83
                self.group_by_clause()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 86
                self.order_by_clause()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 89
                self.limit_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ruleName = None # Token

        def DEFINE(self):
            return self.getToken(DroltaParser.DEFINE, 0)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def result_var_list(self):
            return self.getTypedRuleContext(DroltaParser.Result_var_listContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_define_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_clause" ):
                return visitor.visitDefine_clause(self)
            else:
                return visitor.visitChildren(self)




    def define_clause(self):

        localctx = DroltaParser.Define_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_define_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(DroltaParser.DEFINE)
            self.state = 93
            localctx.ruleName = self.match(DroltaParser.IDENTIFIER)
            self.state = 94
            self.match(DroltaParser.OPEN_PAR)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==39:
                self.state = 95
                self.result_var_list()


            self.state = 98
            self.match(DroltaParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Result_var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def result_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Result_varContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Result_varContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_result_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult_var_list" ):
                return visitor.visitResult_var_list(self)
            else:
                return visitor.visitChildren(self)




    def result_var_list(self):

        localctx = DroltaParser.Result_var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_result_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.result_var()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 101
                self.match(DroltaParser.COMMA)
                self.state = 102
                self.result_var()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def find_clause(self):
            return self.getTypedRuleContext(DroltaParser.Find_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(DroltaParser.Where_clauseContext,0)


        def group_by_clause(self):
            return self.getTypedRuleContext(DroltaParser.Group_by_clauseContext,0)


        def order_by_clause(self):
            return self.getTypedRuleContext(DroltaParser.Order_by_clauseContext,0)


        def limit_clause(self):
            return self.getTypedRuleContext(DroltaParser.Limit_clauseContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_query_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_stmt" ):
                return visitor.visitQuery_stmt(self)
            else:
                return visitor.visitChildren(self)




    def query_stmt(self):

        localctx = DroltaParser.Query_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_query_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.find_clause()
            self.state = 109
            self.where_clause()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 110
                self.group_by_clause()


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 113
                self.order_by_clause()


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 116
                self.limit_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Find_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIND(self):
            return self.getToken(DroltaParser.FIND, 0)

        def result_var_list(self):
            return self.getTypedRuleContext(DroltaParser.Result_var_listContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_find_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFind_clause" ):
                return visitor.visitFind_clause(self)
            else:
                return visitor.visitChildren(self)




    def find_clause(self):

        localctx = DroltaParser.Find_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_find_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(DroltaParser.FIND)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==39:
                self.state = 120
                self.result_var_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Result_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.aggregateName = None # Token

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)

        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)


        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def variable_alias(self):
            return self.getTypedRuleContext(DroltaParser.Variable_aliasContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_result_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult_var" ):
                return visitor.visitResult_var(self)
            else:
                return visitor.visitChildren(self)




    def result_var(self):

        localctx = DroltaParser.Result_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_result_var)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                localctx.aggregateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 124
                self.match(DroltaParser.OPEN_PAR)
                self.state = 125
                self.variable()
                self.state = 126
                self.match(DroltaParser.CLOSE_PAR)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 127
                    self.variable_alias()


                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.variable()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22:
                    self.state = 131
                    self.variable_alias()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_aliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.alias = None # Token

        def AS(self):
            return self.getToken(DroltaParser.AS, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_variable_alias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_alias" ):
                return visitor.visitVariable_alias(self)
            else:
                return visitor.visitChildren(self)




    def variable_alias(self):

        localctx = DroltaParser.Variable_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(DroltaParser.AS)
            self.state = 137
            localctx.alias = self.match(DroltaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(DroltaParser.WHERE, 0)

        def where_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Where_stmtContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Where_stmtContext,i)


        def getRuleIndex(self):
            return DroltaParser.RULE_where_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_clause" ):
                return visitor.visitWhere_clause(self)
            else:
                return visitor.visitChildren(self)




    def where_clause(self):

        localctx = DroltaParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_where_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(DroltaParser.WHERE)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.where_stmt()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 549755822088) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_by_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(DroltaParser.ORDER, 0)

        def BY(self):
            return self.getToken(DroltaParser.BY, 0)

        def ordering_term_list(self):
            return self.getTypedRuleContext(DroltaParser.Ordering_term_listContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_order_by_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrder_by_clause" ):
                return visitor.visitOrder_by_clause(self)
            else:
                return visitor.visitChildren(self)




    def order_by_clause(self):

        localctx = DroltaParser.Order_by_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_order_by_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(DroltaParser.ORDER)
            self.state = 146
            self.match(DroltaParser.BY)
            self.state = 147
            self.ordering_term_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ordering_term_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ordering_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Ordering_termContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Ordering_termContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_ordering_term_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrdering_term_list" ):
                return visitor.visitOrdering_term_list(self)
            else:
                return visitor.visitChildren(self)




    def ordering_term_list(self):

        localctx = DroltaParser.Ordering_term_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ordering_term_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.ordering_term()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 150
                self.match(DroltaParser.COMMA)
                self.state = 151
                self.ordering_term()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ordering_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)


        def NULLS(self):
            return self.getToken(DroltaParser.NULLS, 0)

        def ASC(self):
            return self.getToken(DroltaParser.ASC, 0)

        def DESC(self):
            return self.getToken(DroltaParser.DESC, 0)

        def FIRST(self):
            return self.getToken(DroltaParser.FIRST, 0)

        def LAST(self):
            return self.getToken(DroltaParser.LAST, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_ordering_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrdering_term" ):
                return visitor.visitOrdering_term(self)
            else:
                return visitor.visitChildren(self)




    def ordering_term(self):

        localctx = DroltaParser.Ordering_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ordering_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.variable()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 161
                self.match(DroltaParser.NULLS)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_by_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(DroltaParser.GROUP, 0)

        def BY(self):
            return self.getToken(DroltaParser.BY, 0)

        def variable_list(self):
            return self.getTypedRuleContext(DroltaParser.Variable_listContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_group_by_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup_by_clause" ):
                return visitor.visitGroup_by_clause(self)
            else:
                return visitor.visitChildren(self)




    def group_by_clause(self):

        localctx = DroltaParser.Group_by_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_group_by_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(DroltaParser.GROUP)
            self.state = 166
            self.match(DroltaParser.BY)
            self.state = 167
            self.variable_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.VariableContext)
            else:
                return self.getTypedRuleContext(DroltaParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = DroltaParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.variable()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 170
                self.match(DroltaParser.COMMA)
                self.state = 171
                self.variable()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.limitVal = None # Token
            self.offsetVal = None # Token

        def LIMIT(self):
            return self.getToken(DroltaParser.LIMIT, 0)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.INT_LITERAL)
            else:
                return self.getToken(DroltaParser.INT_LITERAL, i)

        def OFFSET(self):
            return self.getToken(DroltaParser.OFFSET, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_limit_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit_clause" ):
                return visitor.visitLimit_clause(self)
            else:
                return visitor.visitChildren(self)




    def limit_clause(self):

        localctx = DroltaParser.Limit_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_limit_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(DroltaParser.LIMIT)
            self.state = 178
            localctx.limitVal = self.match(DroltaParser.INT_LITERAL)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 179
                self.match(DroltaParser.OFFSET)
                self.state = 180
                localctx.offsetVal = self.match(DroltaParser.INT_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filter_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Filter_stmtContext,0)


        def predicate_neg_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Predicate_neg_stmtContext,0)


        def predicate_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Predicate_stmtContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_where_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_stmt" ):
                return visitor.visitWhere_stmt(self)
            else:
                return visitor.visitChildren(self)




    def where_stmt(self):

        localctx = DroltaParser.Where_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_where_stmt)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.filter_stmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.predicate_neg_stmt()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.predicate_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Filter_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DroltaParser.RULE_filter_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotFilterStmtContext(Filter_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def NOT(self):
            return self.getToken(DroltaParser.NOT, 0)
        def filter_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Filter_stmtContext,0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotFilterStmt" ):
                return visitor.visitNotFilterStmt(self)
            else:
                return visitor.visitChildren(self)


    class MembershipFilterStmtContext(Filter_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_stmtContext
            super().__init__(parser)
            self.left = None # VariableContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def IN(self):
            return self.getToken(DroltaParser.IN, 0)
        def atom_list(self):
            return self.getTypedRuleContext(DroltaParser.Atom_listContext,0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)

        def NOT(self):
            return self.getToken(DroltaParser.NOT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembershipFilterStmt" ):
                return visitor.visitMembershipFilterStmt(self)
            else:
                return visitor.visitChildren(self)


    class AndFilterStmtContext(Filter_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_stmtContext
            super().__init__(parser)
            self.left = None # Filter_stmtContext
            self.right = None # Filter_stmtContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def AND(self):
            return self.getToken(DroltaParser.AND, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def filter_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Filter_stmtContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Filter_stmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndFilterStmt" ):
                return visitor.visitAndFilterStmt(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonFilterStmtContext(Filter_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_stmtContext
            super().__init__(parser)
            self.left = None # VariableContext
            self.op = None # Comparison_operatorContext
            self.right = None # AtomContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)

        def comparison_operator(self):
            return self.getTypedRuleContext(DroltaParser.Comparison_operatorContext,0)

        def atom(self):
            return self.getTypedRuleContext(DroltaParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonFilterStmt" ):
                return visitor.visitComparisonFilterStmt(self)
            else:
                return visitor.visitChildren(self)


    class OrFilterStmtContext(Filter_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_stmtContext
            super().__init__(parser)
            self.left = None # Filter_stmtContext
            self.right = None # Filter_stmtContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def OR(self):
            return self.getToken(DroltaParser.OR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def filter_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Filter_stmtContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Filter_stmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrFilterStmt" ):
                return visitor.visitOrFilterStmt(self)
            else:
                return visitor.visitChildren(self)



    def filter_stmt(self):

        localctx = DroltaParser.Filter_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filter_stmt)
        self._la = 0 # Token type
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = DroltaParser.ComparisonFilterStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(DroltaParser.OPEN_PAR)
                self.state = 189
                localctx.left = self.variable()
                self.state = 190
                localctx.op = self.comparison_operator()
                self.state = 191
                localctx.right = self.atom()
                self.state = 192
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                localctx = DroltaParser.MembershipFilterStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(DroltaParser.OPEN_PAR)
                self.state = 195
                localctx.left = self.variable()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 196
                    self.match(DroltaParser.NOT)


                self.state = 199
                self.match(DroltaParser.IN)
                self.state = 200
                self.atom_list()
                self.state = 201
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                localctx = DroltaParser.AndFilterStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(DroltaParser.OPEN_PAR)
                self.state = 204
                localctx.left = self.filter_stmt()
                self.state = 205
                self.match(DroltaParser.AND)
                self.state = 206
                localctx.right = self.filter_stmt()
                self.state = 207
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 4:
                localctx = DroltaParser.OrFilterStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(DroltaParser.OPEN_PAR)
                self.state = 210
                localctx.left = self.filter_stmt()
                self.state = 211
                self.match(DroltaParser.OR)
                self.state = 212
                localctx.right = self.filter_stmt()
                self.state = 213
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 5:
                localctx = DroltaParser.NotFilterStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.match(DroltaParser.OPEN_PAR)
                self.state = 216
                self.match(DroltaParser.NOT)
                self.state = 217
                self.filter_stmt()
                self.state = 218
                self.match(DroltaParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_L(self):
            return self.getToken(DroltaParser.BRACKET_L, 0)

        def BRACKET_R(self):
            return self.getToken(DroltaParser.BRACKET_R, 0)

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.AtomContext)
            else:
                return self.getTypedRuleContext(DroltaParser.AtomContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_atom_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_list" ):
                return visitor.visitAtom_list(self)
            else:
                return visitor.visitChildren(self)




    def atom_list(self):

        localctx = DroltaParser.Atom_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atom_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(DroltaParser.BRACKET_L)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8211977469952) != 0):
                self.state = 223
                self.atom()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 224
                    self.match(DroltaParser.COMMA)
                    self.state = 225
                    self.atom()
                    self.state = 230
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 233
            self.match(DroltaParser.BRACKET_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(DroltaParser.GT, 0)

        def GTE(self):
            return self.getToken(DroltaParser.GTE, 0)

        def LT(self):
            return self.getToken(DroltaParser.LT, 0)

        def LTE(self):
            return self.getToken(DroltaParser.LTE, 0)

        def EQ(self):
            return self.getToken(DroltaParser.EQ, 0)

        def NEQ(self):
            return self.getToken(DroltaParser.NEQ, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_comparison_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_operator" ):
                return visitor.visitComparison_operator(self)
            else:
                return visitor.visitChildren(self)




    def comparison_operator(self):

        localctx = DroltaParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_neg_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(DroltaParser.NOT, 0)

        def predicate_stmt(self):
            return self.getTypedRuleContext(DroltaParser.Predicate_stmtContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_predicate_neg_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_neg_stmt" ):
                return visitor.visitPredicate_neg_stmt(self)
            else:
                return visitor.visitChildren(self)




    def predicate_neg_stmt(self):

        localctx = DroltaParser.Predicate_neg_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_predicate_neg_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(DroltaParser.NOT)
            self.state = 238
            self.predicate_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.PredicateName = None # Token

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)

        def positional_param_list(self):
            return self.getTypedRuleContext(DroltaParser.Positional_param_listContext,0)


        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def named_param_list(self):
            return self.getTypedRuleContext(DroltaParser.Named_param_listContext,0)


        def COMMA(self):
            return self.getToken(DroltaParser.COMMA, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_predicate_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_stmt" ):
                return visitor.visitPredicate_stmt(self)
            else:
                return visitor.visitChildren(self)




    def predicate_stmt(self):

        localctx = DroltaParser.Predicate_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_predicate_stmt)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                localctx.PredicateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 241
                self.match(DroltaParser.OPEN_PAR)
                self.state = 242
                self.positional_param_list()
                self.state = 243
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                localctx.PredicateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 246
                self.match(DroltaParser.OPEN_PAR)
                self.state = 247
                self.named_param_list()
                self.state = 248
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                localctx.PredicateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 251
                self.match(DroltaParser.OPEN_PAR)
                self.state = 252
                self.positional_param_list()
                self.state = 253
                self.match(DroltaParser.COMMA)
                self.state = 254
                self.named_param_list()
                self.state = 255
                self.match(DroltaParser.CLOSE_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Positional_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.AtomContext)
            else:
                return self.getTypedRuleContext(DroltaParser.AtomContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_positional_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositional_param_list" ):
                return visitor.visitPositional_param_list(self)
            else:
                return visitor.visitChildren(self)




    def positional_param_list(self):

        localctx = DroltaParser.Positional_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_positional_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.atom()
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.match(DroltaParser.COMMA)
                    self.state = 261
                    self.atom() 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def named_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Named_paramContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Named_paramContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_named_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_param_list" ):
                return visitor.visitNamed_param_list(self)
            else:
                return visitor.visitChildren(self)




    def named_param_list(self):

        localctx = DroltaParser.Named_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_named_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.named_param()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 268
                self.match(DroltaParser.COMMA)
                self.state = 269
                self.named_param()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(DroltaParser.EQ, 0)

        def atom(self):
            return self.getTypedRuleContext(DroltaParser.AtomContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_named_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_param" ):
                return visitor.visitNamed_param(self)
            else:
                return visitor.visitChildren(self)




    def named_param(self):

        localctx = DroltaParser.Named_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_named_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(DroltaParser.IDENTIFIER)
            self.state = 276
            self.match(DroltaParser.EQ)
            self.state = 277
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DroltaParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Int_literalContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(DroltaParser.INT_LITERAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_literal" ):
                return visitor.visitInt_literal(self)
            else:
                return visitor.visitChildren(self)


    class String_literalContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(DroltaParser.STRING_LITERAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)


    class Null_literalContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(DroltaParser.NULL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_literal" ):
                return visitor.visitNull_literal(self)
            else:
                return visitor.visitChildren(self)


    class Float_literalContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(DroltaParser.FLOAT_LITERAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_literal" ):
                return visitor.visitFloat_literal(self)
            else:
                return visitor.visitChildren(self)


    class Variable_atomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_atom" ):
                return visitor.visitVariable_atom(self)
            else:
                return visitor.visitChildren(self)


    class Bool_literalContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(DroltaParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(DroltaParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_literal" ):
                return visitor.visitBool_literal(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = DroltaParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                localctx = DroltaParser.Variable_atomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.variable()
                pass
            elif token in [40]:
                localctx = DroltaParser.Int_literalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(DroltaParser.INT_LITERAL)
                pass
            elif token in [41]:
                localctx = DroltaParser.Float_literalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(DroltaParser.FLOAT_LITERAL)
                pass
            elif token in [42]:
                localctx = DroltaParser.String_literalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(DroltaParser.STRING_LITERAL)
                pass
            elif token in [35]:
                localctx = DroltaParser.Null_literalContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.match(DroltaParser.NULL)
                pass
            elif token in [36, 37]:
                localctx = DroltaParser.Bool_literalContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_PREFIX(self):
            return self.getToken(DroltaParser.VAR_PREFIX, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = DroltaParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(DroltaParser.VAR_PREFIX)
            self.state = 288
            self.match(DroltaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





