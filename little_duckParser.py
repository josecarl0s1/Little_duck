# Generated from little_duck.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from Interventions import *

def serializedATN():
    return [
        4,1,35,283,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,93,8,1,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,112,
        8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        128,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,136,8,7,1,8,1,8,1,8,3,8,141,
        8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,152,8,10,1,11,
        1,11,1,11,1,11,3,11,158,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,3,13,169,8,13,1,14,1,14,1,14,1,14,1,14,3,14,176,8,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,17,1,17,1,17,3,17,197,8,17,1,18,1,18,1,19,1,19,1,
        19,1,20,1,20,1,20,1,20,3,20,208,8,20,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,226,8,
        24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,238,8,
        27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,247,8,29,1,30,1,30,1,
        30,1,30,3,30,253,8,30,1,31,1,31,3,31,257,8,31,1,32,1,32,1,32,1,32,
        1,32,3,32,264,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,3,34,276,8,34,1,35,1,35,1,35,3,35,281,8,35,1,35,0,0,36,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,0,5,1,0,8,9,1,0,32,33,1,0,22,24,
        1,0,26,27,1,0,28,29,269,0,72,1,0,0,0,2,92,1,0,0,0,4,94,1,0,0,0,6,
        101,1,0,0,0,8,111,1,0,0,0,10,113,1,0,0,0,12,127,1,0,0,0,14,135,1,
        0,0,0,16,140,1,0,0,0,18,142,1,0,0,0,20,151,1,0,0,0,22,157,1,0,0,
        0,24,159,1,0,0,0,26,168,1,0,0,0,28,175,1,0,0,0,30,177,1,0,0,0,32,
        185,1,0,0,0,34,196,1,0,0,0,36,198,1,0,0,0,38,200,1,0,0,0,40,207,
        1,0,0,0,42,209,1,0,0,0,44,211,1,0,0,0,46,217,1,0,0,0,48,225,1,0,
        0,0,50,227,1,0,0,0,52,229,1,0,0,0,54,237,1,0,0,0,56,239,1,0,0,0,
        58,246,1,0,0,0,60,252,1,0,0,0,62,256,1,0,0,0,64,263,1,0,0,0,66,265,
        1,0,0,0,68,275,1,0,0,0,70,280,1,0,0,0,72,73,5,1,0,0,73,74,5,34,0,
        0,74,75,5,2,0,0,75,76,3,2,1,0,76,77,3,12,6,0,77,78,5,3,0,0,78,79,
        3,18,9,0,79,80,5,4,0,0,80,81,6,0,-1,0,81,82,5,0,0,1,82,1,1,0,0,0,
        83,84,5,5,0,0,84,85,3,4,2,0,85,86,5,6,0,0,86,87,3,10,5,0,87,88,6,
        1,-1,0,88,89,5,2,0,0,89,90,3,8,4,0,90,93,1,0,0,0,91,93,1,0,0,0,92,
        83,1,0,0,0,92,91,1,0,0,0,93,3,1,0,0,0,94,95,5,34,0,0,95,96,6,2,-1,
        0,96,97,3,6,3,0,97,5,1,0,0,0,98,99,5,7,0,0,99,102,3,4,2,0,100,102,
        1,0,0,0,101,98,1,0,0,0,101,100,1,0,0,0,102,7,1,0,0,0,103,104,3,4,
        2,0,104,105,5,6,0,0,105,106,3,10,5,0,106,107,5,2,0,0,107,108,3,8,
        4,0,108,109,6,4,-1,0,109,112,1,0,0,0,110,112,1,0,0,0,111,103,1,0,
        0,0,111,110,1,0,0,0,112,9,1,0,0,0,113,114,7,0,0,0,114,11,1,0,0,0,
        115,116,5,10,0,0,116,117,5,34,0,0,117,118,5,11,0,0,118,119,3,14,
        7,0,119,120,5,12,0,0,120,121,5,13,0,0,121,122,3,2,1,0,122,123,3,
        18,9,0,123,124,5,14,0,0,124,125,5,2,0,0,125,128,1,0,0,0,126,128,
        1,0,0,0,127,115,1,0,0,0,127,126,1,0,0,0,128,13,1,0,0,0,129,130,5,
        34,0,0,130,131,5,6,0,0,131,132,3,10,5,0,132,133,3,16,8,0,133,136,
        1,0,0,0,134,136,1,0,0,0,135,129,1,0,0,0,135,134,1,0,0,0,136,15,1,
        0,0,0,137,138,5,7,0,0,138,141,3,14,7,0,139,141,1,0,0,0,140,137,1,
        0,0,0,140,139,1,0,0,0,141,17,1,0,0,0,142,143,5,15,0,0,143,144,3,
        22,11,0,144,145,5,16,0,0,145,19,1,0,0,0,146,152,3,44,22,0,147,152,
        3,32,16,0,148,152,3,30,15,0,149,152,3,66,33,0,150,152,3,24,12,0,
        151,146,1,0,0,0,151,147,1,0,0,0,151,148,1,0,0,0,151,149,1,0,0,0,
        151,150,1,0,0,0,152,21,1,0,0,0,153,154,3,20,10,0,154,155,3,22,11,
        0,155,158,1,0,0,0,156,158,1,0,0,0,157,153,1,0,0,0,157,156,1,0,0,
        0,158,23,1,0,0,0,159,160,5,17,0,0,160,161,5,11,0,0,161,162,3,26,
        13,0,162,163,3,28,14,0,163,164,5,12,0,0,164,165,5,2,0,0,165,25,1,
        0,0,0,166,169,3,38,19,0,167,169,5,35,0,0,168,166,1,0,0,0,168,167,
        1,0,0,0,169,27,1,0,0,0,170,171,5,7,0,0,171,172,3,26,13,0,172,173,
        3,28,14,0,173,176,1,0,0,0,174,176,1,0,0,0,175,170,1,0,0,0,175,174,
        1,0,0,0,176,29,1,0,0,0,177,178,5,18,0,0,178,179,3,18,9,0,179,180,
        5,19,0,0,180,181,5,11,0,0,181,182,3,38,19,0,182,183,5,12,0,0,183,
        184,5,2,0,0,184,31,1,0,0,0,185,186,5,20,0,0,186,187,5,11,0,0,187,
        188,3,38,19,0,188,189,5,12,0,0,189,190,3,18,9,0,190,191,3,34,17,
        0,191,192,5,2,0,0,192,33,1,0,0,0,193,194,5,21,0,0,194,197,3,18,9,
        0,195,197,1,0,0,0,196,193,1,0,0,0,196,195,1,0,0,0,197,35,1,0,0,0,
        198,199,7,1,0,0,199,37,1,0,0,0,200,201,3,46,23,0,201,202,3,40,20,
        0,202,39,1,0,0,0,203,204,3,42,21,0,204,205,3,46,23,0,205,208,1,0,
        0,0,206,208,1,0,0,0,207,203,1,0,0,0,207,206,1,0,0,0,208,41,1,0,0,
        0,209,210,7,2,0,0,210,43,1,0,0,0,211,212,5,34,0,0,212,213,6,22,-1,
        0,213,214,5,25,0,0,214,215,3,38,19,0,215,216,5,2,0,0,216,45,1,0,
        0,0,217,218,3,52,26,0,218,219,3,48,24,0,219,47,1,0,0,0,220,221,3,
        50,25,0,221,222,3,52,26,0,222,223,3,48,24,0,223,226,1,0,0,0,224,
        226,1,0,0,0,225,220,1,0,0,0,225,224,1,0,0,0,226,49,1,0,0,0,227,228,
        7,3,0,0,228,51,1,0,0,0,229,230,3,58,29,0,230,231,3,54,27,0,231,53,
        1,0,0,0,232,233,3,56,28,0,233,234,3,58,29,0,234,235,3,54,27,0,235,
        238,1,0,0,0,236,238,1,0,0,0,237,232,1,0,0,0,237,236,1,0,0,0,238,
        55,1,0,0,0,239,240,7,4,0,0,240,57,1,0,0,0,241,242,5,11,0,0,242,243,
        3,38,19,0,243,244,5,12,0,0,244,247,1,0,0,0,245,247,3,60,30,0,246,
        241,1,0,0,0,246,245,1,0,0,0,247,59,1,0,0,0,248,249,3,62,31,0,249,
        250,3,64,32,0,250,253,1,0,0,0,251,253,3,50,25,0,252,248,1,0,0,0,
        252,251,1,0,0,0,253,61,1,0,0,0,254,257,3,50,25,0,255,257,1,0,0,0,
        256,254,1,0,0,0,256,255,1,0,0,0,257,63,1,0,0,0,258,259,5,34,0,0,
        259,264,6,32,-1,0,260,261,3,36,18,0,261,262,6,32,-1,0,262,264,1,
        0,0,0,263,258,1,0,0,0,263,260,1,0,0,0,264,65,1,0,0,0,265,266,5,34,
        0,0,266,267,5,11,0,0,267,268,3,68,34,0,268,269,5,12,0,0,269,270,
        5,2,0,0,270,67,1,0,0,0,271,272,3,38,19,0,272,273,3,70,35,0,273,276,
        1,0,0,0,274,276,1,0,0,0,275,271,1,0,0,0,275,274,1,0,0,0,276,69,1,
        0,0,0,277,278,5,7,0,0,278,281,3,68,34,0,279,281,1,0,0,0,280,277,
        1,0,0,0,280,279,1,0,0,0,281,71,1,0,0,0,20,92,101,111,127,135,140,
        151,157,168,175,196,207,225,237,246,252,256,263,275,280
    ]

class little_duckParser ( Parser ):

    grammarFileName = "little_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "':'", "','", "'int'", "'float'", "'void'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'print'", 
                     "'do'", "'while'", "'if'", "'else'", "'>'", "'<'", 
                     "'!='", "'='", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NEWLINE", "WHITESPACE", 
                      "INT", "FLOAT", "ID", "STRING" ]

    RULE_programa = 0
    RULE_vars = 1
    RULE_vars_prime = 2
    RULE_vars_prime_prime = 3
    RULE_l_vars = 4
    RULE_type = 5
    RULE_funcs = 6
    RULE_funcs_prime = 7
    RULE_funcs_prime_prime = 8
    RULE_body = 9
    RULE_statement = 10
    RULE_l_statement = 11
    RULE_print = 12
    RULE_print_prime = 13
    RULE_l_print = 14
    RULE_cycle = 15
    RULE_condition = 16
    RULE_condition_prime = 17
    RULE_cte = 18
    RULE_expression = 19
    RULE_expression_prime = 20
    RULE_oper = 21
    RULE_assign = 22
    RULE_exp = 23
    RULE_l_exp = 24
    RULE_pm = 25
    RULE_termino = 26
    RULE_l_termino = 27
    RULE_ad = 28
    RULE_factor = 29
    RULE_factor_prime = 30
    RULE_b_factor = 31
    RULE_ic = 32
    RULE_f_call = 33
    RULE_f_call_prime = 34
    RULE_l_f_call_prime = 35

    ruleNames =  [ "programa", "vars", "vars_prime", "vars_prime_prime", 
                   "l_vars", "type", "funcs", "funcs_prime", "funcs_prime_prime", 
                   "body", "statement", "l_statement", "print", "print_prime", 
                   "l_print", "cycle", "condition", "condition_prime", "cte", 
                   "expression", "expression_prime", "oper", "assign", "exp", 
                   "l_exp", "pm", "termino", "l_termino", "ad", "factor", 
                   "factor_prime", "b_factor", "ic", "f_call", "f_call_prime", 
                   "l_f_call_prime" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    NEWLINE=30
    WHITESPACE=31
    INT=32
    FLOAT=33
    ID=34
    STRING=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def vars_(self):
            return self.getTypedRuleContext(little_duckParser.VarsContext,0)


        def funcs(self):
            return self.getTypedRuleContext(little_duckParser.FuncsContext,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def EOF(self):
            return self.getToken(little_duckParser.EOF, 0)

        def getRuleIndex(self):
            return little_duckParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = little_duckParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(little_duckParser.T__0)
            self.state = 73
            self.match(little_duckParser.ID)
            self.state = 74
            self.match(little_duckParser.T__1)
            self.state = 75
            self.vars_()
            self.state = 76
            self.funcs()
            self.state = 77
            self.match(little_duckParser.T__2)
            self.state = 78
            self.body()
            self.state = 79
            self.match(little_duckParser.T__3)
            inter.printGlobal()
            self.state = 81
            self.match(little_duckParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type = None # TypeContext

        def vars_prime(self):
            return self.getTypedRuleContext(little_duckParser.Vars_primeContext,0)


        def type_(self):
            return self.getTypedRuleContext(little_duckParser.TypeContext,0)


        def l_vars(self):
            return self.getTypedRuleContext(little_duckParser.L_varsContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = little_duckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(little_duckParser.T__4)
                self.state = 84
                self.vars_prime()
                self.state = 85
                self.match(little_duckParser.T__5)
                self.state = 86
                localctx._type = self.type_()
                inter.setTypes((None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)))
                self.state = 88
                self.match(little_duckParser.T__1)
                self.state = 89
                self.l_vars()
                pass
            elif token in [3, 10, 15]:
                self.enterOuterAlt(localctx, 2)

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


    class Vars_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def vars_prime_prime(self):
            return self.getTypedRuleContext(little_duckParser.Vars_prime_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_vars_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_prime" ):
                listener.enterVars_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_prime" ):
                listener.exitVars_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars_prime" ):
                return visitor.visitVars_prime(self)
            else:
                return visitor.visitChildren(self)




    def vars_prime(self):

        localctx = little_duckParser.Vars_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars_prime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            localctx._ID = self.match(little_duckParser.ID)
            inter.addVariable((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 96
            self.vars_prime_prime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_prime_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_prime(self):
            return self.getTypedRuleContext(little_duckParser.Vars_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_vars_prime_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_prime_prime" ):
                listener.enterVars_prime_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_prime_prime" ):
                listener.exitVars_prime_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars_prime_prime" ):
                return visitor.visitVars_prime_prime(self)
            else:
                return visitor.visitChildren(self)




    def vars_prime_prime(self):

        localctx = little_duckParser.Vars_prime_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vars_prime_prime)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(little_duckParser.T__6)
                self.state = 99
                self.vars_prime()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

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


    class L_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._type = None # TypeContext

        def vars_prime(self):
            return self.getTypedRuleContext(little_duckParser.Vars_primeContext,0)


        def type_(self):
            return self.getTypedRuleContext(little_duckParser.TypeContext,0)


        def l_vars(self):
            return self.getTypedRuleContext(little_duckParser.L_varsContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_vars" ):
                listener.enterL_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_vars" ):
                listener.exitL_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_vars" ):
                return visitor.visitL_vars(self)
            else:
                return visitor.visitChildren(self)




    def l_vars(self):

        localctx = little_duckParser.L_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_l_vars)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.vars_prime()
                self.state = 104
                self.match(little_duckParser.T__5)
                self.state = 105
                localctx._type = self.type_()
                self.state = 106
                self.match(little_duckParser.T__1)
                self.state = 107
                self.l_vars()
                inter.setTypes((None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)))
                pass
            elif token in [3, 10, 15]:
                self.enterOuterAlt(localctx, 2)

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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = little_duckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def funcs_prime(self):
            return self.getTypedRuleContext(little_duckParser.Funcs_primeContext,0)


        def vars_(self):
            return self.getTypedRuleContext(little_duckParser.VarsContext,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs" ):
                return visitor.visitFuncs(self)
            else:
                return visitor.visitChildren(self)




    def funcs(self):

        localctx = little_duckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcs)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(little_duckParser.T__9)
                self.state = 116
                self.match(little_duckParser.ID)
                self.state = 117
                self.match(little_duckParser.T__10)
                self.state = 118
                self.funcs_prime()
                self.state = 119
                self.match(little_duckParser.T__11)
                self.state = 120
                self.match(little_duckParser.T__12)
                self.state = 121
                self.vars_()
                self.state = 122
                self.body()
                self.state = 123
                self.match(little_duckParser.T__13)
                self.state = 124
                self.match(little_duckParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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


    class Funcs_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(little_duckParser.TypeContext,0)


        def funcs_prime_prime(self):
            return self.getTypedRuleContext(little_duckParser.Funcs_prime_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs_prime" ):
                listener.enterFuncs_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs_prime" ):
                listener.exitFuncs_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs_prime" ):
                return visitor.visitFuncs_prime(self)
            else:
                return visitor.visitChildren(self)




    def funcs_prime(self):

        localctx = little_duckParser.Funcs_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcs_prime)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(little_duckParser.ID)
                self.state = 130
                self.match(little_duckParser.T__5)
                self.state = 131
                self.type_()
                self.state = 132
                self.funcs_prime_prime()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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


    class Funcs_prime_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs_prime(self):
            return self.getTypedRuleContext(little_duckParser.Funcs_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_funcs_prime_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs_prime_prime" ):
                listener.enterFuncs_prime_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs_prime_prime" ):
                listener.exitFuncs_prime_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs_prime_prime" ):
                return visitor.visitFuncs_prime_prime(self)
            else:
                return visitor.visitChildren(self)




    def funcs_prime_prime(self):

        localctx = little_duckParser.Funcs_prime_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcs_prime_prime)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(little_duckParser.T__6)
                self.state = 138
                self.funcs_prime()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def l_statement(self):
            return self.getTypedRuleContext(little_duckParser.L_statementContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = little_duckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(little_duckParser.T__14)
            self.state = 143
            self.l_statement()
            self.state = 144
            self.match(little_duckParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(little_duckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(little_duckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(little_duckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(little_duckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(little_duckParser.PrintContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = little_duckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(little_duckParser.StatementContext,0)


        def l_statement(self):
            return self.getTypedRuleContext(little_duckParser.L_statementContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_statement" ):
                listener.enterL_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_statement" ):
                listener.exitL_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_statement" ):
                return visitor.visitL_statement(self)
            else:
                return visitor.visitChildren(self)




    def l_statement(self):

        localctx = little_duckParser.L_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_l_statement)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 20, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.statement()
                self.state = 154
                self.l_statement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)

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


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_prime(self):
            return self.getTypedRuleContext(little_duckParser.Print_primeContext,0)


        def l_print(self):
            return self.getTypedRuleContext(little_duckParser.L_printContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = little_duckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(little_duckParser.T__16)
            self.state = 160
            self.match(little_duckParser.T__10)
            self.state = 161
            self.print_prime()
            self.state = 162
            self.l_print()
            self.state = 163
            self.match(little_duckParser.T__11)
            self.state = 164
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(little_duckParser.STRING, 0)

        def getRuleIndex(self):
            return little_duckParser.RULE_print_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_prime" ):
                listener.enterPrint_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_prime" ):
                listener.exitPrint_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_prime" ):
                return visitor.visitPrint_prime(self)
            else:
                return visitor.visitChildren(self)




    def print_prime(self):

        localctx = little_duckParser.Print_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print_prime)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.expression()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(little_duckParser.STRING)
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


    class L_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_prime(self):
            return self.getTypedRuleContext(little_duckParser.Print_primeContext,0)


        def l_print(self):
            return self.getTypedRuleContext(little_duckParser.L_printContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_print" ):
                listener.enterL_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_print" ):
                listener.exitL_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_print" ):
                return visitor.visitL_print(self)
            else:
                return visitor.visitChildren(self)




    def l_print(self):

        localctx = little_duckParser.L_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_l_print)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(little_duckParser.T__6)
                self.state = 171
                self.print_prime()
                self.state = 172
                self.l_print()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycle" ):
                return visitor.visitCycle(self)
            else:
                return visitor.visitChildren(self)




    def cycle(self):

        localctx = little_duckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(little_duckParser.T__17)
            self.state = 178
            self.body()
            self.state = 179
            self.match(little_duckParser.T__18)
            self.state = 180
            self.match(little_duckParser.T__10)
            self.state = 181
            self.expression()
            self.state = 182
            self.match(little_duckParser.T__11)
            self.state = 183
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def condition_prime(self):
            return self.getTypedRuleContext(little_duckParser.Condition_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = little_duckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(little_duckParser.T__19)
            self.state = 186
            self.match(little_duckParser.T__10)
            self.state = 187
            self.expression()
            self.state = 188
            self.match(little_duckParser.T__11)
            self.state = 189
            self.body()
            self.state = 190
            self.condition_prime()
            self.state = 191
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_condition_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_prime" ):
                listener.enterCondition_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_prime" ):
                listener.exitCondition_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_prime" ):
                return visitor.visitCondition_prime(self)
            else:
                return visitor.visitChildren(self)




    def condition_prime(self):

        localctx = little_duckParser.Condition_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition_prime)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(little_duckParser.T__20)
                self.state = 194
                self.body()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(little_duckParser.INT, 0)

        def FLOAT(self):
            return self.getToken(little_duckParser.FLOAT, 0)

        def getRuleIndex(self):
            return little_duckParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCte" ):
                return visitor.visitCte(self)
            else:
                return visitor.visitChildren(self)




    def cte(self):

        localctx = little_duckParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(little_duckParser.ExpContext,0)


        def expression_prime(self):
            return self.getTypedRuleContext(little_duckParser.Expression_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = little_duckParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.exp()
            self.state = 201
            self.expression_prime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oper(self):
            return self.getTypedRuleContext(little_duckParser.OperContext,0)


        def exp(self):
            return self.getTypedRuleContext(little_duckParser.ExpContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_expression_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_prime" ):
                listener.enterExpression_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_prime" ):
                listener.exitExpression_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_prime" ):
                return visitor.visitExpression_prime(self)
            else:
                return visitor.visitChildren(self)




    def expression_prime(self):

        localctx = little_duckParser.Expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression_prime)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.oper()
                self.state = 204
                self.exp()
                pass
            elif token in [2, 7, 12]:
                self.enterOuterAlt(localctx, 2)

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


    class OperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_oper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOper" ):
                listener.enterOper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOper" ):
                listener.exitOper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOper" ):
                return visitor.visitOper(self)
            else:
                return visitor.visitChildren(self)




    def oper(self):

        localctx = little_duckParser.OperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_oper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = little_duckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            localctx._ID = self.match(little_duckParser.ID)
            inter.isNotDefined((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 213
            self.match(little_duckParser.T__24)
            self.state = 214
            self.expression()
            self.state = 215
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(little_duckParser.TerminoContext,0)


        def l_exp(self):
            return self.getTypedRuleContext(little_duckParser.L_expContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = little_duckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.termino()
            self.state = 218
            self.l_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pm(self):
            return self.getTypedRuleContext(little_duckParser.PmContext,0)


        def termino(self):
            return self.getTypedRuleContext(little_duckParser.TerminoContext,0)


        def l_exp(self):
            return self.getTypedRuleContext(little_duckParser.L_expContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_exp" ):
                listener.enterL_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_exp" ):
                listener.exitL_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_exp" ):
                return visitor.visitL_exp(self)
            else:
                return visitor.visitChildren(self)




    def l_exp(self):

        localctx = little_duckParser.L_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_l_exp)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.pm()
                self.state = 221
                self.termino()
                self.state = 222
                self.l_exp()
                pass
            elif token in [2, 7, 12, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)

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


    class PmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_pm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPm" ):
                listener.enterPm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPm" ):
                listener.exitPm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPm" ):
                return visitor.visitPm(self)
            else:
                return visitor.visitChildren(self)




    def pm(self):

        localctx = little_duckParser.PmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_pm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(little_duckParser.FactorContext,0)


        def l_termino(self):
            return self.getTypedRuleContext(little_duckParser.L_terminoContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = little_duckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.factor()
            self.state = 230
            self.l_termino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L_terminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ad(self):
            return self.getTypedRuleContext(little_duckParser.AdContext,0)


        def factor(self):
            return self.getTypedRuleContext(little_duckParser.FactorContext,0)


        def l_termino(self):
            return self.getTypedRuleContext(little_duckParser.L_terminoContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_termino" ):
                listener.enterL_termino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_termino" ):
                listener.exitL_termino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_termino" ):
                return visitor.visitL_termino(self)
            else:
                return visitor.visitChildren(self)




    def l_termino(self):

        localctx = little_duckParser.L_terminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_l_termino)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.ad()
                self.state = 233
                self.factor()
                self.state = 234
                self.l_termino()
                pass
            elif token in [2, 7, 12, 22, 23, 24, 26, 27]:
                self.enterOuterAlt(localctx, 2)

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


    class AdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_ad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAd" ):
                listener.enterAd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAd" ):
                listener.exitAd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAd" ):
                return visitor.visitAd(self)
            else:
                return visitor.visitChildren(self)




    def ad(self):

        localctx = little_duckParser.AdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def factor_prime(self):
            return self.getTypedRuleContext(little_duckParser.Factor_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = little_duckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_factor)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(little_duckParser.T__10)
                self.state = 242
                self.expression()
                self.state = 243
                self.match(little_duckParser.T__11)
                pass
            elif token in [26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.factor_prime()
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


    class Factor_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b_factor(self):
            return self.getTypedRuleContext(little_duckParser.B_factorContext,0)


        def ic(self):
            return self.getTypedRuleContext(little_duckParser.IcContext,0)


        def pm(self):
            return self.getTypedRuleContext(little_duckParser.PmContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_factor_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_prime" ):
                listener.enterFactor_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_prime" ):
                listener.exitFactor_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_prime" ):
                return visitor.visitFactor_prime(self)
            else:
                return visitor.visitChildren(self)




    def factor_prime(self):

        localctx = little_duckParser.Factor_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_factor_prime)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.b_factor()
                self.state = 249
                self.ic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.pm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class B_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pm(self):
            return self.getTypedRuleContext(little_duckParser.PmContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_b_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB_factor" ):
                listener.enterB_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB_factor" ):
                listener.exitB_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_factor" ):
                return visitor.visitB_factor(self)
            else:
                return visitor.visitChildren(self)




    def b_factor(self):

        localctx = little_duckParser.B_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_b_factor)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.pm()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 2)

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


    class IcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(little_duckParser.CteContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_ic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIc" ):
                listener.enterIc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIc" ):
                listener.exitIc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIc" ):
                return visitor.visitIc(self)
            else:
                return visitor.visitChildren(self)




    def ic(self):

        localctx = little_duckParser.IcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ic)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                localctx._ID = self.match(little_duckParser.ID)
                inter.isNotDefined((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.cte()
                # ID or Constant
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


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def f_call_prime(self):
            return self.getTypedRuleContext(little_duckParser.F_call_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_call" ):
                return visitor.visitF_call(self)
            else:
                return visitor.visitChildren(self)




    def f_call(self):

        localctx = little_duckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(little_duckParser.ID)
            self.state = 266
            self.match(little_duckParser.T__10)
            self.state = 267
            self.f_call_prime()
            self.state = 268
            self.match(little_duckParser.T__11)
            self.state = 269
            self.match(little_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(little_duckParser.ExpressionContext,0)


        def l_f_call_prime(self):
            return self.getTypedRuleContext(little_duckParser.L_f_call_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_f_call_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call_prime" ):
                listener.enterF_call_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call_prime" ):
                listener.exitF_call_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_call_prime" ):
                return visitor.visitF_call_prime(self)
            else:
                return visitor.visitChildren(self)




    def f_call_prime(self):

        localctx = little_duckParser.F_call_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_f_call_prime)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expression()
                self.state = 272
                self.l_f_call_prime()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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


    class L_f_call_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_call_prime(self):
            return self.getTypedRuleContext(little_duckParser.F_call_primeContext,0)


        def getRuleIndex(self):
            return little_duckParser.RULE_l_f_call_prime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_f_call_prime" ):
                listener.enterL_f_call_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_f_call_prime" ):
                listener.exitL_f_call_prime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_f_call_prime" ):
                return visitor.visitL_f_call_prime(self)
            else:
                return visitor.visitChildren(self)




    def l_f_call_prime(self):

        localctx = little_duckParser.L_f_call_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_l_f_call_prime)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(little_duckParser.T__6)
                self.state = 278
                self.f_call_prime()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)

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




