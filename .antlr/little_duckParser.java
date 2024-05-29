// Generated from c:/Users/josec/OneDrive/Documentos/GitHub/Little_duck/little_duck.g4 by ANTLR 4.13.1

from Interventions import *

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
		RULE_pm_const = 32, RULE_ic = 33, RULE_f_call = 34, RULE_f_call_prime = 35, 
		RULE_l_f_call_prime = 36;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "vars", "vars_prime", "vars_prime_prime", "l_vars", "type", 
			"funcs", "funcs_prime", "funcs_prime_prime", "body", "statement", "l_statement", 
			"print", "print_prime", "l_print", "cycle", "condition", "condition_prime", 
			"cte", "expression", "expression_prime", "oper", "assign", "exp", "l_exp", 
			"pm", "termino", "l_termino", "ad", "factor", "factor_prime", "b_factor", 
			"pm_const", "ic", "f_call", "f_call_prime", "l_f_call_prime"
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
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__0);
			setState(75);
			match(ID);
			setState(76);
			match(T__1);
			inter.setVariableScope('global')
			setState(78);
			vars();
			setState(79);
			funcs();
			setState(80);
			match(T__2);
			inter.setMainQuad()
			setState(82);
			body();
			setState(83);
			match(T__3);
			setState(84);
			match(EOF);
			inter.endQuad()
			inter.printGlobal()
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
		public TypeContext type;
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
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vars);
		try {
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				match(T__4);
				setState(89);
				vars_prime();
				setState(90);
				match(T__5);
				setState(91);
				((VarsContext)_localctx).type = type();
				inter.setTypes((((VarsContext)_localctx).type!=null?_input.getText(((VarsContext)_localctx).type.start,((VarsContext)_localctx).type.stop):null))
				setState(93);
				match(T__1);
				setState(94);
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
		public Token ID;
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public Vars_prime_primeContext vars_prime_prime() {
			return getRuleContext(Vars_prime_primeContext.class,0);
		}
		public Vars_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_prime; }
	}

	public final Vars_primeContext vars_prime() throws RecognitionException {
		Vars_primeContext _localctx = new Vars_primeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars_prime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			((Vars_primeContext)_localctx).ID = match(ID);
			inter.addVariable((((Vars_primeContext)_localctx).ID!=null?((Vars_primeContext)_localctx).ID.getText():null), (((Vars_primeContext)_localctx).ID!=null?((Vars_primeContext)_localctx).ID.getLine():0))
			setState(101);
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
	}

	public final Vars_prime_primeContext vars_prime_prime() throws RecognitionException {
		Vars_prime_primeContext _localctx = new Vars_prime_primeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vars_prime_prime);
		try {
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				match(T__6);
				setState(104);
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
		public TypeContext type;
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
	}

	public final L_varsContext l_vars() throws RecognitionException {
		L_varsContext _localctx = new L_varsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_l_vars);
		try {
			setState(116);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				vars_prime();
				setState(109);
				match(T__5);
				setState(110);
				((L_varsContext)_localctx).type = type();
				setState(111);
				match(T__1);
				setState(112);
				l_vars();
				inter.setTypes((((L_varsContext)_localctx).type!=null?_input.getText(((L_varsContext)_localctx).type.start,((L_varsContext)_localctx).type.stop):null))
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
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
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
		public Token ID;
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
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcs);
		try {
			setState(137);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				match(T__9);
				setState(121);
				((FuncsContext)_localctx).ID = match(ID);
				inter.funcStart()
				inter.setVariableScope((((FuncsContext)_localctx).ID!=null?((FuncsContext)_localctx).ID.getText():null))
				setState(124);
				match(T__10);
				setState(125);
				funcs_prime();
				setState(126);
				match(T__11);
				setState(127);
				match(T__12);
				setState(128);
				vars();
				setState(129);
				body();
				setState(130);
				match(T__13);
				setState(131);
				match(T__1);
				inter.setVariableScope('global')
				inter.endFunc((((FuncsContext)_localctx).ID!=null?((FuncsContext)_localctx).ID.getText():null))
				setState(134);
				funcs();
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
		public Token ID;
		public TypeContext type;
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
	}

	public final Funcs_primeContext funcs_prime() throws RecognitionException {
		Funcs_primeContext _localctx = new Funcs_primeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_funcs_prime);
		try {
			setState(148);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				((Funcs_primeContext)_localctx).ID = match(ID);
				inter.addVariable((((Funcs_primeContext)_localctx).ID!=null?((Funcs_primeContext)_localctx).ID.getText():null), (((Funcs_primeContext)_localctx).ID!=null?((Funcs_primeContext)_localctx).ID.getLine():0))
				setState(141);
				match(T__5);
				setState(142);
				((Funcs_primeContext)_localctx).type = type();
				inter.setTypes((((Funcs_primeContext)_localctx).type!=null?_input.getText(((Funcs_primeContext)_localctx).type.start,((Funcs_primeContext)_localctx).type.stop):null))
				inter.countParams()
				setState(145);
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
	}

	public final Funcs_prime_primeContext funcs_prime_prime() throws RecognitionException {
		Funcs_prime_primeContext _localctx = new Funcs_prime_primeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_funcs_prime_prime);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(T__6);
				setState(151);
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
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(T__14);
			setState(156);
			l_statement();
			setState(157);
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
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		try {
			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(161);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(162);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(163);
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
	}

	public final L_statementContext l_statement() throws RecognitionException {
		L_statementContext _localctx = new L_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_l_statement);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__16:
			case T__17:
			case T__19:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				statement();
				setState(167);
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
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(T__16);
			inter.keyPoint_OperationPush('PRINT')
			setState(174);
			match(T__10);
			setState(175);
			print_prime();
			setState(176);
			l_print();
			setState(177);
			match(T__11);
			setState(178);
			match(T__1);
			inter.keyPoint_CreateQuad(4)
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
		public Token STRING;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(little_duckParser.STRING, 0); }
		public Print_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_prime; }
	}

	public final Print_primeContext print_prime() throws RecognitionException {
		Print_primeContext _localctx = new Print_primeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_print_prime);
		try {
			setState(184);
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
				setState(181);
				expression();
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(182);
				((Print_primeContext)_localctx).STRING = match(STRING);
				inter.keyPoint_1((((Print_primeContext)_localctx).STRING!=null?((Print_primeContext)_localctx).STRING.getText():null), (((Print_primeContext)_localctx).STRING!=null?((Print_primeContext)_localctx).STRING.getType():0))
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
	}

	public final L_printContext l_print() throws RecognitionException {
		L_printContext _localctx = new L_printContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_l_print);
		try {
			setState(193);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				match(T__6);
				inter.keyPoint_OperationPush(',')
				setState(188);
				print_prime();
				inter.keyPoint_CreateQuad(3)
				setState(190);
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
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(T__17);
			inter.whileKeyOne()
			setState(197);
			body();
			setState(198);
			match(T__18);
			setState(199);
			match(T__10);
			setState(200);
			expression();
			setState(201);
			match(T__11);
			setState(202);
			match(T__1);
			inter.endWhile()
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
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(T__19);
			setState(206);
			match(T__10);
			setState(207);
			expression();
			setState(208);
			match(T__11);
			inter.createGoToF()
			setState(210);
			body();
			setState(211);
			condition_prime();
			setState(212);
			match(T__1);
			inter.if_Fill()
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
	}

	public final Condition_primeContext condition_prime() throws RecognitionException {
		Condition_primeContext _localctx = new Condition_primeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_condition_prime);
		try {
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				match(T__20);
				inter.else_Fill()
				setState(217);
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
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
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
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			exp();
			setState(224);
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
		public OperContext oper;
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
	}

	public final Expression_primeContext expression_prime() throws RecognitionException {
		Expression_primeContext _localctx = new Expression_primeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expression_prime);
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
			case T__22:
			case T__23:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				((Expression_primeContext)_localctx).oper = oper();
				inter.keyPoint_OperationPush((((Expression_primeContext)_localctx).oper!=null?_input.getText(((Expression_primeContext)_localctx).oper.start,((Expression_primeContext)_localctx).oper.stop):null))
				setState(228);
				exp();
				inter.keyPoint_CreateQuad(2)
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
	}

	public final OperContext oper() throws RecognitionException {
		OperContext _localctx = new OperContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_oper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
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
		public Token ID;
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			((AssignContext)_localctx).ID = match(ID);
			inter.isNotDefined((((AssignContext)_localctx).ID!=null?((AssignContext)_localctx).ID.getText():null), (((AssignContext)_localctx).ID!=null?((AssignContext)_localctx).ID.getLine():0))
			inter.keyPoint_1((((AssignContext)_localctx).ID!=null?((AssignContext)_localctx).ID.getText():null))
			setState(239);
			match(T__24);
			inter.keyPoint_OperationPush('=')
			setState(241);
			expression();
			setState(242);
			match(T__1);
			inter.keyPoint_CreateQuad(3)
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
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			termino();
			inter.keyPoint_CreateQuad(0)
			setState(247);
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
		public PmContext pm;
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
	}

	public final L_expContext l_exp() throws RecognitionException {
		L_expContext _localctx = new L_expContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_l_exp);
		try {
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(249);
				((L_expContext)_localctx).pm = pm();
				inter.keyPoint_OperationPush((((L_expContext)_localctx).pm!=null?_input.getText(((L_expContext)_localctx).pm.start,((L_expContext)_localctx).pm.stop):null))
				setState(251);
				termino();
				inter.keyPoint_CreateQuad(0)
				setState(253);
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
	}

	public final PmContext pm() throws RecognitionException {
		PmContext _localctx = new PmContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_pm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
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
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			factor();
			inter.keyPoint_CreateQuad(1)
			setState(262);
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
		public AdContext ad;
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
	}

	public final L_terminoContext l_termino() throws RecognitionException {
		L_terminoContext _localctx = new L_terminoContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_l_termino);
		try {
			setState(271);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 1);
				{
				setState(264);
				((L_terminoContext)_localctx).ad = ad();
				inter.keyPoint_OperationPush((((L_terminoContext)_localctx).ad!=null?_input.getText(((L_terminoContext)_localctx).ad.start,((L_terminoContext)_localctx).ad.stop):null))
				setState(266);
				factor();
				inter.keyPoint_CreateQuad(1)
				setState(268);
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
	}

	public final AdContext ad() throws RecognitionException {
		AdContext _localctx = new AdContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_ad);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
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
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_factor);
		try {
			setState(282);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(275);
				match(T__10);
				inter.keyPoint_PushBottom()
				setState(277);
				expression();
				setState(278);
				match(T__11);
				inter.keyPoint_PopFalse()
				}
				break;
			case T__25:
			case T__26:
			case INT:
			case FLOAT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(281);
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
		public Factor_primeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_prime; }
	}

	public final Factor_primeContext factor_prime() throws RecognitionException {
		Factor_primeContext _localctx = new Factor_primeContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_factor_prime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			b_factor();
			setState(285);
			ic();
			# removed | pm
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
		public Pm_constContext pm_const() {
			return getRuleContext(Pm_constContext.class,0);
		}
		public B_factorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_b_factor; }
	}

	public final B_factorContext b_factor() throws RecognitionException {
		B_factorContext _localctx = new B_factorContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_b_factor);
		try {
			setState(290);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				pm_const();
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
	public static class Pm_constContext extends ParserRuleContext {
		public Pm_constContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pm_const; }
	}

	public final Pm_constContext pm_const() throws RecognitionException {
		Pm_constContext _localctx = new Pm_constContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_pm_const);
		try {
			setState(295);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				match(T__25);
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				match(T__26);
				inter.setMinusOne()
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
		public Token ID;
		public CteContext cte;
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public IcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ic; }
	}

	public final IcContext ic() throws RecognitionException {
		IcContext _localctx = new IcContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_ic);
		try {
			setState(304);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				((IcContext)_localctx).ID = match(ID);
				inter.isNotDefined((((IcContext)_localctx).ID!=null?((IcContext)_localctx).ID.getText():null), (((IcContext)_localctx).ID!=null?((IcContext)_localctx).ID.getLine():0))
				inter.keyPoint_1((((IcContext)_localctx).ID!=null?((IcContext)_localctx).ID.getText():null))
				}
				break;
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(300);
				((IcContext)_localctx).cte = cte();
				inter.keyPoint_1((((IcContext)_localctx).cte!=null?_input.getText(((IcContext)_localctx).cte.start,((IcContext)_localctx).cte.stop):null), (((IcContext)_localctx).cte!=null?(((IcContext)_localctx).cte.stop):null).type)
				# This rule chesk if this is ID or Constant
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
		public Token ID;
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public F_call_primeContext f_call_prime() {
			return getRuleContext(F_call_primeContext.class,0);
		}
		public F_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call; }
	}

	public final F_callContext f_call() throws RecognitionException {
		F_callContext _localctx = new F_callContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_f_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			((F_callContext)_localctx).ID = match(ID);
			inter.keyPoint_OperationPush('gosub')
			setState(308);
			match(T__10);
			setState(309);
			f_call_prime();
			setState(310);
			match(T__11);
			setState(311);
			match(T__1);
			inter.keyPoint_CreateQuad(4, (((F_callContext)_localctx).ID!=null?((F_callContext)_localctx).ID.getText():null))
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
	}

	public final F_call_primeContext f_call_prime() throws RecognitionException {
		F_call_primeContext _localctx = new F_call_primeContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_f_call_prime);
		try {
			setState(318);
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
				setState(314);
				expression();
				setState(315);
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
	}

	public final L_f_call_primeContext l_f_call_prime() throws RecognitionException {
		L_f_call_primeContext _localctx = new L_f_call_primeContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_l_f_call_prime);
		try {
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(320);
				match(T__6);
				inter.keyPoint_OperationPush('param')
				setState(322);
				f_call_prime();
				inter.keyPoint_CreateQuad(4)
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
		"\u0004\u0001#\u0149\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001b\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003k\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004u\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u008a\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0095\b\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0003\b\u009a\b\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00a5\b\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00ab\b\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u00b9\b\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00c2\b\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0003\u0011\u00dc\b\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u00e9\b\u0014\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0003\u0018\u0101\b\u0018\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0110\b\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u011b\b\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0003\u001f"+
		"\u0123\b\u001f\u0001 \u0001 \u0001 \u0003 \u0128\b \u0001!\u0001!\u0001"+
		"!\u0001!\u0001!\u0001!\u0001!\u0003!\u0131\b!\u0001\"\u0001\"\u0001\""+
		"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001#\u0003"+
		"#\u013f\b#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0003$\u0147\b$\u0001"+
		"$\u0000\u0000%\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFH\u0000\u0005\u0001\u0000"+
		"\b\t\u0001\u0000 !\u0001\u0000\u0016\u0018\u0001\u0000\u001a\u001b\u0001"+
		"\u0000\u001c\u001d\u013a\u0000J\u0001\u0000\u0000\u0000\u0002a\u0001\u0000"+
		"\u0000\u0000\u0004c\u0001\u0000\u0000\u0000\u0006j\u0001\u0000\u0000\u0000"+
		"\bt\u0001\u0000\u0000\u0000\nv\u0001\u0000\u0000\u0000\f\u0089\u0001\u0000"+
		"\u0000\u0000\u000e\u0094\u0001\u0000\u0000\u0000\u0010\u0099\u0001\u0000"+
		"\u0000\u0000\u0012\u009b\u0001\u0000\u0000\u0000\u0014\u00a4\u0001\u0000"+
		"\u0000\u0000\u0016\u00aa\u0001\u0000\u0000\u0000\u0018\u00ac\u0001\u0000"+
		"\u0000\u0000\u001a\u00b8\u0001\u0000\u0000\u0000\u001c\u00c1\u0001\u0000"+
		"\u0000\u0000\u001e\u00c3\u0001\u0000\u0000\u0000 \u00cd\u0001\u0000\u0000"+
		"\u0000\"\u00db\u0001\u0000\u0000\u0000$\u00dd\u0001\u0000\u0000\u0000"+
		"&\u00df\u0001\u0000\u0000\u0000(\u00e8\u0001\u0000\u0000\u0000*\u00ea"+
		"\u0001\u0000\u0000\u0000,\u00ec\u0001\u0000\u0000\u0000.\u00f5\u0001\u0000"+
		"\u0000\u00000\u0100\u0001\u0000\u0000\u00002\u0102\u0001\u0000\u0000\u0000"+
		"4\u0104\u0001\u0000\u0000\u00006\u010f\u0001\u0000\u0000\u00008\u0111"+
		"\u0001\u0000\u0000\u0000:\u011a\u0001\u0000\u0000\u0000<\u011c\u0001\u0000"+
		"\u0000\u0000>\u0122\u0001\u0000\u0000\u0000@\u0127\u0001\u0000\u0000\u0000"+
		"B\u0130\u0001\u0000\u0000\u0000D\u0132\u0001\u0000\u0000\u0000F\u013e"+
		"\u0001\u0000\u0000\u0000H\u0146\u0001\u0000\u0000\u0000JK\u0005\u0001"+
		"\u0000\u0000KL\u0005\"\u0000\u0000LM\u0005\u0002\u0000\u0000MN\u0006\u0000"+
		"\uffff\uffff\u0000NO\u0003\u0002\u0001\u0000OP\u0003\f\u0006\u0000PQ\u0005"+
		"\u0003\u0000\u0000QR\u0006\u0000\uffff\uffff\u0000RS\u0003\u0012\t\u0000"+
		"ST\u0005\u0004\u0000\u0000TU\u0005\u0000\u0000\u0001UV\u0006\u0000\uffff"+
		"\uffff\u0000VW\u0006\u0000\uffff\uffff\u0000W\u0001\u0001\u0000\u0000"+
		"\u0000XY\u0005\u0005\u0000\u0000YZ\u0003\u0004\u0002\u0000Z[\u0005\u0006"+
		"\u0000\u0000[\\\u0003\n\u0005\u0000\\]\u0006\u0001\uffff\uffff\u0000]"+
		"^\u0005\u0002\u0000\u0000^_\u0003\b\u0004\u0000_b\u0001\u0000\u0000\u0000"+
		"`b\u0001\u0000\u0000\u0000aX\u0001\u0000\u0000\u0000a`\u0001\u0000\u0000"+
		"\u0000b\u0003\u0001\u0000\u0000\u0000cd\u0005\"\u0000\u0000de\u0006\u0002"+
		"\uffff\uffff\u0000ef\u0003\u0006\u0003\u0000f\u0005\u0001\u0000\u0000"+
		"\u0000gh\u0005\u0007\u0000\u0000hk\u0003\u0004\u0002\u0000ik\u0001\u0000"+
		"\u0000\u0000jg\u0001\u0000\u0000\u0000ji\u0001\u0000\u0000\u0000k\u0007"+
		"\u0001\u0000\u0000\u0000lm\u0003\u0004\u0002\u0000mn\u0005\u0006\u0000"+
		"\u0000no\u0003\n\u0005\u0000op\u0005\u0002\u0000\u0000pq\u0003\b\u0004"+
		"\u0000qr\u0006\u0004\uffff\uffff\u0000ru\u0001\u0000\u0000\u0000su\u0001"+
		"\u0000\u0000\u0000tl\u0001\u0000\u0000\u0000ts\u0001\u0000\u0000\u0000"+
		"u\t\u0001\u0000\u0000\u0000vw\u0007\u0000\u0000\u0000w\u000b\u0001\u0000"+
		"\u0000\u0000xy\u0005\n\u0000\u0000yz\u0005\"\u0000\u0000z{\u0006\u0006"+
		"\uffff\uffff\u0000{|\u0006\u0006\uffff\uffff\u0000|}\u0005\u000b\u0000"+
		"\u0000}~\u0003\u000e\u0007\u0000~\u007f\u0005\f\u0000\u0000\u007f\u0080"+
		"\u0005\r\u0000\u0000\u0080\u0081\u0003\u0002\u0001\u0000\u0081\u0082\u0003"+
		"\u0012\t\u0000\u0082\u0083\u0005\u000e\u0000\u0000\u0083\u0084\u0005\u0002"+
		"\u0000\u0000\u0084\u0085\u0006\u0006\uffff\uffff\u0000\u0085\u0086\u0006"+
		"\u0006\uffff\uffff\u0000\u0086\u0087\u0003\f\u0006\u0000\u0087\u008a\u0001"+
		"\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089x\u0001\u0000"+
		"\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a\r\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0005\"\u0000\u0000\u008c\u008d\u0006\u0007\uffff\uffff"+
		"\u0000\u008d\u008e\u0005\u0006\u0000\u0000\u008e\u008f\u0003\n\u0005\u0000"+
		"\u008f\u0090\u0006\u0007\uffff\uffff\u0000\u0090\u0091\u0006\u0007\uffff"+
		"\uffff\u0000\u0091\u0092\u0003\u0010\b\u0000\u0092\u0095\u0001\u0000\u0000"+
		"\u0000\u0093\u0095\u0001\u0000\u0000\u0000\u0094\u008b\u0001\u0000\u0000"+
		"\u0000\u0094\u0093\u0001\u0000\u0000\u0000\u0095\u000f\u0001\u0000\u0000"+
		"\u0000\u0096\u0097\u0005\u0007\u0000\u0000\u0097\u009a\u0003\u000e\u0007"+
		"\u0000\u0098\u009a\u0001\u0000\u0000\u0000\u0099\u0096\u0001\u0000\u0000"+
		"\u0000\u0099\u0098\u0001\u0000\u0000\u0000\u009a\u0011\u0001\u0000\u0000"+
		"\u0000\u009b\u009c\u0005\u000f\u0000\u0000\u009c\u009d\u0003\u0016\u000b"+
		"\u0000\u009d\u009e\u0005\u0010\u0000\u0000\u009e\u0013\u0001\u0000\u0000"+
		"\u0000\u009f\u00a5\u0003,\u0016\u0000\u00a0\u00a5\u0003 \u0010\u0000\u00a1"+
		"\u00a5\u0003\u001e\u000f\u0000\u00a2\u00a5\u0003D\"\u0000\u00a3\u00a5"+
		"\u0003\u0018\f\u0000\u00a4\u009f\u0001\u0000\u0000\u0000\u00a4\u00a0\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a5\u0015\u0001"+
		"\u0000\u0000\u0000\u00a6\u00a7\u0003\u0014\n\u0000\u00a7\u00a8\u0003\u0016"+
		"\u000b\u0000\u00a8\u00ab\u0001\u0000\u0000\u0000\u00a9\u00ab\u0001\u0000"+
		"\u0000\u0000\u00aa\u00a6\u0001\u0000\u0000\u0000\u00aa\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ab\u0017\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\u0011"+
		"\u0000\u0000\u00ad\u00ae\u0006\f\uffff\uffff\u0000\u00ae\u00af\u0005\u000b"+
		"\u0000\u0000\u00af\u00b0\u0003\u001a\r\u0000\u00b0\u00b1\u0003\u001c\u000e"+
		"\u0000\u00b1\u00b2\u0005\f\u0000\u0000\u00b2\u00b3\u0005\u0002\u0000\u0000"+
		"\u00b3\u00b4\u0006\f\uffff\uffff\u0000\u00b4\u0019\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b9\u0003&\u0013\u0000\u00b6\u00b7\u0005#\u0000\u0000\u00b7\u00b9"+
		"\u0006\r\uffff\uffff\u0000\u00b8\u00b5\u0001\u0000\u0000\u0000\u00b8\u00b6"+
		"\u0001\u0000\u0000\u0000\u00b9\u001b\u0001\u0000\u0000\u0000\u00ba\u00bb"+
		"\u0005\u0007\u0000\u0000\u00bb\u00bc\u0006\u000e\uffff\uffff\u0000\u00bc"+
		"\u00bd\u0003\u001a\r\u0000\u00bd\u00be\u0006\u000e\uffff\uffff\u0000\u00be"+
		"\u00bf\u0003\u001c\u000e\u0000\u00bf\u00c2\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c2\u0001\u0000\u0000\u0000\u00c1\u00ba\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c2\u001d\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c4\u0005\u0012\u0000\u0000\u00c4\u00c5\u0006\u000f\uffff\uffff\u0000"+
		"\u00c5\u00c6\u0003\u0012\t\u0000\u00c6\u00c7\u0005\u0013\u0000\u0000\u00c7"+
		"\u00c8\u0005\u000b\u0000\u0000\u00c8\u00c9\u0003&\u0013\u0000\u00c9\u00ca"+
		"\u0005\f\u0000\u0000\u00ca\u00cb\u0005\u0002\u0000\u0000\u00cb\u00cc\u0006"+
		"\u000f\uffff\uffff\u0000\u00cc\u001f\u0001\u0000\u0000\u0000\u00cd\u00ce"+
		"\u0005\u0014\u0000\u0000\u00ce\u00cf\u0005\u000b\u0000\u0000\u00cf\u00d0"+
		"\u0003&\u0013\u0000\u00d0\u00d1\u0005\f\u0000\u0000\u00d1\u00d2\u0006"+
		"\u0010\uffff\uffff\u0000\u00d2\u00d3\u0003\u0012\t\u0000\u00d3\u00d4\u0003"+
		"\"\u0011\u0000\u00d4\u00d5\u0005\u0002\u0000\u0000\u00d5\u00d6\u0006\u0010"+
		"\uffff\uffff\u0000\u00d6!\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005\u0015"+
		"\u0000\u0000\u00d8\u00d9\u0006\u0011\uffff\uffff\u0000\u00d9\u00dc\u0003"+
		"\u0012\t\u0000\u00da\u00dc\u0001\u0000\u0000\u0000\u00db\u00d7\u0001\u0000"+
		"\u0000\u0000\u00db\u00da\u0001\u0000\u0000\u0000\u00dc#\u0001\u0000\u0000"+
		"\u0000\u00dd\u00de\u0007\u0001\u0000\u0000\u00de%\u0001\u0000\u0000\u0000"+
		"\u00df\u00e0\u0003.\u0017\u0000\u00e0\u00e1\u0003(\u0014\u0000\u00e1\'"+
		"\u0001\u0000\u0000\u0000\u00e2\u00e3\u0003*\u0015\u0000\u00e3\u00e4\u0006"+
		"\u0014\uffff\uffff\u0000\u00e4\u00e5\u0003.\u0017\u0000\u00e5\u00e6\u0006"+
		"\u0014\uffff\uffff\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e9"+
		"\u0001\u0000\u0000\u0000\u00e8\u00e2\u0001\u0000\u0000\u0000\u00e8\u00e7"+
		"\u0001\u0000\u0000\u0000\u00e9)\u0001\u0000\u0000\u0000\u00ea\u00eb\u0007"+
		"\u0002\u0000\u0000\u00eb+\u0001\u0000\u0000\u0000\u00ec\u00ed\u0005\""+
		"\u0000\u0000\u00ed\u00ee\u0006\u0016\uffff\uffff\u0000\u00ee\u00ef\u0006"+
		"\u0016\uffff\uffff\u0000\u00ef\u00f0\u0005\u0019\u0000\u0000\u00f0\u00f1"+
		"\u0006\u0016\uffff\uffff\u0000\u00f1\u00f2\u0003&\u0013\u0000\u00f2\u00f3"+
		"\u0005\u0002\u0000\u0000\u00f3\u00f4\u0006\u0016\uffff\uffff\u0000\u00f4"+
		"-\u0001\u0000\u0000\u0000\u00f5\u00f6\u00034\u001a\u0000\u00f6\u00f7\u0006"+
		"\u0017\uffff\uffff\u0000\u00f7\u00f8\u00030\u0018\u0000\u00f8/\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fa\u00032\u0019\u0000\u00fa\u00fb\u0006\u0018\uffff"+
		"\uffff\u0000\u00fb\u00fc\u00034\u001a\u0000\u00fc\u00fd\u0006\u0018\uffff"+
		"\uffff\u0000\u00fd\u00fe\u00030\u0018\u0000\u00fe\u0101\u0001\u0000\u0000"+
		"\u0000\u00ff\u0101\u0001\u0000\u0000\u0000\u0100\u00f9\u0001\u0000\u0000"+
		"\u0000\u0100\u00ff\u0001\u0000\u0000\u0000\u01011\u0001\u0000\u0000\u0000"+
		"\u0102\u0103\u0007\u0003\u0000\u0000\u01033\u0001\u0000\u0000\u0000\u0104"+
		"\u0105\u0003:\u001d\u0000\u0105\u0106\u0006\u001a\uffff\uffff\u0000\u0106"+
		"\u0107\u00036\u001b\u0000\u01075\u0001\u0000\u0000\u0000\u0108\u0109\u0003"+
		"8\u001c\u0000\u0109\u010a\u0006\u001b\uffff\uffff\u0000\u010a\u010b\u0003"+
		":\u001d\u0000\u010b\u010c\u0006\u001b\uffff\uffff\u0000\u010c\u010d\u0003"+
		"6\u001b\u0000\u010d\u0110\u0001\u0000\u0000\u0000\u010e\u0110\u0001\u0000"+
		"\u0000\u0000\u010f\u0108\u0001\u0000\u0000\u0000\u010f\u010e\u0001\u0000"+
		"\u0000\u0000\u01107\u0001\u0000\u0000\u0000\u0111\u0112\u0007\u0004\u0000"+
		"\u0000\u01129\u0001\u0000\u0000\u0000\u0113\u0114\u0005\u000b\u0000\u0000"+
		"\u0114\u0115\u0006\u001d\uffff\uffff\u0000\u0115\u0116\u0003&\u0013\u0000"+
		"\u0116\u0117\u0005\f\u0000\u0000\u0117\u0118\u0006\u001d\uffff\uffff\u0000"+
		"\u0118\u011b\u0001\u0000\u0000\u0000\u0119\u011b\u0003<\u001e\u0000\u011a"+
		"\u0113\u0001\u0000\u0000\u0000\u011a\u0119\u0001\u0000\u0000\u0000\u011b"+
		";\u0001\u0000\u0000\u0000\u011c\u011d\u0003>\u001f\u0000\u011d\u011e\u0003"+
		"B!\u0000\u011e\u011f\u0006\u001e\uffff\uffff\u0000\u011f=\u0001\u0000"+
		"\u0000\u0000\u0120\u0123\u0003@ \u0000\u0121\u0123\u0001\u0000\u0000\u0000"+
		"\u0122\u0120\u0001\u0000\u0000\u0000\u0122\u0121\u0001\u0000\u0000\u0000"+
		"\u0123?\u0001\u0000\u0000\u0000\u0124\u0128\u0005\u001a\u0000\u0000\u0125"+
		"\u0126\u0005\u001b\u0000\u0000\u0126\u0128\u0006 \uffff\uffff\u0000\u0127"+
		"\u0124\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000\u0000\u0128"+
		"A\u0001\u0000\u0000\u0000\u0129\u012a\u0005\"\u0000\u0000\u012a\u012b"+
		"\u0006!\uffff\uffff\u0000\u012b\u0131\u0006!\uffff\uffff\u0000\u012c\u012d"+
		"\u0003$\u0012\u0000\u012d\u012e\u0006!\uffff\uffff\u0000\u012e\u012f\u0006"+
		"!\uffff\uffff\u0000\u012f\u0131\u0001\u0000\u0000\u0000\u0130\u0129\u0001"+
		"\u0000\u0000\u0000\u0130\u012c\u0001\u0000\u0000\u0000\u0131C\u0001\u0000"+
		"\u0000\u0000\u0132\u0133\u0005\"\u0000\u0000\u0133\u0134\u0006\"\uffff"+
		"\uffff\u0000\u0134\u0135\u0005\u000b\u0000\u0000\u0135\u0136\u0003F#\u0000"+
		"\u0136\u0137\u0005\f\u0000\u0000\u0137\u0138\u0005\u0002\u0000\u0000\u0138"+
		"\u0139\u0006\"\uffff\uffff\u0000\u0139E\u0001\u0000\u0000\u0000\u013a"+
		"\u013b\u0003&\u0013\u0000\u013b\u013c\u0003H$\u0000\u013c\u013f\u0001"+
		"\u0000\u0000\u0000\u013d\u013f\u0001\u0000\u0000\u0000\u013e\u013a\u0001"+
		"\u0000\u0000\u0000\u013e\u013d\u0001\u0000\u0000\u0000\u013fG\u0001\u0000"+
		"\u0000\u0000\u0140\u0141\u0005\u0007\u0000\u0000\u0141\u0142\u0006$\uffff"+
		"\uffff\u0000\u0142\u0143\u0003F#\u0000\u0143\u0144\u0006$\uffff\uffff"+
		"\u0000\u0144\u0147\u0001\u0000\u0000\u0000\u0145\u0147\u0001\u0000\u0000"+
		"\u0000\u0146\u0140\u0001\u0000\u0000\u0000\u0146\u0145\u0001\u0000\u0000"+
		"\u0000\u0147I\u0001\u0000\u0000\u0000\u0014ajt\u0089\u0094\u0099\u00a4"+
		"\u00aa\u00b8\u00c1\u00db\u00e8\u0100\u010f\u011a\u0122\u0127\u0130\u013e"+
		"\u0146";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}