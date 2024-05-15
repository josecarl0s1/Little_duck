// Generated from little_duck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class little_duckParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, NEWLINE=30, WHITESPACE=31, 
		INT=32, FLOAT=33, ID=34, STRING=35;
	public static final int
		RULE_programa = 0, RULE_vars = 1, RULE_vars_prime = 2, RULE_vars_prime_prime = 3, 
		RULE_l_vars = 4, RULE_type = 5, RULE_funcs = 6, RULE_funcs_prime = 7, 
		RULE_funcs_prime_prime = 8, RULE_body = 9, RULE_statement = 10, RULE_l_statement = 11, 
		RULE_print = 12, RULE_print_prime = 13, RULE_l_print = 14, RULE_cycle = 15, 
		RULE_condition = 16, RULE_condition_prime = 17, RULE_cte = 18, RULE_expression = 19, 
		RULE_expression_prime = 20, RULE_oper = 21, RULE_assign = 22, RULE_exp = 23, 
		RULE_l_exp = 24, RULE_pm = 25, RULE_termino = 26, RULE_l_termino = 27, 
		RULE_ad = 28, RULE_factor = 29, RULE_factor_prime = 30, RULE_b_factor = 31, 
		RULE_ic = 32, RULE_f_call = 33, RULE_f_call_prime = 34, RULE_l_f_call_prime = 35;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "vars", "vars_prime", "vars_prime_prime", "l_vars", "type", 
			"funcs", "funcs_prime", "funcs_prime_prime", "body", "statement", "l_statement", 
			"print", "print_prime", "l_print", "cycle", "condition", "condition_prime", 
			"cte", "expression", "expression_prime", "oper", "assign", "exp", "l_exp", 
			"pm", "termino", "l_termino", "ad", "factor", "factor_prime", "b_factor", 
			"ic", "f_call", "f_call_prime", "l_f_call_prime"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'main'", "'end'", "'var'", "':'", "','", "'int'", 
			"'float'", "'void'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'print'", 
			"'do'", "'while'", "'if'", "'else'", "'>'", "'<'", "'!='", "'='", "'+'", 
			"'-'", "'*'", "'/'", null, "' '"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "NEWLINE", "WHITESPACE", "INT", "FLOAT", 
			"ID", "STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "little_duck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public little_duckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode EOF() { return getToken(little_duckParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(T__0);
			setState(73);
			match(ID);
			setState(74);
			match(T__1);
			setState(75);
			vars();
			setState(76);
			funcs();
			setState(77);
			match(T__2);
			setState(78);
			body();
			setState(79);
			match(T__3);
			setState(80);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public Vars_primeContext vars_prime() {
			return getRuleContext(Vars_primeContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public L_varsContext l_vars() {
			return getRuleContext(L_varsContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterVars(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitVars(this);
		}
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vars);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				match(T__4);
				setState(83);
				vars_prime();
				setState(84);
				match(T__5);
				setState(85);
				type();
				setState(86);
				match(T__1);
				setState(87);
				l_vars();
				}
				break;
			case T__2:
			case T__9:
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Vars_primeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public Vars_prime_primeContext vars_prime_prime() {
			return getRuleContext(Vars_prime_primeContext.class,0);
		}
		public Vars_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterVars_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitVars_prime(this);
		}
	}

	public final Vars_primeContext vars_prime() throws RecognitionException {
		Vars_primeContext _localctx = new Vars_primeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars_prime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(ID);
			setState(93);
			vars_prime_prime();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Vars_prime_primeContext extends ParserRuleContext {
		public Vars_primeContext vars_prime() {
			return getRuleContext(Vars_primeContext.class,0);
		}
		public Vars_prime_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_prime_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterVars_prime_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitVars_prime_prime(this);
		}
	}

	public final Vars_prime_primeContext vars_prime_prime() throws RecognitionException {
		Vars_prime_primeContext _localctx = new Vars_prime_primeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vars_prime_prime);
		try {
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				match(T__6);
				setState(96);
				vars_prime();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_varsContext extends ParserRuleContext {
		public Vars_primeContext vars_prime() {
			return getRuleContext(Vars_primeContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public L_varsContext l_vars() {
			return getRuleContext(L_varsContext.class,0);
		}
		public L_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_vars; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_vars(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_vars(this);
		}
	}

	public final L_varsContext l_vars() throws RecognitionException {
		L_varsContext _localctx = new L_varsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_l_vars);
		try {
			setState(107);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				vars_prime();
				setState(101);
				match(T__5);
				setState(102);
				type();
				setState(103);
				match(T__1);
				setState(104);
				l_vars();
				}
				break;
			case T__2:
			case T__9:
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitType(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_la = _input.LA(1);
			if ( !(_la==T__7 || _la==T__8) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public Funcs_primeContext funcs_prime() {
			return getRuleContext(Funcs_primeContext.class,0);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterFuncs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitFuncs(this);
		}
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcs);
		try {
			setState(123);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				match(T__9);
				setState(112);
				match(ID);
				setState(113);
				match(T__10);
				setState(114);
				funcs_prime();
				setState(115);
				match(T__11);
				setState(116);
				match(T__12);
				setState(117);
				vars();
				setState(118);
				body();
				setState(119);
				match(T__13);
				setState(120);
				match(T__1);
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Funcs_primeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Funcs_prime_primeContext funcs_prime_prime() {
			return getRuleContext(Funcs_prime_primeContext.class,0);
		}
		public Funcs_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterFuncs_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitFuncs_prime(this);
		}
	}

	public final Funcs_primeContext funcs_prime() throws RecognitionException {
		Funcs_primeContext _localctx = new Funcs_primeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_funcs_prime);
		try {
			setState(131);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(125);
				match(ID);
				setState(126);
				match(T__5);
				setState(127);
				type();
				setState(128);
				funcs_prime_prime();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Funcs_prime_primeContext extends ParserRuleContext {
		public Funcs_primeContext funcs_prime() {
			return getRuleContext(Funcs_primeContext.class,0);
		}
		public Funcs_prime_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs_prime_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterFuncs_prime_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitFuncs_prime_prime(this);
		}
	}

	public final Funcs_prime_primeContext funcs_prime_prime() throws RecognitionException {
		Funcs_prime_primeContext _localctx = new Funcs_prime_primeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_funcs_prime_prime);
		try {
			setState(136);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				match(T__6);
				setState(134);
				funcs_prime();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public L_statementContext l_statement() {
			return getRuleContext(L_statementContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(T__14);
			setState(139);
			l_statement();
			setState(140);
			match(T__15);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public F_callContext f_call() {
			return getRuleContext(F_callContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		try {
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(145);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(146);
				print();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_statementContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public L_statementContext l_statement() {
			return getRuleContext(L_statementContext.class,0);
		}
		public L_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_statement(this);
		}
	}

	public final L_statementContext l_statement() throws RecognitionException {
		L_statementContext _localctx = new L_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_l_statement);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
			case T__17:
			case T__19:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(149);
				statement();
				setState(150);
				l_statement();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public Print_primeContext print_prime() {
			return getRuleContext(Print_primeContext.class,0);
		}
		public L_printContext l_print() {
			return getRuleContext(L_printContext.class,0);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitPrint(this);
		}
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(T__16);
			setState(156);
			match(T__10);
			setState(157);
			print_prime();
			setState(158);
			l_print();
			setState(159);
			match(T__11);
			setState(160);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_primeContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(little_duckParser.STRING, 0); }
		public Print_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterPrint_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitPrint_prime(this);
		}
	}

	public final Print_primeContext print_prime() throws RecognitionException {
		Print_primeContext _localctx = new Print_primeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_print_prime);
		try {
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__25:
			case T__26:
			case INT:
			case FLOAT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				expression();
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_printContext extends ParserRuleContext {
		public Print_primeContext print_prime() {
			return getRuleContext(Print_primeContext.class,0);
		}
		public L_printContext l_print() {
			return getRuleContext(L_printContext.class,0);
		}
		public L_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_print; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_print(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_print(this);
		}
	}

	public final L_printContext l_print() throws RecognitionException {
		L_printContext _localctx = new L_printContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_l_print);
		try {
			setState(171);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				match(T__6);
				setState(167);
				print_prime();
				setState(168);
				l_print();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterCycle(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitCycle(this);
		}
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(T__17);
			setState(174);
			body();
			setState(175);
			match(T__18);
			setState(176);
			match(T__10);
			setState(177);
			expression();
			setState(178);
			match(T__11);
			setState(179);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public Condition_primeContext condition_prime() {
			return getRuleContext(Condition_primeContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(T__19);
			setState(182);
			match(T__10);
			setState(183);
			expression();
			setState(184);
			match(T__11);
			setState(185);
			body();
			setState(186);
			condition_prime();
			setState(187);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_primeContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public Condition_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterCondition_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitCondition_prime(this);
		}
	}

	public final Condition_primeContext condition_prime() throws RecognitionException {
		Condition_primeContext _localctx = new Condition_primeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_condition_prime);
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				match(T__20);
				setState(190);
				body();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(little_duckParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(little_duckParser.FLOAT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterCte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitCte(this);
		}
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Expression_primeContext expression_prime() {
			return getRuleContext(Expression_primeContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			exp();
			setState(197);
			expression_prime();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression_primeContext extends ParserRuleContext {
		public OperContext oper() {
			return getRuleContext(OperContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Expression_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterExpression_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitExpression_prime(this);
		}
	}

	public final Expression_primeContext expression_prime() throws RecognitionException {
		Expression_primeContext _localctx = new Expression_primeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expression_prime);
		try {
			setState(203);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
			case T__22:
			case T__23:
				enterOuterAlt(_localctx, 1);
				{
				setState(199);
				oper();
				setState(200);
				exp();
				}
				break;
			case T__1:
			case T__6:
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperContext extends ParserRuleContext {
		public OperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_oper; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterOper(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitOper(this);
		}
	}

	public final OperContext oper() throws RecognitionException {
		OperContext _localctx = new OperContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_oper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitAssign(this);
		}
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(ID);
			setState(208);
			match(T__24);
			setState(209);
			expression();
			setState(210);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public L_expContext l_exp() {
			return getRuleContext(L_expContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			termino();
			setState(213);
			l_exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_expContext extends ParserRuleContext {
		public PmContext pm() {
			return getRuleContext(PmContext.class,0);
		}
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public L_expContext l_exp() {
			return getRuleContext(L_expContext.class,0);
		}
		public L_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_exp(this);
		}
	}

	public final L_expContext l_exp() throws RecognitionException {
		L_expContext _localctx = new L_expContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_l_exp);
		try {
			setState(220);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				pm();
				setState(216);
				termino();
				setState(217);
				l_exp();
				}
				break;
			case T__1:
			case T__6:
			case T__11:
			case T__21:
			case T__22:
			case T__23:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PmContext extends ParserRuleContext {
		public PmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterPm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitPm(this);
		}
	}

	public final PmContext pm() throws RecognitionException {
		PmContext _localctx = new PmContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_pm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			_la = _input.LA(1);
			if ( !(_la==T__25 || _la==T__26) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public L_terminoContext l_termino() {
			return getRuleContext(L_terminoContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterTermino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitTermino(this);
		}
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			factor();
			setState(225);
			l_termino();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_terminoContext extends ParserRuleContext {
		public AdContext ad() {
			return getRuleContext(AdContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public L_terminoContext l_termino() {
			return getRuleContext(L_terminoContext.class,0);
		}
		public L_terminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_termino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_termino(this);
		}
	}

	public final L_terminoContext l_termino() throws RecognitionException {
		L_terminoContext _localctx = new L_terminoContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_l_termino);
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				ad();
				setState(228);
				factor();
				setState(229);
				l_termino();
				}
				break;
			case T__1:
			case T__6:
			case T__11:
			case T__21:
			case T__22:
			case T__23:
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdContext extends ParserRuleContext {
		public AdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ad; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterAd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitAd(this);
		}
	}

	public final AdContext ad() throws RecognitionException {
		AdContext _localctx = new AdContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_ad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			_la = _input.LA(1);
			if ( !(_la==T__27 || _la==T__28) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Factor_primeContext factor_prime() {
			return getRuleContext(Factor_primeContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_factor);
		try {
			setState(241);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				match(T__10);
				setState(237);
				expression();
				setState(238);
				match(T__11);
				}
				break;
			case T__25:
			case T__26:
			case INT:
			case FLOAT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(240);
				factor_prime();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Factor_primeContext extends ParserRuleContext {
		public B_factorContext b_factor() {
			return getRuleContext(B_factorContext.class,0);
		}
		public IcContext ic() {
			return getRuleContext(IcContext.class,0);
		}
		public PmContext pm() {
			return getRuleContext(PmContext.class,0);
		}
		public Factor_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterFactor_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitFactor_prime(this);
		}
	}

	public final Factor_primeContext factor_prime() throws RecognitionException {
		Factor_primeContext _localctx = new Factor_primeContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_factor_prime);
		try {
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(243);
				b_factor();
				setState(244);
				ic();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(246);
				pm();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class B_factorContext extends ParserRuleContext {
		public PmContext pm() {
			return getRuleContext(PmContext.class,0);
		}
		public B_factorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_b_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterB_factor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitB_factor(this);
		}
	}

	public final B_factorContext b_factor() throws RecognitionException {
		B_factorContext _localctx = new B_factorContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_b_factor);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(249);
				pm();
				}
				break;
			case INT:
			case FLOAT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IcContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public IcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ic; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterIc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitIc(this);
		}
	}

	public final IcContext ic() throws RecognitionException {
		IcContext _localctx = new IcContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_ic);
		try {
			setState(255);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				match(ID);
				}
				break;
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(254);
				cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public F_call_primeContext f_call_prime() {
			return getRuleContext(F_call_primeContext.class,0);
		}
		public F_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterF_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitF_call(this);
		}
	}

	public final F_callContext f_call() throws RecognitionException {
		F_callContext _localctx = new F_callContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_f_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(ID);
			setState(258);
			match(T__10);
			setState(259);
			f_call_prime();
			setState(260);
			match(T__11);
			setState(261);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_call_primeContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public L_f_call_primeContext l_f_call_prime() {
			return getRuleContext(L_f_call_primeContext.class,0);
		}
		public F_call_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterF_call_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitF_call_prime(this);
		}
	}

	public final F_call_primeContext f_call_prime() throws RecognitionException {
		F_call_primeContext _localctx = new F_call_primeContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_f_call_prime);
		try {
			setState(267);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__25:
			case T__26:
			case INT:
			case FLOAT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				expression();
				setState(264);
				l_f_call_prime();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class L_f_call_primeContext extends ParserRuleContext {
		public F_call_primeContext f_call_prime() {
			return getRuleContext(F_call_primeContext.class,0);
		}
		public L_f_call_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l_f_call_prime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).enterL_f_call_prime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof little_duckListener ) ((little_duckListener)listener).exitL_f_call_prime(this);
		}
	}

	public final L_f_call_primeContext l_f_call_prime() throws RecognitionException {
		L_f_call_primeContext _localctx = new L_f_call_primeContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_l_f_call_prime);
		try {
			setState(272);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				match(T__6);
				setState(270);
				f_call_prime();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001#\u0113\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001[\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003c\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004l\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006|\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u0084\b\u0007\u0001\b\u0001\b\u0001\b\u0003\b\u0089\b\b\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u0094\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u009a\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\r\u0001\r\u0003\r\u00a5\b\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u00ac\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u00c1\b\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00cc\b\u0014"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u00dd\b\u0018\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u00e9\b\u001b\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0003\u001d\u00f2\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0003\u001e\u00f8\b\u001e\u0001\u001f\u0001\u001f\u0003\u001f\u00fc\b"+
		"\u001f\u0001 \u0001 \u0003 \u0100\b \u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001!\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u010c\b\"\u0001#\u0001"+
		"#\u0001#\u0003#\u0111\b#\u0001#\u0000\u0000$\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02"+
		"468:<>@BDF\u0000\u0005\u0001\u0000\b\t\u0001\u0000 !\u0001\u0000\u0016"+
		"\u0018\u0001\u0000\u001a\u001b\u0001\u0000\u001c\u001d\u0105\u0000H\u0001"+
		"\u0000\u0000\u0000\u0002Z\u0001\u0000\u0000\u0000\u0004\\\u0001\u0000"+
		"\u0000\u0000\u0006b\u0001\u0000\u0000\u0000\bk\u0001\u0000\u0000\u0000"+
		"\nm\u0001\u0000\u0000\u0000\f{\u0001\u0000\u0000\u0000\u000e\u0083\u0001"+
		"\u0000\u0000\u0000\u0010\u0088\u0001\u0000\u0000\u0000\u0012\u008a\u0001"+
		"\u0000\u0000\u0000\u0014\u0093\u0001\u0000\u0000\u0000\u0016\u0099\u0001"+
		"\u0000\u0000\u0000\u0018\u009b\u0001\u0000\u0000\u0000\u001a\u00a4\u0001"+
		"\u0000\u0000\u0000\u001c\u00ab\u0001\u0000\u0000\u0000\u001e\u00ad\u0001"+
		"\u0000\u0000\u0000 \u00b5\u0001\u0000\u0000\u0000\"\u00c0\u0001\u0000"+
		"\u0000\u0000$\u00c2\u0001\u0000\u0000\u0000&\u00c4\u0001\u0000\u0000\u0000"+
		"(\u00cb\u0001\u0000\u0000\u0000*\u00cd\u0001\u0000\u0000\u0000,\u00cf"+
		"\u0001\u0000\u0000\u0000.\u00d4\u0001\u0000\u0000\u00000\u00dc\u0001\u0000"+
		"\u0000\u00002\u00de\u0001\u0000\u0000\u00004\u00e0\u0001\u0000\u0000\u0000"+
		"6\u00e8\u0001\u0000\u0000\u00008\u00ea\u0001\u0000\u0000\u0000:\u00f1"+
		"\u0001\u0000\u0000\u0000<\u00f7\u0001\u0000\u0000\u0000>\u00fb\u0001\u0000"+
		"\u0000\u0000@\u00ff\u0001\u0000\u0000\u0000B\u0101\u0001\u0000\u0000\u0000"+
		"D\u010b\u0001\u0000\u0000\u0000F\u0110\u0001\u0000\u0000\u0000HI\u0005"+
		"\u0001\u0000\u0000IJ\u0005\"\u0000\u0000JK\u0005\u0002\u0000\u0000KL\u0003"+
		"\u0002\u0001\u0000LM\u0003\f\u0006\u0000MN\u0005\u0003\u0000\u0000NO\u0003"+
		"\u0012\t\u0000OP\u0005\u0004\u0000\u0000PQ\u0005\u0000\u0000\u0001Q\u0001"+
		"\u0001\u0000\u0000\u0000RS\u0005\u0005\u0000\u0000ST\u0003\u0004\u0002"+
		"\u0000TU\u0005\u0006\u0000\u0000UV\u0003\n\u0005\u0000VW\u0005\u0002\u0000"+
		"\u0000WX\u0003\b\u0004\u0000X[\u0001\u0000\u0000\u0000Y[\u0001\u0000\u0000"+
		"\u0000ZR\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\u0003\u0001"+
		"\u0000\u0000\u0000\\]\u0005\"\u0000\u0000]^\u0003\u0006\u0003\u0000^\u0005"+
		"\u0001\u0000\u0000\u0000_`\u0005\u0007\u0000\u0000`c\u0003\u0004\u0002"+
		"\u0000ac\u0001\u0000\u0000\u0000b_\u0001\u0000\u0000\u0000ba\u0001\u0000"+
		"\u0000\u0000c\u0007\u0001\u0000\u0000\u0000de\u0003\u0004\u0002\u0000"+
		"ef\u0005\u0006\u0000\u0000fg\u0003\n\u0005\u0000gh\u0005\u0002\u0000\u0000"+
		"hi\u0003\b\u0004\u0000il\u0001\u0000\u0000\u0000jl\u0001\u0000\u0000\u0000"+
		"kd\u0001\u0000\u0000\u0000kj\u0001\u0000\u0000\u0000l\t\u0001\u0000\u0000"+
		"\u0000mn\u0007\u0000\u0000\u0000n\u000b\u0001\u0000\u0000\u0000op\u0005"+
		"\n\u0000\u0000pq\u0005\"\u0000\u0000qr\u0005\u000b\u0000\u0000rs\u0003"+
		"\u000e\u0007\u0000st\u0005\f\u0000\u0000tu\u0005\r\u0000\u0000uv\u0003"+
		"\u0002\u0001\u0000vw\u0003\u0012\t\u0000wx\u0005\u000e\u0000\u0000xy\u0005"+
		"\u0002\u0000\u0000y|\u0001\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000"+
		"{o\u0001\u0000\u0000\u0000{z\u0001\u0000\u0000\u0000|\r\u0001\u0000\u0000"+
		"\u0000}~\u0005\"\u0000\u0000~\u007f\u0005\u0006\u0000\u0000\u007f\u0080"+
		"\u0003\n\u0005\u0000\u0080\u0081\u0003\u0010\b\u0000\u0081\u0084\u0001"+
		"\u0000\u0000\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083}\u0001\u0000"+
		"\u0000\u0000\u0083\u0082\u0001\u0000\u0000\u0000\u0084\u000f\u0001\u0000"+
		"\u0000\u0000\u0085\u0086\u0005\u0007\u0000\u0000\u0086\u0089\u0003\u000e"+
		"\u0007\u0000\u0087\u0089\u0001\u0000\u0000\u0000\u0088\u0085\u0001\u0000"+
		"\u0000\u0000\u0088\u0087\u0001\u0000\u0000\u0000\u0089\u0011\u0001\u0000"+
		"\u0000\u0000\u008a\u008b\u0005\u000f\u0000\u0000\u008b\u008c\u0003\u0016"+
		"\u000b\u0000\u008c\u008d\u0005\u0010\u0000\u0000\u008d\u0013\u0001\u0000"+
		"\u0000\u0000\u008e\u0094\u0003,\u0016\u0000\u008f\u0094\u0003 \u0010\u0000"+
		"\u0090\u0094\u0003\u001e\u000f\u0000\u0091\u0094\u0003B!\u0000\u0092\u0094"+
		"\u0003\u0018\f\u0000\u0093\u008e\u0001\u0000\u0000\u0000\u0093\u008f\u0001"+
		"\u0000\u0000\u0000\u0093\u0090\u0001\u0000\u0000\u0000\u0093\u0091\u0001"+
		"\u0000\u0000\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0094\u0015\u0001"+
		"\u0000\u0000\u0000\u0095\u0096\u0003\u0014\n\u0000\u0096\u0097\u0003\u0016"+
		"\u000b\u0000\u0097\u009a\u0001\u0000\u0000\u0000\u0098\u009a\u0001\u0000"+
		"\u0000\u0000\u0099\u0095\u0001\u0000\u0000\u0000\u0099\u0098\u0001\u0000"+
		"\u0000\u0000\u009a\u0017\u0001\u0000\u0000\u0000\u009b\u009c\u0005\u0011"+
		"\u0000\u0000\u009c\u009d\u0005\u000b\u0000\u0000\u009d\u009e\u0003\u001a"+
		"\r\u0000\u009e\u009f\u0003\u001c\u000e\u0000\u009f\u00a0\u0005\f\u0000"+
		"\u0000\u00a0\u00a1\u0005\u0002\u0000\u0000\u00a1\u0019\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a5\u0003&\u0013\u0000\u00a3\u00a5\u0005#\u0000\u0000\u00a4"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a5"+
		"\u001b\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\u0007\u0000\u0000\u00a7"+
		"\u00a8\u0003\u001a\r\u0000\u00a8\u00a9\u0003\u001c\u000e\u0000\u00a9\u00ac"+
		"\u0001\u0000\u0000\u0000\u00aa\u00ac\u0001\u0000\u0000\u0000\u00ab\u00a6"+
		"\u0001\u0000\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000\u0000\u00ac\u001d"+
		"\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\u0012\u0000\u0000\u00ae\u00af"+
		"\u0003\u0012\t\u0000\u00af\u00b0\u0005\u0013\u0000\u0000\u00b0\u00b1\u0005"+
		"\u000b\u0000\u0000\u00b1\u00b2\u0003&\u0013\u0000\u00b2\u00b3\u0005\f"+
		"\u0000\u0000\u00b3\u00b4\u0005\u0002\u0000\u0000\u00b4\u001f\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b6\u0005\u0014\u0000\u0000\u00b6\u00b7\u0005\u000b"+
		"\u0000\u0000\u00b7\u00b8\u0003&\u0013\u0000\u00b8\u00b9\u0005\f\u0000"+
		"\u0000\u00b9\u00ba\u0003\u0012\t\u0000\u00ba\u00bb\u0003\"\u0011\u0000"+
		"\u00bb\u00bc\u0005\u0002\u0000\u0000\u00bc!\u0001\u0000\u0000\u0000\u00bd"+
		"\u00be\u0005\u0015\u0000\u0000\u00be\u00c1\u0003\u0012\t\u0000\u00bf\u00c1"+
		"\u0001\u0000\u0000\u0000\u00c0\u00bd\u0001\u0000\u0000\u0000\u00c0\u00bf"+
		"\u0001\u0000\u0000\u0000\u00c1#\u0001\u0000\u0000\u0000\u00c2\u00c3\u0007"+
		"\u0001\u0000\u0000\u00c3%\u0001\u0000\u0000\u0000\u00c4\u00c5\u0003.\u0017"+
		"\u0000\u00c5\u00c6\u0003(\u0014\u0000\u00c6\'\u0001\u0000\u0000\u0000"+
		"\u00c7\u00c8\u0003*\u0015\u0000\u00c8\u00c9\u0003.\u0017\u0000\u00c9\u00cc"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cc\u0001\u0000\u0000\u0000\u00cb\u00c7"+
		"\u0001\u0000\u0000\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cc)\u0001"+
		"\u0000\u0000\u0000\u00cd\u00ce\u0007\u0002\u0000\u0000\u00ce+\u0001\u0000"+
		"\u0000\u0000\u00cf\u00d0\u0005\"\u0000\u0000\u00d0\u00d1\u0005\u0019\u0000"+
		"\u0000\u00d1\u00d2\u0003&\u0013\u0000\u00d2\u00d3\u0005\u0002\u0000\u0000"+
		"\u00d3-\u0001\u0000\u0000\u0000\u00d4\u00d5\u00034\u001a\u0000\u00d5\u00d6"+
		"\u00030\u0018\u0000\u00d6/\u0001\u0000\u0000\u0000\u00d7\u00d8\u00032"+
		"\u0019\u0000\u00d8\u00d9\u00034\u001a\u0000\u00d9\u00da\u00030\u0018\u0000"+
		"\u00da\u00dd\u0001\u0000\u0000\u0000\u00db\u00dd\u0001\u0000\u0000\u0000"+
		"\u00dc\u00d7\u0001\u0000\u0000\u0000\u00dc\u00db\u0001\u0000\u0000\u0000"+
		"\u00dd1\u0001\u0000\u0000\u0000\u00de\u00df\u0007\u0003\u0000\u0000\u00df"+
		"3\u0001\u0000\u0000\u0000\u00e0\u00e1\u0003:\u001d\u0000\u00e1\u00e2\u0003"+
		"6\u001b\u0000\u00e25\u0001\u0000\u0000\u0000\u00e3\u00e4\u00038\u001c"+
		"\u0000\u00e4\u00e5\u0003:\u001d\u0000\u00e5\u00e6\u00036\u001b\u0000\u00e6"+
		"\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e9\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e3\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000\u0000\u00e9"+
		"7\u0001\u0000\u0000\u0000\u00ea\u00eb\u0007\u0004\u0000\u0000\u00eb9\u0001"+
		"\u0000\u0000\u0000\u00ec\u00ed\u0005\u000b\u0000\u0000\u00ed\u00ee\u0003"+
		"&\u0013\u0000\u00ee\u00ef\u0005\f\u0000\u0000\u00ef\u00f2\u0001\u0000"+
		"\u0000\u0000\u00f0\u00f2\u0003<\u001e\u0000\u00f1\u00ec\u0001\u0000\u0000"+
		"\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000\u00f2;\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f4\u0003>\u001f\u0000\u00f4\u00f5\u0003@ \u0000\u00f5\u00f8"+
		"\u0001\u0000\u0000\u0000\u00f6\u00f8\u00032\u0019\u0000\u00f7\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f7\u00f6\u0001\u0000\u0000\u0000\u00f8=\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fc\u00032\u0019\u0000\u00fa\u00fc\u0001\u0000\u0000"+
		"\u0000\u00fb\u00f9\u0001\u0000\u0000\u0000\u00fb\u00fa\u0001\u0000\u0000"+
		"\u0000\u00fc?\u0001\u0000\u0000\u0000\u00fd\u0100\u0005\"\u0000\u0000"+
		"\u00fe\u0100\u0003$\u0012\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u00ff"+
		"\u00fe\u0001\u0000\u0000\u0000\u0100A\u0001\u0000\u0000\u0000\u0101\u0102"+
		"\u0005\"\u0000\u0000\u0102\u0103\u0005\u000b\u0000\u0000\u0103\u0104\u0003"+
		"D\"\u0000\u0104\u0105\u0005\f\u0000\u0000\u0105\u0106\u0005\u0002\u0000"+
		"\u0000\u0106C\u0001\u0000\u0000\u0000\u0107\u0108\u0003&\u0013\u0000\u0108"+
		"\u0109\u0003F#\u0000\u0109\u010c\u0001\u0000\u0000\u0000\u010a\u010c\u0001"+
		"\u0000\u0000\u0000\u010b\u0107\u0001\u0000\u0000\u0000\u010b\u010a\u0001"+
		"\u0000\u0000\u0000\u010cE\u0001\u0000\u0000\u0000\u010d\u010e\u0005\u0007"+
		"\u0000\u0000\u010e\u0111\u0003D\"\u0000\u010f\u0111\u0001\u0000\u0000"+
		"\u0000\u0110\u010d\u0001\u0000\u0000\u0000\u0110\u010f\u0001\u0000\u0000"+
		"\u0000\u0111G\u0001\u0000\u0000\u0000\u0014Zbk{\u0083\u0088\u0093\u0099"+
		"\u00a4\u00ab\u00c0\u00cb\u00dc\u00e8\u00f1\u00f7\u00fb\u00ff\u010b\u0110";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}