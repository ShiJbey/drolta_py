# Generated from ./Drolta.g4 by ANTLR 4.13.2
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
        4,1,45,251,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,3,0,52,8,0,1,0,
        1,0,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,3,4,80,8,4,1,4,1,4,
        1,5,1,5,1,5,3,5,87,8,5,1,5,3,5,90,8,5,1,5,3,5,93,8,5,1,6,1,6,1,6,
        1,6,5,6,99,8,6,10,6,12,6,102,9,6,3,6,104,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,112,8,7,1,7,1,7,1,7,3,7,117,8,7,3,7,119,8,7,1,8,1,8,1,8,
        5,8,124,8,8,10,8,12,8,127,9,8,3,8,129,8,8,1,9,1,9,1,9,1,9,1,9,5,
        9,136,8,9,10,9,12,9,139,9,9,1,10,1,10,3,10,143,8,10,1,10,1,10,3,
        10,147,8,10,1,11,1,11,1,11,1,11,1,11,5,11,154,8,11,10,11,12,11,157,
        9,11,1,12,1,12,1,12,1,12,3,12,163,8,12,1,13,1,13,3,13,167,8,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,178,8,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,201,8,14,1,15,1,15,1,15,1,
        15,5,15,207,8,15,10,15,12,15,210,9,15,3,15,212,8,15,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,223,8,17,10,17,12,17,226,9,
        17,3,17,228,8,17,1,17,1,17,1,17,3,17,233,8,17,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,246,8,19,1,20,1,20,1,20,
        1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,0,3,1,0,30,31,1,0,33,34,1,0,24,29,267,0,42,1,0,0,0,2,58,1,
        0,0,0,4,60,1,0,0,0,6,65,1,0,0,0,8,68,1,0,0,0,10,83,1,0,0,0,12,94,
        1,0,0,0,14,118,1,0,0,0,16,120,1,0,0,0,18,130,1,0,0,0,20,140,1,0,
        0,0,22,148,1,0,0,0,24,158,1,0,0,0,26,166,1,0,0,0,28,200,1,0,0,0,
        30,202,1,0,0,0,32,215,1,0,0,0,34,232,1,0,0,0,36,234,1,0,0,0,38,245,
        1,0,0,0,40,247,1,0,0,0,42,47,3,2,1,0,43,44,5,2,0,0,44,46,3,2,1,0,
        45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,51,1,
        0,0,0,49,47,1,0,0,0,50,52,5,2,0,0,51,50,1,0,0,0,51,52,1,0,0,0,52,
        53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,59,3,4,2,0,56,59,3,6,3,
        0,57,59,3,10,5,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,
        1,0,0,0,60,61,5,22,0,0,61,62,5,39,0,0,62,63,5,23,0,0,63,64,5,39,
        0,0,64,5,1,0,0,0,65,66,3,8,4,0,66,67,3,16,8,0,67,7,1,0,0,0,68,69,
        5,21,0,0,69,70,5,39,0,0,70,79,5,4,0,0,71,76,3,14,7,0,72,73,5,9,0,
        0,73,75,3,14,7,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,79,71,1,0,0,0,79,80,1,0,0,0,
        80,81,1,0,0,0,81,82,5,5,0,0,82,9,1,0,0,0,83,84,3,12,6,0,84,86,3,
        16,8,0,85,87,3,22,11,0,86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,
        88,90,3,18,9,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,3,
        24,12,0,92,91,1,0,0,0,92,93,1,0,0,0,93,11,1,0,0,0,94,103,5,10,0,
        0,95,100,3,14,7,0,96,97,5,9,0,0,97,99,3,14,7,0,98,96,1,0,0,0,99,
        102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,104,1,0,0,0,102,100,
        1,0,0,0,103,95,1,0,0,0,103,104,1,0,0,0,104,13,1,0,0,0,105,106,5,
        39,0,0,106,107,5,4,0,0,107,108,3,40,20,0,108,111,5,5,0,0,109,110,
        5,23,0,0,110,112,5,39,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,119,
        1,0,0,0,113,116,3,40,20,0,114,115,5,23,0,0,115,117,5,39,0,0,116,
        114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,105,1,0,0,0,118,
        113,1,0,0,0,119,15,1,0,0,0,120,128,5,11,0,0,121,125,3,26,13,0,122,
        124,3,26,13,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,
        126,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,121,1,0,0,0,128,
        129,1,0,0,0,129,17,1,0,0,0,130,131,5,18,0,0,131,132,5,16,0,0,132,
        137,3,20,10,0,133,134,5,9,0,0,134,136,3,20,10,0,135,133,1,0,0,0,
        136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,19,1,0,0,0,139,
        137,1,0,0,0,140,142,3,40,20,0,141,143,7,0,0,0,142,141,1,0,0,0,142,
        143,1,0,0,0,143,146,1,0,0,0,144,145,5,35,0,0,145,147,7,1,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,21,1,0,0,0,148,149,5,19,0,0,149,
        150,5,16,0,0,150,155,3,40,20,0,151,152,5,9,0,0,152,154,3,40,20,0,
        153,151,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,
        156,23,1,0,0,0,157,155,1,0,0,0,158,159,5,15,0,0,159,162,5,40,0,0,
        160,161,5,32,0,0,161,163,5,40,0,0,162,160,1,0,0,0,162,163,1,0,0,
        0,163,25,1,0,0,0,164,167,3,28,14,0,165,167,3,34,17,0,166,164,1,0,
        0,0,166,165,1,0,0,0,167,27,1,0,0,0,168,169,5,4,0,0,169,170,3,40,
        20,0,170,171,3,32,16,0,171,172,3,38,19,0,172,173,5,5,0,0,173,201,
        1,0,0,0,174,175,5,4,0,0,175,177,3,40,20,0,176,178,5,14,0,0,177,176,
        1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,17,0,0,180,181,
        3,30,15,0,181,182,5,5,0,0,182,201,1,0,0,0,183,184,5,4,0,0,184,185,
        3,28,14,0,185,186,5,13,0,0,186,187,3,28,14,0,187,188,5,5,0,0,188,
        201,1,0,0,0,189,190,5,4,0,0,190,191,3,28,14,0,191,192,5,12,0,0,192,
        193,3,28,14,0,193,194,5,5,0,0,194,201,1,0,0,0,195,196,5,4,0,0,196,
        197,5,14,0,0,197,198,3,28,14,0,198,199,5,5,0,0,199,201,1,0,0,0,200,
        168,1,0,0,0,200,174,1,0,0,0,200,183,1,0,0,0,200,189,1,0,0,0,200,
        195,1,0,0,0,201,29,1,0,0,0,202,211,5,6,0,0,203,208,3,38,19,0,204,
        205,5,9,0,0,205,207,3,38,19,0,206,204,1,0,0,0,207,210,1,0,0,0,208,
        206,1,0,0,0,208,209,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,211,
        203,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,7,0,0,214,
        31,1,0,0,0,215,216,7,2,0,0,216,33,1,0,0,0,217,218,5,39,0,0,218,227,
        5,4,0,0,219,224,3,36,18,0,220,221,5,9,0,0,221,223,3,36,18,0,222,
        220,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        228,1,0,0,0,226,224,1,0,0,0,227,219,1,0,0,0,227,228,1,0,0,0,228,
        229,1,0,0,0,229,233,5,5,0,0,230,231,5,14,0,0,231,233,3,34,17,0,232,
        217,1,0,0,0,232,230,1,0,0,0,233,35,1,0,0,0,234,235,5,39,0,0,235,
        236,5,24,0,0,236,237,3,38,19,0,237,37,1,0,0,0,238,246,3,40,20,0,
        239,246,5,40,0,0,240,246,5,41,0,0,241,246,5,42,0,0,242,246,5,36,
        0,0,243,246,5,37,0,0,244,246,5,38,0,0,245,238,1,0,0,0,245,239,1,
        0,0,0,245,240,1,0,0,0,245,241,1,0,0,0,245,242,1,0,0,0,245,243,1,
        0,0,0,245,244,1,0,0,0,246,39,1,0,0,0,247,248,5,1,0,0,248,249,5,39,
        0,0,249,41,1,0,0,0,29,47,51,58,76,79,86,89,92,100,103,111,116,118,
        125,128,137,142,146,155,162,166,177,200,208,211,224,227,232,245
    ]

class DroltaParser ( Parser ):

    grammarFileName = "Drolta.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "';'", "'.'", "'('", "')'", "'['", 
                     "']'", "'::'", "','", "'FIND'", "'WHERE'", "'OR'", 
                     "'AND'", "'NOT'", "'LIMIT'", "'BY'", "'IN'", "'ORDER'", 
                     "'GROUP'", "'USING'", "'DEFINE'", "'ALIAS'", "'AS'", 
                     "'='", "'!='", "'<='", "'<'", "'>='", "'>'", "'ASC'", 
                     "'DESC'", "'OFFSET'", "'FIRST'", "'LAST'", "'NULLS'", 
                     "'NULL'", "'TRUE'", "'FALSE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "S_COL", "DOT", "OPEN_PAR", 
                      "CLOSE_PAR", "BRACKET_L", "BRACKET_R", "DBL_COL", 
                      "COMMA", "FIND", "WHERE", "OR", "AND", "NOT", "LIMIT", 
                      "BY", "IN", "ORDER", "GROUP", "USING", "DEFINE", "ALIAS", 
                      "AS", "EQ", "NEQ", "LTE", "LT", "GTE", "GT", "ASC", 
                      "DESC", "OFFSET", "FIRST", "LAST", "NULLS", "NULL", 
                      "TRUE", "FALSE", "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", 
                      "WHITESPACE" ]

    RULE_prog = 0
    RULE_prog_statement = 1
    RULE_alias_declaration = 2
    RULE_rule_declaration = 3
    RULE_define_clause = 4
    RULE_query = 5
    RULE_find_clause = 6
    RULE_result_var = 7
    RULE_where_clause = 8
    RULE_order_by_statement = 9
    RULE_ordering_term = 10
    RULE_group_by_statement = 11
    RULE_limit_statement = 12
    RULE_where_statement = 13
    RULE_filter_statement = 14
    RULE_atom_list = 15
    RULE_comparison_operator = 16
    RULE_predicate_statement = 17
    RULE_predicate_param = 18
    RULE_atom = 19
    RULE_variable = 20

    ruleNames =  [ "prog", "prog_statement", "alias_declaration", "rule_declaration", 
                   "define_clause", "query", "find_clause", "result_var", 
                   "where_clause", "order_by_statement", "ordering_term", 
                   "group_by_statement", "limit_statement", "where_statement", 
                   "filter_statement", "atom_list", "comparison_operator", 
                   "predicate_statement", "predicate_param", "atom", "variable" ]

    EOF = Token.EOF
    T__0=1
    S_COL=2
    DOT=3
    OPEN_PAR=4
    CLOSE_PAR=5
    BRACKET_L=6
    BRACKET_R=7
    DBL_COL=8
    COMMA=9
    FIND=10
    WHERE=11
    OR=12
    AND=13
    NOT=14
    LIMIT=15
    BY=16
    IN=17
    ORDER=18
    GROUP=19
    USING=20
    DEFINE=21
    ALIAS=22
    AS=23
    EQ=24
    NEQ=25
    LTE=26
    LT=27
    GTE=28
    GT=29
    ASC=30
    DESC=31
    OFFSET=32
    FIRST=33
    LAST=34
    NULLS=35
    NULL=36
    TRUE=37
    FALSE=38
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

        def prog_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Prog_statementContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Prog_statementContext,i)


        def EOF(self):
            return self.getToken(DroltaParser.EOF, 0)

        def S_COL(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.S_COL)
            else:
                return self.getToken(DroltaParser.S_COL, i)

        def getRuleIndex(self):
            return DroltaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = DroltaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.prog_statement()
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 43
                    self.match(DroltaParser.S_COL)
                    self.state = 44
                    self.prog_statement() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 50
                self.match(DroltaParser.S_COL)


            self.state = 53
            self.match(DroltaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prog_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alias_declaration(self):
            return self.getTypedRuleContext(DroltaParser.Alias_declarationContext,0)


        def rule_declaration(self):
            return self.getTypedRuleContext(DroltaParser.Rule_declarationContext,0)


        def query(self):
            return self.getTypedRuleContext(DroltaParser.QueryContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_prog_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg_statement" ):
                listener.enterProg_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg_statement" ):
                listener.exitProg_statement(self)




    def prog_statement(self):

        localctx = DroltaParser.Prog_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.alias_declaration()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.rule_declaration()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.query()
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


    class Alias_declarationContext(ParserRuleContext):
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
            return DroltaParser.RULE_alias_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlias_declaration" ):
                listener.enterAlias_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlias_declaration" ):
                listener.exitAlias_declaration(self)




    def alias_declaration(self):

        localctx = DroltaParser.Alias_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_alias_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(DroltaParser.ALIAS)
            self.state = 61
            localctx.original = self.match(DroltaParser.IDENTIFIER)
            self.state = 62
            self.match(DroltaParser.AS)
            self.state = 63
            localctx.alias = self.match(DroltaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_clause(self):
            return self.getTypedRuleContext(DroltaParser.Define_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(DroltaParser.Where_clauseContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_rule_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_declaration" ):
                listener.enterRule_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_declaration" ):
                listener.exitRule_declaration(self)




    def rule_declaration(self):

        localctx = DroltaParser.Rule_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.define_clause()
            self.state = 66
            self.where_clause()
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
            return DroltaParser.RULE_define_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_clause" ):
                listener.enterDefine_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_clause" ):
                listener.exitDefine_clause(self)




    def define_clause(self):

        localctx = DroltaParser.Define_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_define_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(DroltaParser.DEFINE)
            self.state = 69
            localctx.ruleName = self.match(DroltaParser.IDENTIFIER)
            self.state = 70
            self.match(DroltaParser.OPEN_PAR)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==39:
                self.state = 71
                self.result_var()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 72
                    self.match(DroltaParser.COMMA)
                    self.state = 73
                    self.result_var()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 81
            self.match(DroltaParser.CLOSE_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def find_clause(self):
            return self.getTypedRuleContext(DroltaParser.Find_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(DroltaParser.Where_clauseContext,0)


        def group_by_statement(self):
            return self.getTypedRuleContext(DroltaParser.Group_by_statementContext,0)


        def order_by_statement(self):
            return self.getTypedRuleContext(DroltaParser.Order_by_statementContext,0)


        def limit_statement(self):
            return self.getTypedRuleContext(DroltaParser.Limit_statementContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = DroltaParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.find_clause()
            self.state = 84
            self.where_clause()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 85
                self.group_by_statement()


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 88
                self.order_by_statement()


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 91
                self.limit_statement()


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
            return DroltaParser.RULE_find_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFind_clause" ):
                listener.enterFind_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFind_clause" ):
                listener.exitFind_clause(self)




    def find_clause(self):

        localctx = DroltaParser.Find_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_find_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(DroltaParser.FIND)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==39:
                self.state = 95
                self.result_var()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 96
                    self.match(DroltaParser.COMMA)
                    self.state = 97
                    self.result_var()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
            self.alias = None # Token

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)

        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)


        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.IDENTIFIER)
            else:
                return self.getToken(DroltaParser.IDENTIFIER, i)

        def AS(self):
            return self.getToken(DroltaParser.AS, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_result_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult_var" ):
                listener.enterResult_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult_var" ):
                listener.exitResult_var(self)




    def result_var(self):

        localctx = DroltaParser.Result_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_result_var)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                localctx.aggregateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 106
                self.match(DroltaParser.OPEN_PAR)
                self.state = 107
                self.variable()
                self.state = 108
                self.match(DroltaParser.CLOSE_PAR)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 109
                    self.match(DroltaParser.AS)
                    self.state = 110
                    localctx.alias = self.match(DroltaParser.IDENTIFIER)


                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.variable()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 114
                    self.match(DroltaParser.AS)
                    self.state = 115
                    localctx.alias = self.match(DroltaParser.IDENTIFIER)


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


    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(DroltaParser.WHERE, 0)

        def where_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Where_statementContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Where_statementContext,i)


        def getRuleIndex(self):
            return DroltaParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = DroltaParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(DroltaParser.WHERE)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 549755830288) != 0):
                self.state = 121
                self.where_statement()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 549755830288) != 0):
                    self.state = 122
                    self.where_statement()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_by_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(DroltaParser.ORDER, 0)

        def BY(self):
            return self.getToken(DroltaParser.BY, 0)

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
            return DroltaParser.RULE_order_by_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_by_statement" ):
                listener.enterOrder_by_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_by_statement" ):
                listener.exitOrder_by_statement(self)




    def order_by_statement(self):

        localctx = DroltaParser.Order_by_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_order_by_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DroltaParser.ORDER)
            self.state = 131
            self.match(DroltaParser.BY)
            self.state = 132
            self.ordering_term()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 133
                self.match(DroltaParser.COMMA)
                self.state = 134
                self.ordering_term()
                self.state = 139
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdering_term" ):
                listener.enterOrdering_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdering_term" ):
                listener.exitOrdering_term(self)




    def ordering_term(self):

        localctx = DroltaParser.Ordering_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ordering_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.variable()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30 or _la==31:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 144
                self.match(DroltaParser.NULLS)
                self.state = 145
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
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


    class Group_by_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(DroltaParser.GROUP, 0)

        def BY(self):
            return self.getToken(DroltaParser.BY, 0)

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
            return DroltaParser.RULE_group_by_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_statement" ):
                listener.enterGroup_by_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_statement" ):
                listener.exitGroup_by_statement(self)




    def group_by_statement(self):

        localctx = DroltaParser.Group_by_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_group_by_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(DroltaParser.GROUP)
            self.state = 149
            self.match(DroltaParser.BY)
            self.state = 150
            self.variable()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 151
                self.match(DroltaParser.COMMA)
                self.state = 152
                self.variable()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_statementContext(ParserRuleContext):
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
            return DroltaParser.RULE_limit_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_statement" ):
                listener.enterLimit_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_statement" ):
                listener.exitLimit_statement(self)




    def limit_statement(self):

        localctx = DroltaParser.Limit_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_limit_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(DroltaParser.LIMIT)
            self.state = 159
            localctx.limitVal = self.match(DroltaParser.INT_LITERAL)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 160
                self.match(DroltaParser.OFFSET)
                self.state = 161
                localctx.offsetVal = self.match(DroltaParser.INT_LITERAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filter_statement(self):
            return self.getTypedRuleContext(DroltaParser.Filter_statementContext,0)


        def predicate_statement(self):
            return self.getTypedRuleContext(DroltaParser.Predicate_statementContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_where_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_statement" ):
                listener.enterWhere_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_statement" ):
                listener.exitWhere_statement(self)




    def where_statement(self):

        localctx = DroltaParser.Where_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_where_statement)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.filter_statement()
                pass
            elif token in [14, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.predicate_statement()
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


    class Filter_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DroltaParser.RULE_filter_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AndFilterContext(Filter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_statementContext
            super().__init__(parser)
            self.left = None # Filter_statementContext
            self.right = None # Filter_statementContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def AND(self):
            return self.getToken(DroltaParser.AND, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def filter_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Filter_statementContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Filter_statementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndFilter" ):
                listener.enterAndFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndFilter" ):
                listener.exitAndFilter(self)


    class ComparisonFilterContext(Filter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_statementContext
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonFilter" ):
                listener.enterComparisonFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonFilter" ):
                listener.exitComparisonFilter(self)


    class NotFilterContext(Filter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def NOT(self):
            return self.getToken(DroltaParser.NOT, 0)
        def filter_statement(self):
            return self.getTypedRuleContext(DroltaParser.Filter_statementContext,0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotFilter" ):
                listener.enterNotFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotFilter" ):
                listener.exitNotFilter(self)


    class OrFilterContext(Filter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_statementContext
            super().__init__(parser)
            self.left = None # Filter_statementContext
            self.right = None # Filter_statementContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def OR(self):
            return self.getToken(DroltaParser.OR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def filter_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Filter_statementContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Filter_statementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrFilter" ):
                listener.enterOrFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrFilter" ):
                listener.exitOrFilter(self)


    class InFilterContext(Filter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Filter_statementContext
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInFilter" ):
                listener.enterInFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInFilter" ):
                listener.exitInFilter(self)



    def filter_statement(self):

        localctx = DroltaParser.Filter_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_filter_statement)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = DroltaParser.ComparisonFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(DroltaParser.OPEN_PAR)
                self.state = 169
                localctx.left = self.variable()
                self.state = 170
                localctx.op = self.comparison_operator()
                self.state = 171
                localctx.right = self.atom()
                self.state = 172
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                localctx = DroltaParser.InFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(DroltaParser.OPEN_PAR)
                self.state = 175
                localctx.left = self.variable()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 176
                    self.match(DroltaParser.NOT)


                self.state = 179
                self.match(DroltaParser.IN)
                self.state = 180
                self.atom_list()
                self.state = 181
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                localctx = DroltaParser.AndFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(DroltaParser.OPEN_PAR)
                self.state = 184
                localctx.left = self.filter_statement()
                self.state = 185
                self.match(DroltaParser.AND)
                self.state = 186
                localctx.right = self.filter_statement()
                self.state = 187
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 4:
                localctx = DroltaParser.OrFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(DroltaParser.OPEN_PAR)
                self.state = 190
                localctx.left = self.filter_statement()
                self.state = 191
                self.match(DroltaParser.OR)
                self.state = 192
                localctx.right = self.filter_statement()
                self.state = 193
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 5:
                localctx = DroltaParser.NotFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.match(DroltaParser.OPEN_PAR)
                self.state = 196
                self.match(DroltaParser.NOT)
                self.state = 197
                self.filter_statement()
                self.state = 198
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_list" ):
                listener.enterAtom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_list" ):
                listener.exitAtom_list(self)




    def atom_list(self):

        localctx = DroltaParser.Atom_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(DroltaParser.BRACKET_L)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8177617731586) != 0):
                self.state = 203
                self.atom()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 204
                    self.match(DroltaParser.COMMA)
                    self.state = 205
                    self.atom()
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 213
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)




    def comparison_operator(self):

        localctx = DroltaParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
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


    class Predicate_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DroltaParser.RULE_predicate_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PredicateNotContext(Predicate_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Predicate_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(DroltaParser.NOT, 0)
        def predicate_statement(self):
            return self.getTypedRuleContext(DroltaParser.Predicate_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateNot" ):
                listener.enterPredicateNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateNot" ):
                listener.exitPredicateNot(self)


    class PredicateContext(Predicate_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DroltaParser.Predicate_statementContext
            super().__init__(parser)
            self.PredicateName = None # Token
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)
        def predicate_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Predicate_paramContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Predicate_paramContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.COMMA)
            else:
                return self.getToken(DroltaParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)



    def predicate_statement(self):

        localctx = DroltaParser.Predicate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_predicate_statement)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                localctx = DroltaParser.PredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                localctx.PredicateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 218
                self.match(DroltaParser.OPEN_PAR)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 219
                    self.predicate_param()
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==9:
                        self.state = 220
                        self.match(DroltaParser.COMMA)
                        self.state = 221
                        self.predicate_param()
                        self.state = 226
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 229
                self.match(DroltaParser.CLOSE_PAR)
                pass
            elif token in [14]:
                localctx = DroltaParser.PredicateNotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(DroltaParser.NOT)
                self.state = 231
                self.predicate_statement()
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


    class Predicate_paramContext(ParserRuleContext):
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
            return DroltaParser.RULE_predicate_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate_param" ):
                listener.enterPredicate_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate_param" ):
                listener.exitPredicate_param(self)




    def predicate_param(self):

        localctx = DroltaParser.Predicate_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_predicate_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(DroltaParser.IDENTIFIER)
            self.state = 235
            self.match(DroltaParser.EQ)
            self.state = 236
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

        def variable(self):
            return self.getTypedRuleContext(DroltaParser.VariableContext,0)


        def INT_LITERAL(self):
            return self.getToken(DroltaParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(DroltaParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(DroltaParser.STRING_LITERAL, 0)

        def NULL(self):
            return self.getToken(DroltaParser.NULL, 0)

        def TRUE(self):
            return self.getToken(DroltaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(DroltaParser.FALSE, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = DroltaParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_atom)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.variable()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(DroltaParser.INT_LITERAL)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(DroltaParser.FLOAT_LITERAL)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.match(DroltaParser.STRING_LITERAL)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.match(DroltaParser.NULL)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.match(DroltaParser.TRUE)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 244
                self.match(DroltaParser.FALSE)
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

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DroltaParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = DroltaParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(DroltaParser.T__0)
            self.state = 248
            self.match(DroltaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





