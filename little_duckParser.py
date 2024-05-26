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
        4,1,35,323,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,98,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,107,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,117,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,137,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,3,7,148,8,7,1,8,1,8,1,8,3,8,153,8,8,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,164,8,10,1,11,1,11,1,11,1,
        11,3,11,170,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,3,13,184,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,
        14,193,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,3,17,219,8,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,
        20,1,20,3,20,232,8,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,256,8,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,3,27,271,8,27,1,28,1,28,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,3,29,282,8,29,1,30,1,30,1,30,1,30,1,31,1,31,3,31,290,
        8,31,1,32,1,32,1,32,3,32,295,8,32,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,3,33,304,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,3,35,316,8,35,1,36,1,36,1,36,3,36,321,8,36,1,36,0,0,37,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,0,5,1,0,8,9,1,0,32,33,1,0,22,
        24,1,0,26,27,1,0,28,29,308,0,74,1,0,0,0,2,97,1,0,0,0,4,99,1,0,0,
        0,6,106,1,0,0,0,8,116,1,0,0,0,10,118,1,0,0,0,12,136,1,0,0,0,14,147,
        1,0,0,0,16,152,1,0,0,0,18,154,1,0,0,0,20,163,1,0,0,0,22,169,1,0,
        0,0,24,171,1,0,0,0,26,183,1,0,0,0,28,192,1,0,0,0,30,194,1,0,0,0,
        32,204,1,0,0,0,34,218,1,0,0,0,36,220,1,0,0,0,38,222,1,0,0,0,40,231,
        1,0,0,0,42,233,1,0,0,0,44,235,1,0,0,0,46,244,1,0,0,0,48,255,1,0,
        0,0,50,257,1,0,0,0,52,259,1,0,0,0,54,270,1,0,0,0,56,272,1,0,0,0,
        58,281,1,0,0,0,60,283,1,0,0,0,62,289,1,0,0,0,64,294,1,0,0,0,66,303,
        1,0,0,0,68,305,1,0,0,0,70,315,1,0,0,0,72,320,1,0,0,0,74,75,5,1,0,
        0,75,76,5,34,0,0,76,77,5,2,0,0,77,78,6,0,-1,0,78,79,3,2,1,0,79,80,
        3,12,6,0,80,81,5,3,0,0,81,82,6,0,-1,0,82,83,3,18,9,0,83,84,5,4,0,
        0,84,85,5,0,0,1,85,86,6,0,-1,0,86,87,6,0,-1,0,87,1,1,0,0,0,88,89,
        5,5,0,0,89,90,3,4,2,0,90,91,5,6,0,0,91,92,3,10,5,0,92,93,6,1,-1,
        0,93,94,5,2,0,0,94,95,3,8,4,0,95,98,1,0,0,0,96,98,1,0,0,0,97,88,
        1,0,0,0,97,96,1,0,0,0,98,3,1,0,0,0,99,100,5,34,0,0,100,101,6,2,-1,
        0,101,102,3,6,3,0,102,5,1,0,0,0,103,104,5,7,0,0,104,107,3,4,2,0,
        105,107,1,0,0,0,106,103,1,0,0,0,106,105,1,0,0,0,107,7,1,0,0,0,108,
        109,3,4,2,0,109,110,5,6,0,0,110,111,3,10,5,0,111,112,5,2,0,0,112,
        113,3,8,4,0,113,114,6,4,-1,0,114,117,1,0,0,0,115,117,1,0,0,0,116,
        108,1,0,0,0,116,115,1,0,0,0,117,9,1,0,0,0,118,119,7,0,0,0,119,11,
        1,0,0,0,120,121,5,10,0,0,121,122,5,34,0,0,122,123,6,6,-1,0,123,124,
        5,11,0,0,124,125,3,14,7,0,125,126,5,12,0,0,126,127,5,13,0,0,127,
        128,3,2,1,0,128,129,3,18,9,0,129,130,5,14,0,0,130,131,5,2,0,0,131,
        132,6,6,-1,0,132,133,6,6,-1,0,133,134,3,12,6,0,134,137,1,0,0,0,135,
        137,1,0,0,0,136,120,1,0,0,0,136,135,1,0,0,0,137,13,1,0,0,0,138,139,
        5,34,0,0,139,140,6,7,-1,0,140,141,5,6,0,0,141,142,3,10,5,0,142,143,
        6,7,-1,0,143,144,6,7,-1,0,144,145,3,16,8,0,145,148,1,0,0,0,146,148,
        1,0,0,0,147,138,1,0,0,0,147,146,1,0,0,0,148,15,1,0,0,0,149,150,5,
        7,0,0,150,153,3,14,7,0,151,153,1,0,0,0,152,149,1,0,0,0,152,151,1,
        0,0,0,153,17,1,0,0,0,154,155,5,15,0,0,155,156,3,22,11,0,156,157,
        5,16,0,0,157,19,1,0,0,0,158,164,3,44,22,0,159,164,3,32,16,0,160,
        164,3,30,15,0,161,164,3,68,34,0,162,164,3,24,12,0,163,158,1,0,0,
        0,163,159,1,0,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,
        0,164,21,1,0,0,0,165,166,3,20,10,0,166,167,3,22,11,0,167,170,1,0,
        0,0,168,170,1,0,0,0,169,165,1,0,0,0,169,168,1,0,0,0,170,23,1,0,0,
        0,171,172,5,17,0,0,172,173,6,12,-1,0,173,174,5,11,0,0,174,175,3,
        26,13,0,175,176,3,28,14,0,176,177,5,12,0,0,177,178,5,2,0,0,178,179,
        6,12,-1,0,179,25,1,0,0,0,180,184,3,38,19,0,181,182,5,35,0,0,182,
        184,6,13,-1,0,183,180,1,0,0,0,183,181,1,0,0,0,184,27,1,0,0,0,185,
        186,5,7,0,0,186,187,6,14,-1,0,187,188,3,26,13,0,188,189,6,14,-1,
        0,189,190,3,28,14,0,190,193,1,0,0,0,191,193,1,0,0,0,192,185,1,0,
        0,0,192,191,1,0,0,0,193,29,1,0,0,0,194,195,5,18,0,0,195,196,6,15,
        -1,0,196,197,3,18,9,0,197,198,5,19,0,0,198,199,5,11,0,0,199,200,
        3,38,19,0,200,201,5,12,0,0,201,202,5,2,0,0,202,203,6,15,-1,0,203,
        31,1,0,0,0,204,205,5,20,0,0,205,206,5,11,0,0,206,207,3,38,19,0,207,
        208,5,12,0,0,208,209,6,16,-1,0,209,210,3,18,9,0,210,211,3,34,17,
        0,211,212,5,2,0,0,212,213,6,16,-1,0,213,33,1,0,0,0,214,215,5,21,
        0,0,215,216,6,17,-1,0,216,219,3,18,9,0,217,219,1,0,0,0,218,214,1,
        0,0,0,218,217,1,0,0,0,219,35,1,0,0,0,220,221,7,1,0,0,221,37,1,0,
        0,0,222,223,3,46,23,0,223,224,3,40,20,0,224,39,1,0,0,0,225,226,3,
        42,21,0,226,227,6,20,-1,0,227,228,3,46,23,0,228,229,6,20,-1,0,229,
        232,1,0,0,0,230,232,1,0,0,0,231,225,1,0,0,0,231,230,1,0,0,0,232,
        41,1,0,0,0,233,234,7,2,0,0,234,43,1,0,0,0,235,236,5,34,0,0,236,237,
        6,22,-1,0,237,238,6,22,-1,0,238,239,5,25,0,0,239,240,6,22,-1,0,240,
        241,3,38,19,0,241,242,5,2,0,0,242,243,6,22,-1,0,243,45,1,0,0,0,244,
        245,3,52,26,0,245,246,6,23,-1,0,246,247,3,48,24,0,247,47,1,0,0,0,
        248,249,3,50,25,0,249,250,6,24,-1,0,250,251,3,52,26,0,251,252,6,
        24,-1,0,252,253,3,48,24,0,253,256,1,0,0,0,254,256,1,0,0,0,255,248,
        1,0,0,0,255,254,1,0,0,0,256,49,1,0,0,0,257,258,7,3,0,0,258,51,1,
        0,0,0,259,260,3,58,29,0,260,261,6,26,-1,0,261,262,3,54,27,0,262,
        53,1,0,0,0,263,264,3,56,28,0,264,265,6,27,-1,0,265,266,3,58,29,0,
        266,267,6,27,-1,0,267,268,3,54,27,0,268,271,1,0,0,0,269,271,1,0,
        0,0,270,263,1,0,0,0,270,269,1,0,0,0,271,55,1,0,0,0,272,273,7,4,0,
        0,273,57,1,0,0,0,274,275,5,11,0,0,275,276,6,29,-1,0,276,277,3,38,
        19,0,277,278,5,12,0,0,278,279,6,29,-1,0,279,282,1,0,0,0,280,282,
        3,60,30,0,281,274,1,0,0,0,281,280,1,0,0,0,282,59,1,0,0,0,283,284,
        3,62,31,0,284,285,3,66,33,0,285,286,6,30,-1,0,286,61,1,0,0,0,287,
        290,3,64,32,0,288,290,1,0,0,0,289,287,1,0,0,0,289,288,1,0,0,0,290,
        63,1,0,0,0,291,295,5,26,0,0,292,293,5,27,0,0,293,295,6,32,-1,0,294,
        291,1,0,0,0,294,292,1,0,0,0,295,65,1,0,0,0,296,297,5,34,0,0,297,
        298,6,33,-1,0,298,304,6,33,-1,0,299,300,3,36,18,0,300,301,6,33,-1,
        0,301,302,6,33,-1,0,302,304,1,0,0,0,303,296,1,0,0,0,303,299,1,0,
        0,0,304,67,1,0,0,0,305,306,5,34,0,0,306,307,5,11,0,0,307,308,3,70,
        35,0,308,309,5,12,0,0,309,310,5,2,0,0,310,69,1,0,0,0,311,312,3,38,
        19,0,312,313,3,72,36,0,313,316,1,0,0,0,314,316,1,0,0,0,315,311,1,
        0,0,0,315,314,1,0,0,0,316,71,1,0,0,0,317,318,5,7,0,0,318,321,3,70,
        35,0,319,321,1,0,0,0,320,317,1,0,0,0,320,319,1,0,0,0,321,73,1,0,
        0,0,20,97,106,116,136,147,152,163,169,183,192,218,231,255,270,281,
        289,294,303,315,320
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
    RULE_pm_const = 32
    RULE_ic = 33
    RULE_f_call = 34
    RULE_f_call_prime = 35
    RULE_l_f_call_prime = 36

    ruleNames =  [ "programa", "vars", "vars_prime", "vars_prime_prime", 
                   "l_vars", "type", "funcs", "funcs_prime", "funcs_prime_prime", 
                   "body", "statement", "l_statement", "print", "print_prime", 
                   "l_print", "cycle", "condition", "condition_prime", "cte", 
                   "expression", "expression_prime", "oper", "assign", "exp", 
                   "l_exp", "pm", "termino", "l_termino", "ad", "factor", 
                   "factor_prime", "b_factor", "pm_const", "ic", "f_call", 
                   "f_call_prime", "l_f_call_prime" ]

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
            self.state = 74
            self.match(little_duckParser.T__0)
            self.state = 75
            self.match(little_duckParser.ID)
            self.state = 76
            self.match(little_duckParser.T__1)
            inter.setVariableScope('global')
            self.state = 78
            self.vars_()
            self.state = 79
            self.funcs()
            self.state = 80
            self.match(little_duckParser.T__2)
            inter.setMainQuad()
            self.state = 82
            self.body()
            self.state = 83
            self.match(little_duckParser.T__3)
            self.state = 84
            self.match(little_duckParser.EOF)
            inter.endQuad()
            inter.printGlobal()
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(little_duckParser.T__4)
                self.state = 89
                self.vars_prime()
                self.state = 90
                self.match(little_duckParser.T__5)
                self.state = 91
                localctx._type = self.type_()
                inter.setTypes((None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)))
                self.state = 93
                self.match(little_duckParser.T__1)
                self.state = 94
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
            self.state = 99
            localctx._ID = self.match(little_duckParser.ID)
            inter.addVariable((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 101
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
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(little_duckParser.T__6)
                self.state = 104
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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.vars_prime()
                self.state = 109
                self.match(little_duckParser.T__5)
                self.state = 110
                localctx._type = self.type_()
                self.state = 111
                self.match(little_duckParser.T__1)
                self.state = 112
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
            self.state = 118
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
            self._ID = None # Token

        def ID(self):
            return self.getToken(little_duckParser.ID, 0)

        def funcs_prime(self):
            return self.getTypedRuleContext(little_duckParser.Funcs_primeContext,0)


        def vars_(self):
            return self.getTypedRuleContext(little_duckParser.VarsContext,0)


        def body(self):
            return self.getTypedRuleContext(little_duckParser.BodyContext,0)


        def funcs(self):
            return self.getTypedRuleContext(little_duckParser.FuncsContext,0)


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
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(little_duckParser.T__9)
                self.state = 121
                localctx._ID = self.match(little_duckParser.ID)
                inter.setVariableScope((None if localctx._ID is None else localctx._ID.text))
                self.state = 123
                self.match(little_duckParser.T__10)
                self.state = 124
                self.funcs_prime()
                self.state = 125
                self.match(little_duckParser.T__11)
                self.state = 126
                self.match(little_duckParser.T__12)
                self.state = 127
                self.vars_()
                self.state = 128
                self.body()
                self.state = 129
                self.match(little_duckParser.T__13)
                self.state = 130
                self.match(little_duckParser.T__1)
                inter.setVariableScope('global')
                inter.endFunc()
                self.state = 133
                self.funcs()
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
            self._ID = None # Token
            self._type = None # TypeContext

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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                localctx._ID = self.match(little_duckParser.ID)
                inter.addVariable((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 140
                self.match(little_duckParser.T__5)
                self.state = 141
                localctx._type = self.type_()
                inter.setTypes((None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)))
                inter.countParams()
                self.state = 144
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
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(little_duckParser.T__6)
                self.state = 150
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
            self.state = 154
            self.match(little_duckParser.T__14)
            self.state = 155
            self.l_statement()
            self.state = 156
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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 20, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.statement()
                self.state = 166
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
            self.state = 171
            self.match(little_duckParser.T__16)
            inter.keyPoint_OperationPush('PRINT')
            self.state = 173
            self.match(little_duckParser.T__10)
            self.state = 174
            self.print_prime()
            self.state = 175
            self.l_print()
            self.state = 176
            self.match(little_duckParser.T__11)
            self.state = 177
            self.match(little_duckParser.T__1)
            inter.keyPoint_CreateQuad(4)
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
            self._STRING = None # Token

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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expression()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                localctx._STRING = self.match(little_duckParser.STRING)
                inter.keyPoint_1((None if localctx._STRING is None else localctx._STRING.text), (0 if localctx._STRING is None else localctx._STRING.type))
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
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(little_duckParser.T__6)
                inter.keyPoint_OperationPush(',')
                self.state = 187
                self.print_prime()
                inter.keyPoint_CreateQuad(3)
                self.state = 189
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
            self.state = 194
            self.match(little_duckParser.T__17)
            inter.whileKeyOne()
            self.state = 196
            self.body()
            self.state = 197
            self.match(little_duckParser.T__18)
            self.state = 198
            self.match(little_duckParser.T__10)
            self.state = 199
            self.expression()
            self.state = 200
            self.match(little_duckParser.T__11)
            self.state = 201
            self.match(little_duckParser.T__1)
            inter.endWhile()
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
            self.state = 204
            self.match(little_duckParser.T__19)
            self.state = 205
            self.match(little_duckParser.T__10)
            self.state = 206
            self.expression()
            self.state = 207
            self.match(little_duckParser.T__11)
            inter.createGoToF()
            self.state = 209
            self.body()
            self.state = 210
            self.condition_prime()
            self.state = 211
            self.match(little_duckParser.T__1)
            inter.if_Fill()
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
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(little_duckParser.T__20)
                inter.else_Fill()
                self.state = 216
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
            self.state = 220
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
            self.state = 222
            self.exp()
            self.state = 223
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
            self._oper = None # OperContext

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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                localctx._oper = self.oper()
                inter.keyPoint_OperationPush((None if localctx._oper is None else self._input.getText(localctx._oper.start,localctx._oper.stop)))
                self.state = 227
                self.exp()
                inter.keyPoint_CreateQuad(2)
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
            self.state = 233
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
            self.state = 235
            localctx._ID = self.match(little_duckParser.ID)
            inter.isNotDefined((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            inter.keyPoint_1((None if localctx._ID is None else localctx._ID.text))
            self.state = 238
            self.match(little_duckParser.T__24)
            inter.keyPoint_OperationPush('=')
            self.state = 240
            self.expression()
            self.state = 241
            self.match(little_duckParser.T__1)
            inter.keyPoint_CreateQuad(3)
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
            self.state = 244
            self.termino()
            inter.keyPoint_CreateQuad(0)
            self.state = 246
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
            self._pm = None # PmContext

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
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx._pm = self.pm()
                inter.keyPoint_OperationPush((None if localctx._pm is None else self._input.getText(localctx._pm.start,localctx._pm.stop)))
                self.state = 250
                self.termino()
                inter.keyPoint_CreateQuad(0)
                self.state = 252
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
            self.state = 257
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
            self.state = 259
            self.factor()
            inter.keyPoint_CreateQuad(1)
            self.state = 261
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
            self._ad = None # AdContext

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
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                localctx._ad = self.ad()
                inter.keyPoint_OperationPush((None if localctx._ad is None else self._input.getText(localctx._ad.start,localctx._ad.stop)))
                self.state = 265
                self.factor()
                inter.keyPoint_CreateQuad(1)
                self.state = 267
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
            self.state = 272
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
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(little_duckParser.T__10)
                inter.keyPoint_PushBottom()
                self.state = 276
                self.expression()
                self.state = 277
                self.match(little_duckParser.T__11)
                inter.keyPoint_PopFalse()
                pass
            elif token in [26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.b_factor()
            self.state = 284
            self.ic()
            # removed | pm
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

        def pm_const(self):
            return self.getTypedRuleContext(little_duckParser.Pm_constContext,0)


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
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.pm_const()
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


    class Pm_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return little_duckParser.RULE_pm_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPm_const" ):
                listener.enterPm_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPm_const" ):
                listener.exitPm_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPm_const" ):
                return visitor.visitPm_const(self)
            else:
                return visitor.visitChildren(self)




    def pm_const(self):

        localctx = little_duckParser.Pm_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_pm_const)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(little_duckParser.T__25)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.match(little_duckParser.T__26)
                inter.setMinusOne()
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
            self._cte = None # CteContext

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
        self.enterRule(localctx, 66, self.RULE_ic)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                localctx._ID = self.match(little_duckParser.ID)
                inter.isNotDefined((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                inter.keyPoint_1((None if localctx._ID is None else localctx._ID.text))
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                localctx._cte = self.cte()
                inter.keyPoint_1((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)), (None if localctx._cte is None else localctx._cte.stop).type)
                # This rule chesk if this is ID or Constant
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
        self.enterRule(localctx, 68, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(little_duckParser.ID)
            self.state = 306
            self.match(little_duckParser.T__10)
            self.state = 307
            self.f_call_prime()
            self.state = 308
            self.match(little_duckParser.T__11)
            self.state = 309
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
        self.enterRule(localctx, 70, self.RULE_f_call_prime)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 26, 27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.expression()
                self.state = 312
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
        self.enterRule(localctx, 72, self.RULE_l_f_call_prime)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(little_duckParser.T__6)
                self.state = 318
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





