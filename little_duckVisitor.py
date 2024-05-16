# Generated from little_duck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

# This class defines a complete generic visitor for a parse tree produced by little_duckParser.

class little_duckVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by little_duckParser#programa.
    def visitPrograma(self, ctx:little_duckParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#vars.
    def visitVars(self, ctx:little_duckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#vars_prime.
    def visitVars_prime(self, ctx:little_duckParser.Vars_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#vars_prime_prime.
    def visitVars_prime_prime(self, ctx:little_duckParser.Vars_prime_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_vars.
    def visitL_vars(self, ctx:little_duckParser.L_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#type.
    def visitType(self, ctx:little_duckParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs.
    def visitFuncs(self, ctx:little_duckParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs_prime.
    def visitFuncs_prime(self, ctx:little_duckParser.Funcs_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#funcs_prime_prime.
    def visitFuncs_prime_prime(self, ctx:little_duckParser.Funcs_prime_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#body.
    def visitBody(self, ctx:little_duckParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#statement.
    def visitStatement(self, ctx:little_duckParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_statement.
    def visitL_statement(self, ctx:little_duckParser.L_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#print.
    def visitPrint(self, ctx:little_duckParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#print_prime.
    def visitPrint_prime(self, ctx:little_duckParser.Print_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_print.
    def visitL_print(self, ctx:little_duckParser.L_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#cycle.
    def visitCycle(self, ctx:little_duckParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#condition.
    def visitCondition(self, ctx:little_duckParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#condition_prime.
    def visitCondition_prime(self, ctx:little_duckParser.Condition_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#cte.
    def visitCte(self, ctx:little_duckParser.CteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#expression.
    def visitExpression(self, ctx:little_duckParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#expression_prime.
    def visitExpression_prime(self, ctx:little_duckParser.Expression_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#oper.
    def visitOper(self, ctx:little_duckParser.OperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#assign.
    def visitAssign(self, ctx:little_duckParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#exp.
    def visitExp(self, ctx:little_duckParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_exp.
    def visitL_exp(self, ctx:little_duckParser.L_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#pm.
    def visitPm(self, ctx:little_duckParser.PmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#termino.
    def visitTermino(self, ctx:little_duckParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_termino.
    def visitL_termino(self, ctx:little_duckParser.L_terminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#ad.
    def visitAd(self, ctx:little_duckParser.AdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor.
    def visitFactor(self, ctx:little_duckParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#factor_prime.
    def visitFactor_prime(self, ctx:little_duckParser.Factor_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#b_factor.
    def visitB_factor(self, ctx:little_duckParser.B_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#ic.
    def visitIc(self, ctx:little_duckParser.IcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call.
    def visitF_call(self, ctx:little_duckParser.F_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#f_call_prime.
    def visitF_call_prime(self, ctx:little_duckParser.F_call_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by little_duckParser#l_f_call_prime.
    def visitL_f_call_prime(self, ctx:little_duckParser.L_f_call_primeContext):
        return self.visitChildren(ctx)



del little_duckParser