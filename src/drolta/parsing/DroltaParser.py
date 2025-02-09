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
        4,1,39,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,5,
        0,42,8,0,10,0,12,0,45,9,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,3,1,
        55,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,71,8,4,10,4,12,4,74,9,4,3,4,76,8,4,1,4,1,4,1,5,1,5,1,5,5,5,83,
        8,5,10,5,12,5,86,9,5,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,
        3,6,97,8,6,1,7,1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,3,7,107,8,7,
        1,8,1,8,1,8,3,8,112,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,12,1,12,3,12,127,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,138,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,161,8,13,1,14,1,14,1,14,1,14,5,14,167,8,14,10,14,12,14,
        170,9,14,3,14,172,8,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,5,16,183,8,16,10,16,12,16,186,9,16,3,16,188,8,16,1,16,1,16,1,
        16,3,16,193,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,0,0,19,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,2,1,0,26,31,3,0,
        1,3,32,32,34,36,205,0,38,1,0,0,0,2,54,1,0,0,0,4,56,1,0,0,0,6,61,
        1,0,0,0,8,64,1,0,0,0,10,79,1,0,0,0,12,87,1,0,0,0,14,98,1,0,0,0,16,
        111,1,0,0,0,18,113,1,0,0,0,20,117,1,0,0,0,22,121,1,0,0,0,24,126,
        1,0,0,0,26,160,1,0,0,0,28,162,1,0,0,0,30,175,1,0,0,0,32,192,1,0,
        0,0,34,194,1,0,0,0,36,198,1,0,0,0,38,43,3,2,1,0,39,40,5,4,0,0,40,
        42,3,2,1,0,41,39,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,47,1,0,0,0,45,43,1,0,0,0,46,48,5,4,0,0,47,46,1,0,0,0,47,48,
        1,0,0,0,48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,55,3,4,2,0,52,
        55,3,6,3,0,53,55,3,10,5,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,
        0,0,55,3,1,0,0,0,56,57,5,24,0,0,57,58,5,33,0,0,58,59,5,25,0,0,59,
        60,5,33,0,0,60,5,1,0,0,0,61,62,3,8,4,0,62,63,3,14,7,0,63,7,1,0,0,
        0,64,65,5,23,0,0,65,66,5,33,0,0,66,75,5,6,0,0,67,72,5,32,0,0,68,
        69,5,11,0,0,69,71,5,32,0,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,
        0,0,72,73,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,75,67,1,0,0,0,75,76,
        1,0,0,0,76,77,1,0,0,0,77,78,5,7,0,0,78,9,1,0,0,0,79,80,3,12,6,0,
        80,84,3,14,7,0,81,83,3,16,8,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,
        1,0,0,0,84,85,1,0,0,0,85,11,1,0,0,0,86,84,1,0,0,0,87,96,5,12,0,0,
        88,93,5,32,0,0,89,90,5,11,0,0,90,92,5,32,0,0,91,89,1,0,0,0,92,95,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,
        96,88,1,0,0,0,96,97,1,0,0,0,97,13,1,0,0,0,98,106,5,13,0,0,99,103,
        3,24,12,0,100,102,3,24,12,0,101,100,1,0,0,0,102,105,1,0,0,0,103,
        101,1,0,0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,106,
        99,1,0,0,0,106,107,1,0,0,0,107,15,1,0,0,0,108,112,3,18,9,0,109,112,
        3,20,10,0,110,112,3,22,11,0,111,108,1,0,0,0,111,109,1,0,0,0,111,
        110,1,0,0,0,112,17,1,0,0,0,113,114,5,20,0,0,114,115,5,18,0,0,115,
        116,5,32,0,0,116,19,1,0,0,0,117,118,5,21,0,0,118,119,5,18,0,0,119,
        120,5,32,0,0,120,21,1,0,0,0,121,122,5,17,0,0,122,123,5,34,0,0,123,
        23,1,0,0,0,124,127,3,26,13,0,125,127,3,32,16,0,126,124,1,0,0,0,126,
        125,1,0,0,0,127,25,1,0,0,0,128,129,5,6,0,0,129,130,5,32,0,0,130,
        131,3,30,15,0,131,132,3,36,18,0,132,133,5,7,0,0,133,161,1,0,0,0,
        134,135,5,6,0,0,135,137,5,32,0,0,136,138,5,16,0,0,137,136,1,0,0,
        0,137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,19,0,0,140,141,3,28,
        14,0,141,142,5,7,0,0,142,161,1,0,0,0,143,144,5,6,0,0,144,145,3,26,
        13,0,145,146,5,15,0,0,146,147,3,26,13,0,147,148,5,7,0,0,148,161,
        1,0,0,0,149,150,5,6,0,0,150,151,3,26,13,0,151,152,5,14,0,0,152,153,
        3,26,13,0,153,154,5,7,0,0,154,161,1,0,0,0,155,156,5,6,0,0,156,157,
        5,16,0,0,157,158,3,26,13,0,158,159,5,7,0,0,159,161,1,0,0,0,160,128,
        1,0,0,0,160,134,1,0,0,0,160,143,1,0,0,0,160,149,1,0,0,0,160,155,
        1,0,0,0,161,27,1,0,0,0,162,171,5,8,0,0,163,168,3,36,18,0,164,165,
        5,11,0,0,165,167,3,36,18,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,163,
        1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,9,0,0,174,29,1,
        0,0,0,175,176,7,0,0,0,176,31,1,0,0,0,177,178,5,33,0,0,178,187,5,
        6,0,0,179,184,3,34,17,0,180,181,5,11,0,0,181,183,3,34,17,0,182,180,
        1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,188,
        1,0,0,0,186,184,1,0,0,0,187,179,1,0,0,0,187,188,1,0,0,0,188,189,
        1,0,0,0,189,193,5,7,0,0,190,191,5,16,0,0,191,193,3,32,16,0,192,177,
        1,0,0,0,192,190,1,0,0,0,193,33,1,0,0,0,194,195,5,33,0,0,195,196,
        5,26,0,0,196,197,3,36,18,0,197,35,1,0,0,0,198,199,7,1,0,0,199,37,
        1,0,0,0,19,43,47,54,72,75,84,93,96,103,106,111,126,137,160,168,171,
        184,187,192
    ]

class DroltaParser ( Parser ):

    grammarFileName = "Drolta.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'NULL'", "'TRUE'", "'FALSE'", "';'", 
                     "'.'", "'('", "')'", "'['", "']'", "'::'", "','", "'FIND'", 
                     "'WHERE'", "'OR'", "'AND'", "'NOT'", "'LIMIT'", "'BY'", 
                     "'IN'", "'ORDER'", "'GROUP'", "'USING'", "'DEFINE'", 
                     "'ALIAS'", "'AS'", "'='", "'!='", "'<='", "'<'", "'>='", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "S_COL", "DOT", "OPEN_PAR", "CLOSE_PAR", "BRACKET_L", 
                      "BRACKET_R", "DBL_COL", "COMMA", "FIND", "WHERE", 
                      "OR", "AND", "NOT", "LIMIT", "BY", "IN", "ORDER", 
                      "GROUP", "USING", "DEFINE", "ALIAS", "AS", "EQ", "NEQ", 
                      "LTE", "LT", "GTE", "GT", "VARIABLE", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "WHITESPACE" ]

    RULE_prog = 0
    RULE_prog_statement = 1
    RULE_alias_declaration = 2
    RULE_rule_declaration = 3
    RULE_define_clause = 4
    RULE_query = 5
    RULE_find_clause = 6
    RULE_where_clause = 7
    RULE_post_processing_statements = 8
    RULE_order_by_statement = 9
    RULE_group_by_statement = 10
    RULE_limit_statement = 11
    RULE_where_statement = 12
    RULE_filter_statement = 13
    RULE_atom_list = 14
    RULE_comparison_operator = 15
    RULE_predicate_statement = 16
    RULE_predicate_param = 17
    RULE_atom = 18

    ruleNames =  [ "prog", "prog_statement", "alias_declaration", "rule_declaration", 
                   "define_clause", "query", "find_clause", "where_clause", 
                   "post_processing_statements", "order_by_statement", "group_by_statement", 
                   "limit_statement", "where_statement", "filter_statement", 
                   "atom_list", "comparison_operator", "predicate_statement", 
                   "predicate_param", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    S_COL=4
    DOT=5
    OPEN_PAR=6
    CLOSE_PAR=7
    BRACKET_L=8
    BRACKET_R=9
    DBL_COL=10
    COMMA=11
    FIND=12
    WHERE=13
    OR=14
    AND=15
    NOT=16
    LIMIT=17
    BY=18
    IN=19
    ORDER=20
    GROUP=21
    USING=22
    DEFINE=23
    ALIAS=24
    AS=25
    EQ=26
    NEQ=27
    LTE=28
    LT=29
    GTE=30
    GT=31
    VARIABLE=32
    IDENTIFIER=33
    INT_LITERAL=34
    FLOAT_LITERAL=35
    STRING_LITERAL=36
    SINGLE_LINE_COMMENT=37
    MULTILINE_COMMENT=38
    WHITESPACE=39

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
            self.state = 38
            self.prog_statement()
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 39
                    self.match(DroltaParser.S_COL)
                    self.state = 40
                    self.prog_statement() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 46
                self.match(DroltaParser.S_COL)


            self.state = 49
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.alias_declaration()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.rule_declaration()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
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
            self.state = 56
            self.match(DroltaParser.ALIAS)
            self.state = 57
            localctx.original = self.match(DroltaParser.IDENTIFIER)
            self.state = 58
            self.match(DroltaParser.AS)
            self.state = 59
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
            self.state = 61
            self.define_clause()
            self.state = 62
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

        def DEFINE(self):
            return self.getToken(DroltaParser.DEFINE, 0)

        def IDENTIFIER(self):
            return self.getToken(DroltaParser.IDENTIFIER, 0)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.VARIABLE)
            else:
                return self.getToken(DroltaParser.VARIABLE, i)

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
            self.state = 64
            self.match(DroltaParser.DEFINE)
            self.state = 65
            self.match(DroltaParser.IDENTIFIER)
            self.state = 66
            self.match(DroltaParser.OPEN_PAR)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 67
                self.match(DroltaParser.VARIABLE)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 68
                    self.match(DroltaParser.COMMA)
                    self.state = 69
                    self.match(DroltaParser.VARIABLE)
                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 77
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


        def post_processing_statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DroltaParser.Post_processing_statementsContext)
            else:
                return self.getTypedRuleContext(DroltaParser.Post_processing_statementsContext,i)


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
            self.state = 79
            self.find_clause()
            self.state = 80
            self.where_clause()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3276800) != 0):
                self.state = 81
                self.post_processing_statements()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(DroltaParser.VARIABLE)
            else:
                return self.getToken(DroltaParser.VARIABLE, i)

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
            self.state = 87
            self.match(DroltaParser.FIND)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 88
                self.match(DroltaParser.VARIABLE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 89
                    self.match(DroltaParser.COMMA)
                    self.state = 90
                    self.match(DroltaParser.VARIABLE)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
        self.enterRule(localctx, 14, self.RULE_where_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DroltaParser.WHERE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590000192) != 0):
                self.state = 99
                self.where_statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590000192) != 0):
                    self.state = 100
                    self.where_statement()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_processing_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def order_by_statement(self):
            return self.getTypedRuleContext(DroltaParser.Order_by_statementContext,0)


        def group_by_statement(self):
            return self.getTypedRuleContext(DroltaParser.Group_by_statementContext,0)


        def limit_statement(self):
            return self.getTypedRuleContext(DroltaParser.Limit_statementContext,0)


        def getRuleIndex(self):
            return DroltaParser.RULE_post_processing_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPost_processing_statements" ):
                listener.enterPost_processing_statements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPost_processing_statements" ):
                listener.exitPost_processing_statements(self)




    def post_processing_statements(self):

        localctx = DroltaParser.Post_processing_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_post_processing_statements)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.order_by_statement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.group_by_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.limit_statement()
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


    class Order_by_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(DroltaParser.ORDER, 0)

        def BY(self):
            return self.getToken(DroltaParser.BY, 0)

        def VARIABLE(self):
            return self.getToken(DroltaParser.VARIABLE, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(DroltaParser.ORDER)
            self.state = 114
            self.match(DroltaParser.BY)
            self.state = 115
            self.match(DroltaParser.VARIABLE)
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

        def VARIABLE(self):
            return self.getToken(DroltaParser.VARIABLE, 0)

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
        self.enterRule(localctx, 20, self.RULE_group_by_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(DroltaParser.GROUP)
            self.state = 118
            self.match(DroltaParser.BY)
            self.state = 119
            self.match(DroltaParser.VARIABLE)
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

        def LIMIT(self):
            return self.getToken(DroltaParser.LIMIT, 0)

        def INT_LITERAL(self):
            return self.getToken(DroltaParser.INT_LITERAL, 0)

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
        self.enterRule(localctx, 22, self.RULE_limit_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(DroltaParser.LIMIT)
            self.state = 122
            self.match(DroltaParser.INT_LITERAL)
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
        self.enterRule(localctx, 24, self.RULE_where_statement)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.filter_statement()
                pass
            elif token in [16, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
            self.left = None # Token
            self.op = None # Comparison_operatorContext
            self.right = None # AtomContext
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def VARIABLE(self):
            return self.getToken(DroltaParser.VARIABLE, 0)
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
            self.left = None # Token
            self.copyFrom(ctx)

        def OPEN_PAR(self):
            return self.getToken(DroltaParser.OPEN_PAR, 0)
        def IN(self):
            return self.getToken(DroltaParser.IN, 0)
        def atom_list(self):
            return self.getTypedRuleContext(DroltaParser.Atom_listContext,0)

        def CLOSE_PAR(self):
            return self.getToken(DroltaParser.CLOSE_PAR, 0)
        def VARIABLE(self):
            return self.getToken(DroltaParser.VARIABLE, 0)
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
        self.enterRule(localctx, 26, self.RULE_filter_statement)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = DroltaParser.ComparisonFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(DroltaParser.OPEN_PAR)
                self.state = 129
                localctx.left = self.match(DroltaParser.VARIABLE)
                self.state = 130
                localctx.op = self.comparison_operator()
                self.state = 131
                localctx.right = self.atom()
                self.state = 132
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 2:
                localctx = DroltaParser.InFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(DroltaParser.OPEN_PAR)
                self.state = 135
                localctx.left = self.match(DroltaParser.VARIABLE)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 136
                    self.match(DroltaParser.NOT)


                self.state = 139
                self.match(DroltaParser.IN)
                self.state = 140
                self.atom_list()
                self.state = 141
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 3:
                localctx = DroltaParser.AndFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(DroltaParser.OPEN_PAR)
                self.state = 144
                localctx.left = self.filter_statement()
                self.state = 145
                self.match(DroltaParser.AND)
                self.state = 146
                localctx.right = self.filter_statement()
                self.state = 147
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 4:
                localctx = DroltaParser.OrFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(DroltaParser.OPEN_PAR)
                self.state = 150
                localctx.left = self.filter_statement()
                self.state = 151
                self.match(DroltaParser.OR)
                self.state = 152
                localctx.right = self.filter_statement()
                self.state = 153
                self.match(DroltaParser.CLOSE_PAR)
                pass

            elif la_ == 5:
                localctx = DroltaParser.NotFilterContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(DroltaParser.OPEN_PAR)
                self.state = 156
                self.match(DroltaParser.NOT)
                self.state = 157
                self.filter_statement()
                self.state = 158
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
        self.enterRule(localctx, 28, self.RULE_atom_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(DroltaParser.BRACKET_L)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 124554051598) != 0):
                self.state = 163
                self.atom()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 164
                    self.match(DroltaParser.COMMA)
                    self.state = 165
                    self.atom()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 173
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
        self.enterRule(localctx, 30, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_predicate_statement)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = DroltaParser.PredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                localctx.PredicateName = self.match(DroltaParser.IDENTIFIER)
                self.state = 178
                self.match(DroltaParser.OPEN_PAR)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 179
                    self.predicate_param()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==11:
                        self.state = 180
                        self.match(DroltaParser.COMMA)
                        self.state = 181
                        self.predicate_param()
                        self.state = 186
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 189
                self.match(DroltaParser.CLOSE_PAR)
                pass
            elif token in [16]:
                localctx = DroltaParser.PredicateNotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(DroltaParser.NOT)
                self.state = 191
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
        self.enterRule(localctx, 34, self.RULE_predicate_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(DroltaParser.IDENTIFIER)
            self.state = 195
            self.match(DroltaParser.EQ)
            self.state = 196
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

        def VARIABLE(self):
            return self.getToken(DroltaParser.VARIABLE, 0)

        def INT_LITERAL(self):
            return self.getToken(DroltaParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(DroltaParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(DroltaParser.STRING_LITERAL, 0)

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
        self.enterRule(localctx, 36, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124554051598) != 0)):
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





