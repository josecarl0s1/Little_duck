// Generated from c:/Users/josec/OneDrive/Documentos/GitHub/Little_duck/little_duck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link little_duckParser}.
 */
public interface little_duckListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link little_duckParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(little_duckParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(little_duckParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(little_duckParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(little_duckParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#vars_prime}.
	 * @param ctx the parse tree
	 */
	void enterVars_prime(little_duckParser.Vars_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#vars_prime}.
	 * @param ctx the parse tree
	 */
	void exitVars_prime(little_duckParser.Vars_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#vars_prime_prime}.
	 * @param ctx the parse tree
	 */
	void enterVars_prime_prime(little_duckParser.Vars_prime_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#vars_prime_prime}.
	 * @param ctx the parse tree
	 */
	void exitVars_prime_prime(little_duckParser.Vars_prime_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_vars}.
	 * @param ctx the parse tree
	 */
	void enterL_vars(little_duckParser.L_varsContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_vars}.
	 * @param ctx the parse tree
	 */
	void exitL_vars(little_duckParser.L_varsContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(little_duckParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(little_duckParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(little_duckParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(little_duckParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#funcs_prime}.
	 * @param ctx the parse tree
	 */
	void enterFuncs_prime(little_duckParser.Funcs_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#funcs_prime}.
	 * @param ctx the parse tree
	 */
	void exitFuncs_prime(little_duckParser.Funcs_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#funcs_prime_prime}.
	 * @param ctx the parse tree
	 */
	void enterFuncs_prime_prime(little_duckParser.Funcs_prime_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#funcs_prime_prime}.
	 * @param ctx the parse tree
	 */
	void exitFuncs_prime_prime(little_duckParser.Funcs_prime_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(little_duckParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(little_duckParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(little_duckParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(little_duckParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_statement}.
	 * @param ctx the parse tree
	 */
	void enterL_statement(little_duckParser.L_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_statement}.
	 * @param ctx the parse tree
	 */
	void exitL_statement(little_duckParser.L_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(little_duckParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(little_duckParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#print_prime}.
	 * @param ctx the parse tree
	 */
	void enterPrint_prime(little_duckParser.Print_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#print_prime}.
	 * @param ctx the parse tree
	 */
	void exitPrint_prime(little_duckParser.Print_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_print}.
	 * @param ctx the parse tree
	 */
	void enterL_print(little_duckParser.L_printContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_print}.
	 * @param ctx the parse tree
	 */
	void exitL_print(little_duckParser.L_printContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(little_duckParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(little_duckParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(little_duckParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(little_duckParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#condition_prime}.
	 * @param ctx the parse tree
	 */
	void enterCondition_prime(little_duckParser.Condition_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#condition_prime}.
	 * @param ctx the parse tree
	 */
	void exitCondition_prime(little_duckParser.Condition_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(little_duckParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(little_duckParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(little_duckParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(little_duckParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#expression_prime}.
	 * @param ctx the parse tree
	 */
	void enterExpression_prime(little_duckParser.Expression_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#expression_prime}.
	 * @param ctx the parse tree
	 */
	void exitExpression_prime(little_duckParser.Expression_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#oper}.
	 * @param ctx the parse tree
	 */
	void enterOper(little_duckParser.OperContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#oper}.
	 * @param ctx the parse tree
	 */
	void exitOper(little_duckParser.OperContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(little_duckParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(little_duckParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(little_duckParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(little_duckParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_exp}.
	 * @param ctx the parse tree
	 */
	void enterL_exp(little_duckParser.L_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_exp}.
	 * @param ctx the parse tree
	 */
	void exitL_exp(little_duckParser.L_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#pm}.
	 * @param ctx the parse tree
	 */
	void enterPm(little_duckParser.PmContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#pm}.
	 * @param ctx the parse tree
	 */
	void exitPm(little_duckParser.PmContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(little_duckParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(little_duckParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_termino}.
	 * @param ctx the parse tree
	 */
	void enterL_termino(little_duckParser.L_terminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_termino}.
	 * @param ctx the parse tree
	 */
	void exitL_termino(little_duckParser.L_terminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#ad}.
	 * @param ctx the parse tree
	 */
	void enterAd(little_duckParser.AdContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#ad}.
	 * @param ctx the parse tree
	 */
	void exitAd(little_duckParser.AdContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(little_duckParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(little_duckParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#factor_prime}.
	 * @param ctx the parse tree
	 */
	void enterFactor_prime(little_duckParser.Factor_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#factor_prime}.
	 * @param ctx the parse tree
	 */
	void exitFactor_prime(little_duckParser.Factor_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#b_factor}.
	 * @param ctx the parse tree
	 */
	void enterB_factor(little_duckParser.B_factorContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#b_factor}.
	 * @param ctx the parse tree
	 */
	void exitB_factor(little_duckParser.B_factorContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#ic}.
	 * @param ctx the parse tree
	 */
	void enterIc(little_duckParser.IcContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#ic}.
	 * @param ctx the parse tree
	 */
	void exitIc(little_duckParser.IcContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#f_call}.
	 * @param ctx the parse tree
	 */
	void enterF_call(little_duckParser.F_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#f_call}.
	 * @param ctx the parse tree
	 */
	void exitF_call(little_duckParser.F_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#f_call_prime}.
	 * @param ctx the parse tree
	 */
	void enterF_call_prime(little_duckParser.F_call_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#f_call_prime}.
	 * @param ctx the parse tree
	 */
	void exitF_call_prime(little_duckParser.F_call_primeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#l_f_call_prime}.
	 * @param ctx the parse tree
	 */
	void enterL_f_call_prime(little_duckParser.L_f_call_primeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#l_f_call_prime}.
	 * @param ctx the parse tree
	 */
	void exitL_f_call_prime(little_duckParser.L_f_call_primeContext ctx);
}