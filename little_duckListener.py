# Generated from little_duck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

# This class defines a complete listener for a parse tree produced by little_duckParser.
class little_duckListener(ParseTreeListener):

    # Enter a parse tree produced by little_duckParser#programa.
    def enterPrograma(self, ctx:little_duckParser.ProgramaContext):
        pass

    # Exit a parse tree produced by little_duckParser#programa.
    def exitPrograma(self, ctx:little_duckParser.ProgramaContext):
        pass


    # Enter a parse tree produced by little_duckParser#vars.
    def enterVars(self, ctx:little_duckParser.VarsContext):
        pass

    # Exit a parse tree produced by little_duckParser#vars.
    def exitVars(self, ctx:little_duckParser.VarsContext):
        pass


    # Enter a parse tree produced by little_duckParser#vars_prime.
    def enterVars_prime(self, ctx:little_duckParser.Vars_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#vars_prime.
    def exitVars_prime(self, ctx:little_duckParser.Vars_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#vars_prime_prime.
    def enterVars_prime_prime(self, ctx:little_duckParser.Vars_prime_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#vars_prime_prime.
    def exitVars_prime_prime(self, ctx:little_duckParser.Vars_prime_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_vars.
    def enterL_vars(self, ctx:little_duckParser.L_varsContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_vars.
    def exitL_vars(self, ctx:little_duckParser.L_varsContext):
        pass


    # Enter a parse tree produced by little_duckParser#type.
    def enterType(self, ctx:little_duckParser.TypeContext):
        pass

    # Exit a parse tree produced by little_duckParser#type.
    def exitType(self, ctx:little_duckParser.TypeContext):
        pass


    # Enter a parse tree produced by little_duckParser#funcs.
    def enterFuncs(self, ctx:little_duckParser.FuncsContext):
        pass

    # Exit a parse tree produced by little_duckParser#funcs.
    def exitFuncs(self, ctx:little_duckParser.FuncsContext):
        pass


    # Enter a parse tree produced by little_duckParser#funcs_prime.
    def enterFuncs_prime(self, ctx:little_duckParser.Funcs_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#funcs_prime.
    def exitFuncs_prime(self, ctx:little_duckParser.Funcs_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#funcs_prime_prime.
    def enterFuncs_prime_prime(self, ctx:little_duckParser.Funcs_prime_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#funcs_prime_prime.
    def exitFuncs_prime_prime(self, ctx:little_duckParser.Funcs_prime_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#body.
    def enterBody(self, ctx:little_duckParser.BodyContext):
        pass

    # Exit a parse tree produced by little_duckParser#body.
    def exitBody(self, ctx:little_duckParser.BodyContext):
        pass


    # Enter a parse tree produced by little_duckParser#statement.
    def enterStatement(self, ctx:little_duckParser.StatementContext):
        pass

    # Exit a parse tree produced by little_duckParser#statement.
    def exitStatement(self, ctx:little_duckParser.StatementContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_statement.
    def enterL_statement(self, ctx:little_duckParser.L_statementContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_statement.
    def exitL_statement(self, ctx:little_duckParser.L_statementContext):
        pass


    # Enter a parse tree produced by little_duckParser#print.
    def enterPrint(self, ctx:little_duckParser.PrintContext):
        pass

    # Exit a parse tree produced by little_duckParser#print.
    def exitPrint(self, ctx:little_duckParser.PrintContext):
        pass


    # Enter a parse tree produced by little_duckParser#print_prime.
    def enterPrint_prime(self, ctx:little_duckParser.Print_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#print_prime.
    def exitPrint_prime(self, ctx:little_duckParser.Print_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_print.
    def enterL_print(self, ctx:little_duckParser.L_printContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_print.
    def exitL_print(self, ctx:little_duckParser.L_printContext):
        pass


    # Enter a parse tree produced by little_duckParser#cycle.
    def enterCycle(self, ctx:little_duckParser.CycleContext):
        pass

    # Exit a parse tree produced by little_duckParser#cycle.
    def exitCycle(self, ctx:little_duckParser.CycleContext):
        pass


    # Enter a parse tree produced by little_duckParser#condition.
    def enterCondition(self, ctx:little_duckParser.ConditionContext):
        pass

    # Exit a parse tree produced by little_duckParser#condition.
    def exitCondition(self, ctx:little_duckParser.ConditionContext):
        pass


    # Enter a parse tree produced by little_duckParser#condition_prime.
    def enterCondition_prime(self, ctx:little_duckParser.Condition_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#condition_prime.
    def exitCondition_prime(self, ctx:little_duckParser.Condition_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#cte.
    def enterCte(self, ctx:little_duckParser.CteContext):
        pass

    # Exit a parse tree produced by little_duckParser#cte.
    def exitCte(self, ctx:little_duckParser.CteContext):
        pass


    # Enter a parse tree produced by little_duckParser#expression.
    def enterExpression(self, ctx:little_duckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by little_duckParser#expression.
    def exitExpression(self, ctx:little_duckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by little_duckParser#expression_prime.
    def enterExpression_prime(self, ctx:little_duckParser.Expression_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#expression_prime.
    def exitExpression_prime(self, ctx:little_duckParser.Expression_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#oper.
    def enterOper(self, ctx:little_duckParser.OperContext):
        pass

    # Exit a parse tree produced by little_duckParser#oper.
    def exitOper(self, ctx:little_duckParser.OperContext):
        pass


    # Enter a parse tree produced by little_duckParser#assign.
    def enterAssign(self, ctx:little_duckParser.AssignContext):
        pass

    # Exit a parse tree produced by little_duckParser#assign.
    def exitAssign(self, ctx:little_duckParser.AssignContext):
        pass


    # Enter a parse tree produced by little_duckParser#exp.
    def enterExp(self, ctx:little_duckParser.ExpContext):
        pass

    # Exit a parse tree produced by little_duckParser#exp.
    def exitExp(self, ctx:little_duckParser.ExpContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_exp.
    def enterL_exp(self, ctx:little_duckParser.L_expContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_exp.
    def exitL_exp(self, ctx:little_duckParser.L_expContext):
        pass


    # Enter a parse tree produced by little_duckParser#pm.
    def enterPm(self, ctx:little_duckParser.PmContext):
        pass

    # Exit a parse tree produced by little_duckParser#pm.
    def exitPm(self, ctx:little_duckParser.PmContext):
        pass


    # Enter a parse tree produced by little_duckParser#termino.
    def enterTermino(self, ctx:little_duckParser.TerminoContext):
        pass

    # Exit a parse tree produced by little_duckParser#termino.
    def exitTermino(self, ctx:little_duckParser.TerminoContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_termino.
    def enterL_termino(self, ctx:little_duckParser.L_terminoContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_termino.
    def exitL_termino(self, ctx:little_duckParser.L_terminoContext):
        pass


    # Enter a parse tree produced by little_duckParser#ad.
    def enterAd(self, ctx:little_duckParser.AdContext):
        pass

    # Exit a parse tree produced by little_duckParser#ad.
    def exitAd(self, ctx:little_duckParser.AdContext):
        pass


    # Enter a parse tree produced by little_duckParser#factor.
    def enterFactor(self, ctx:little_duckParser.FactorContext):
        pass

    # Exit a parse tree produced by little_duckParser#factor.
    def exitFactor(self, ctx:little_duckParser.FactorContext):
        pass


    # Enter a parse tree produced by little_duckParser#factor_prime.
    def enterFactor_prime(self, ctx:little_duckParser.Factor_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#factor_prime.
    def exitFactor_prime(self, ctx:little_duckParser.Factor_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#b_factor.
    def enterB_factor(self, ctx:little_duckParser.B_factorContext):
        pass

    # Exit a parse tree produced by little_duckParser#b_factor.
    def exitB_factor(self, ctx:little_duckParser.B_factorContext):
        pass


    # Enter a parse tree produced by little_duckParser#ic.
    def enterIc(self, ctx:little_duckParser.IcContext):
        pass

    # Exit a parse tree produced by little_duckParser#ic.
    def exitIc(self, ctx:little_duckParser.IcContext):
        pass


    # Enter a parse tree produced by little_duckParser#f_call.
    def enterF_call(self, ctx:little_duckParser.F_callContext):
        pass

    # Exit a parse tree produced by little_duckParser#f_call.
    def exitF_call(self, ctx:little_duckParser.F_callContext):
        pass


    # Enter a parse tree produced by little_duckParser#f_call_prime.
    def enterF_call_prime(self, ctx:little_duckParser.F_call_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#f_call_prime.
    def exitF_call_prime(self, ctx:little_duckParser.F_call_primeContext):
        pass


    # Enter a parse tree produced by little_duckParser#l_f_call_prime.
    def enterL_f_call_prime(self, ctx:little_duckParser.L_f_call_primeContext):
        pass

    # Exit a parse tree produced by little_duckParser#l_f_call_prime.
    def exitL_f_call_prime(self, ctx:little_duckParser.L_f_call_primeContext):
        pass



del little_duckParser