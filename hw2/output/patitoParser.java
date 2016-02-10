// $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 12:53:33

import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

import org.antlr.runtime.debug.*;
import java.io.IOException;
@SuppressWarnings("all")
public class patitoParser extends DebugParser {
	public static final String[] tokenNames = new String[] {
		"<invalid>", "<EOR>", "<DOWN>", "<UP>", "ESC_SEQ", "EXPONENT", "FLOAT", 
		"HEX_DIGIT", "ID", "INT", "OCTAL_ESC", "STRING", "UNICODE_ESC", "WS", 
		"'('", "')'", "'*'", "'+'", "','", "'-'", "'/'", "':'", "';'", "'<'", 
		"'<>'", "'>'", "'float'", "'int'", "'print'", "'var'"
	};
	public static final int EOF=-1;
	public static final int T__14=14;
	public static final int T__15=15;
	public static final int T__16=16;
	public static final int T__17=17;
	public static final int T__18=18;
	public static final int T__19=19;
	public static final int T__20=20;
	public static final int T__21=21;
	public static final int T__22=22;
	public static final int T__23=23;
	public static final int T__24=24;
	public static final int T__25=25;
	public static final int T__26=26;
	public static final int T__27=27;
	public static final int T__28=28;
	public static final int T__29=29;
	public static final int ESC_SEQ=4;
	public static final int EXPONENT=5;
	public static final int FLOAT=6;
	public static final int HEX_DIGIT=7;
	public static final int ID=8;
	public static final int INT=9;
	public static final int OCTAL_ESC=10;
	public static final int STRING=11;
	public static final int UNICODE_ESC=12;
	public static final int WS=13;

	// delegates
	public Parser[] getDelegates() {
		return new Parser[] {};
	}

	// delegators


	public static final String[] ruleNames = new String[] {
		"invalidRule", "opmul", "exp", "factor", "varcte", "strgstmt", "expresion", 
		"termino", "decl", "vars", "variabs", "tipo", "stmt", "stmt2", "opexp", 
		"opsum", "escritura", "parse", "more"
	};

	public static final boolean[] decisionCanBacktrack = new boolean[] {
		false, // invalid decision
		false, false, false, false, false, false, false, false, false
	};

 
	public int ruleLevel = 0;
	public int getRuleLevel() { return ruleLevel; }
	public void incRuleLevel() { ruleLevel++; }
	public void decRuleLevel() { ruleLevel--; }
	public patitoParser(TokenStream input) {
		this(input, DebugEventSocketProxy.DEFAULT_DEBUGGER_PORT, new RecognizerSharedState());
	}
	public patitoParser(TokenStream input, int port, RecognizerSharedState state) {
		super(input, state);
		DebugEventSocketProxy proxy =
			new DebugEventSocketProxy(this, port, null);

		setDebugListener(proxy);
		try {
			proxy.handshake();
		}
		catch (IOException ioe) {
			reportError(ioe);
		}
	}

	public patitoParser(TokenStream input, DebugEventListener dbg) {
		super(input, dbg, new RecognizerSharedState());
	}

	protected boolean evalPredicate(boolean result, String predicate) {
		dbg.semanticPredicate(result, predicate);
		return result;
	}

	@Override public String[] getTokenNames() { return patitoParser.tokenNames; }
	@Override public String getGrammarFileName() { return "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"; }



	// $ANTLR start "parse"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:1: parse : tipo EOF ;
	public final void parse() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "parse");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(3, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:7: ( tipo EOF )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:9: tipo EOF
			{
			dbg.location(3,9);
			pushFollow(FOLLOW_tipo_in_parse10);
			tipo();
			state._fsp--;
			dbg.location(3,14);
			match(input,EOF,FOLLOW_EOF_in_parse12); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(3, 16);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "parse");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "parse"



	// $ANTLR start "escritura"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:6:1: escritura : 'print' '(' stmt ')' ';' ;
	public final void escritura() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "escritura");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(6, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:2: ( 'print' '(' stmt ')' ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:4: 'print' '(' stmt ')' ';'
			{
			dbg.location(7,4);
			match(input,28,FOLLOW_28_in_escritura22); dbg.location(7,12);
			match(input,14,FOLLOW_14_in_escritura24); dbg.location(7,16);
			pushFollow(FOLLOW_stmt_in_escritura26);
			stmt();
			state._fsp--;
			dbg.location(7,21);
			match(input,15,FOLLOW_15_in_escritura28); dbg.location(7,25);
			match(input,22,FOLLOW_22_in_escritura30); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(7, 27);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "escritura");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "escritura"



	// $ANTLR start "stmt"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: stmt : strgstmt ( stmt2 )* ;
	public final void stmt() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "stmt");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(9, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:6: ( strgstmt ( stmt2 )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:8: strgstmt ( stmt2 )*
			{
			dbg.location(9,8);
			pushFollow(FOLLOW_strgstmt_in_stmt38);
			strgstmt();
			state._fsp--;
			dbg.location(9,17);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:17: ( stmt2 )*
			try { dbg.enterSubRule(1);

			loop1:
			while (true) {
				int alt1=2;
				try { dbg.enterDecision(1, decisionCanBacktrack[1]);

				int LA1_0 = input.LA(1);
				if ( (LA1_0==18) ) {
					alt1=1;
				}

				} finally {dbg.exitDecision(1);}

				switch (alt1) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:17: stmt2
					{
					dbg.location(9,17);
					pushFollow(FOLLOW_stmt2_in_stmt40);
					stmt2();
					state._fsp--;

					}
					break;

				default :
					break loop1;
				}
			}
			} finally {dbg.exitSubRule(1);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(9, 22);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "stmt");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "stmt"



	// $ANTLR start "stmt2"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:1: stmt2 : ',' stmt ;
	public final void stmt2() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "stmt2");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(11, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:7: ( ',' stmt )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:9: ',' stmt
			{
			dbg.location(11,9);
			match(input,18,FOLLOW_18_in_stmt249); dbg.location(11,13);
			pushFollow(FOLLOW_stmt_in_stmt251);
			stmt();
			state._fsp--;

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(11, 16);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "stmt2");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "stmt2"



	// $ANTLR start "strgstmt"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:1: strgstmt : ( STRING | expresion );
	public final void strgstmt() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "strgstmt");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(13, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:9: ( STRING | expresion )
			int alt2=2;
			try { dbg.enterDecision(2, decisionCanBacktrack[2]);

			int LA2_0 = input.LA(1);
			if ( (LA2_0==STRING) ) {
				alt2=1;
			}
			else if ( (LA2_0==FLOAT||(LA2_0 >= ID && LA2_0 <= INT)||LA2_0==14||LA2_0==17||LA2_0==19) ) {
				alt2=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 2, 0, input);
				dbg.recognitionException(nvae);
				throw nvae;
			}

			} finally {dbg.exitDecision(2);}

			switch (alt2) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:11: STRING
					{
					dbg.location(13,11);
					match(input,STRING,FOLLOW_STRING_in_strgstmt58); 
					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:20: expresion
					{
					dbg.location(13,20);
					pushFollow(FOLLOW_expresion_in_strgstmt62);
					expresion();
					state._fsp--;

					}
					break;

			}
		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(13, 28);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "strgstmt");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "strgstmt"



	// $ANTLR start "expresion"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:1: expresion : exp opexp ;
	public final void expresion() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "expresion");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(15, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:2: ( exp opexp )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:4: exp opexp
			{
			dbg.location(16,4);
			pushFollow(FOLLOW_exp_in_expresion71);
			exp();
			state._fsp--;
			dbg.location(16,8);
			pushFollow(FOLLOW_opexp_in_expresion73);
			opexp();
			state._fsp--;

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(16, 12);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "expresion");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "expresion"



	// $ANTLR start "opexp"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:1: opexp : ( '>' exp | '<' exp | '<>' exp );
	public final void opexp() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opexp");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(18, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:7: ( '>' exp | '<' exp | '<>' exp )
			int alt3=3;
			try { dbg.enterDecision(3, decisionCanBacktrack[3]);

			switch ( input.LA(1) ) {
			case 25:
				{
				alt3=1;
				}
				break;
			case 23:
				{
				alt3=2;
				}
				break;
			case 24:
				{
				alt3=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 3, 0, input);
				dbg.recognitionException(nvae);
				throw nvae;
			}
			} finally {dbg.exitDecision(3);}

			switch (alt3) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:9: '>' exp
					{
					dbg.location(18,9);
					match(input,25,FOLLOW_25_in_opexp81); dbg.location(18,13);
					pushFollow(FOLLOW_exp_in_opexp83);
					exp();
					state._fsp--;

					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:4: '<' exp
					{
					dbg.location(19,4);
					match(input,23,FOLLOW_23_in_opexp88); dbg.location(19,8);
					pushFollow(FOLLOW_exp_in_opexp90);
					exp();
					state._fsp--;

					}
					break;
				case 3 :
					dbg.enterAlt(3);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:4: '<>' exp
					{
					dbg.location(20,4);
					match(input,24,FOLLOW_24_in_opexp95); dbg.location(20,9);
					pushFollow(FOLLOW_exp_in_opexp97);
					exp();
					state._fsp--;

					}
					break;

			}
		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(21, 1);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opexp");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opexp"



	// $ANTLR start "exp"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:1: exp : termino ( opsum exp )* ;
	public final void exp() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "exp");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(23, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:5: ( termino ( opsum exp )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:7: termino ( opsum exp )*
			{
			dbg.location(23,7);
			pushFollow(FOLLOW_termino_in_exp107);
			termino();
			state._fsp--;
			dbg.location(23,15);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:15: ( opsum exp )*
			try { dbg.enterSubRule(4);

			loop4:
			while (true) {
				int alt4=2;
				try { dbg.enterDecision(4, decisionCanBacktrack[4]);

				int LA4_0 = input.LA(1);
				if ( (LA4_0==17||LA4_0==19) ) {
					alt4=1;
				}

				} finally {dbg.exitDecision(4);}

				switch (alt4) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:16: opsum exp
					{
					dbg.location(23,16);
					pushFollow(FOLLOW_opsum_in_exp110);
					opsum();
					state._fsp--;
					dbg.location(23,22);
					pushFollow(FOLLOW_exp_in_exp112);
					exp();
					state._fsp--;

					}
					break;

				default :
					break loop4;
				}
			}
			} finally {dbg.exitSubRule(4);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(23, 26);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "exp");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "exp"



	// $ANTLR start "factor"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:1: factor : ( '(' expresion ')' | ( opsum )? varcte );
	public final void factor() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "factor");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(25, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:8: ( '(' expresion ')' | ( opsum )? varcte )
			int alt6=2;
			try { dbg.enterDecision(6, decisionCanBacktrack[6]);

			int LA6_0 = input.LA(1);
			if ( (LA6_0==14) ) {
				alt6=1;
			}
			else if ( (LA6_0==FLOAT||(LA6_0 >= ID && LA6_0 <= INT)||LA6_0==17||LA6_0==19) ) {
				alt6=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 6, 0, input);
				dbg.recognitionException(nvae);
				throw nvae;
			}

			} finally {dbg.exitDecision(6);}

			switch (alt6) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:11: '(' expresion ')'
					{
					dbg.location(25,11);
					match(input,14,FOLLOW_14_in_factor123); dbg.location(25,15);
					pushFollow(FOLLOW_expresion_in_factor125);
					expresion();
					state._fsp--;
					dbg.location(25,25);
					match(input,15,FOLLOW_15_in_factor127); 
					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:4: ( opsum )? varcte
					{
					dbg.location(26,4);
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:4: ( opsum )?
					int alt5=2;
					try { dbg.enterSubRule(5);
					try { dbg.enterDecision(5, decisionCanBacktrack[5]);

					int LA5_0 = input.LA(1);
					if ( (LA5_0==17||LA5_0==19) ) {
						alt5=1;
					}
					} finally {dbg.exitDecision(5);}

					switch (alt5) {
						case 1 :
							dbg.enterAlt(1);

							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:4: opsum
							{
							dbg.location(26,4);
							pushFollow(FOLLOW_opsum_in_factor132);
							opsum();
							state._fsp--;

							}
							break;

					}
					} finally {dbg.exitSubRule(5);}
					dbg.location(26,11);
					pushFollow(FOLLOW_varcte_in_factor135);
					varcte();
					state._fsp--;

					}
					break;

			}
		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(26, 16);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "factor");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "factor"



	// $ANTLR start "termino"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:1: termino : factor ( opmul termino )* ;
	public final void termino() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "termino");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(28, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:9: ( factor ( opmul termino )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:11: factor ( opmul termino )*
			{
			dbg.location(28,11);
			pushFollow(FOLLOW_factor_in_termino143);
			factor();
			state._fsp--;
			dbg.location(28,18);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:18: ( opmul termino )*
			try { dbg.enterSubRule(7);

			loop7:
			while (true) {
				int alt7=2;
				try { dbg.enterDecision(7, decisionCanBacktrack[7]);

				int LA7_0 = input.LA(1);
				if ( (LA7_0==16||LA7_0==20) ) {
					alt7=1;
				}

				} finally {dbg.exitDecision(7);}

				switch (alt7) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:19: opmul termino
					{
					dbg.location(28,19);
					pushFollow(FOLLOW_opmul_in_termino146);
					opmul();
					state._fsp--;
					dbg.location(28,25);
					pushFollow(FOLLOW_termino_in_termino148);
					termino();
					state._fsp--;

					}
					break;

				default :
					break loop7;
				}
			}
			} finally {dbg.exitSubRule(7);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(28, 33);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "termino");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "termino"



	// $ANTLR start "vars"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:1: vars : 'var' ( decl )+ ;
	public final void vars() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "vars");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(30, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:6: ( 'var' ( decl )+ )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:8: 'var' ( decl )+
			{
			dbg.location(30,8);
			match(input,29,FOLLOW_29_in_vars158); dbg.location(30,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:14: ( decl )+
			int cnt8=0;
			try { dbg.enterSubRule(8);

			loop8:
			while (true) {
				int alt8=2;
				try { dbg.enterDecision(8, decisionCanBacktrack[8]);

				int LA8_0 = input.LA(1);
				if ( (LA8_0==ID) ) {
					alt8=1;
				}

				} finally {dbg.exitDecision(8);}

				switch (alt8) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:14: decl
					{
					dbg.location(30,14);
					pushFollow(FOLLOW_decl_in_vars160);
					decl();
					state._fsp--;

					}
					break;

				default :
					if ( cnt8 >= 1 ) break loop8;
					EarlyExitException eee = new EarlyExitException(8, input);
					dbg.recognitionException(eee);

					throw eee;
				}
				cnt8++;
			}
			} finally {dbg.exitSubRule(8);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(30, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "vars");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "vars"



	// $ANTLR start "decl"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:1: decl : variabs ':' tipo ';' ;
	public final void decl() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "decl");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(32, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:6: ( variabs ':' tipo ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:8: variabs ':' tipo ';'
			{
			dbg.location(32,8);
			pushFollow(FOLLOW_variabs_in_decl169);
			variabs();
			state._fsp--;
			dbg.location(32,16);
			match(input,21,FOLLOW_21_in_decl171); dbg.location(32,20);
			pushFollow(FOLLOW_tipo_in_decl173);
			tipo();
			state._fsp--;
			dbg.location(32,25);
			match(input,22,FOLLOW_22_in_decl175); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(32, 27);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "decl");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "decl"



	// $ANTLR start "variabs"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:1: variabs : ID ( more )* ;
	public final void variabs() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "variabs");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(34, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:9: ( ID ( more )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:11: ID ( more )*
			{
			dbg.location(34,11);
			match(input,ID,FOLLOW_ID_in_variabs183); dbg.location(34,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:14: ( more )*
			try { dbg.enterSubRule(9);

			loop9:
			while (true) {
				int alt9=2;
				try { dbg.enterDecision(9, decisionCanBacktrack[9]);

				int LA9_0 = input.LA(1);
				if ( (LA9_0==18) ) {
					alt9=1;
				}

				} finally {dbg.exitDecision(9);}

				switch (alt9) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:14: more
					{
					dbg.location(34,14);
					pushFollow(FOLLOW_more_in_variabs185);
					more();
					state._fsp--;

					}
					break;

				default :
					break loop9;
				}
			}
			} finally {dbg.exitSubRule(9);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(34, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "variabs");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "variabs"



	// $ANTLR start "more"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:1: more : ',' variabs ;
	public final void more() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "more");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(36, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:6: ( ',' variabs )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:8: ',' variabs
			{
			dbg.location(36,8);
			match(input,18,FOLLOW_18_in_more194); dbg.location(36,12);
			pushFollow(FOLLOW_variabs_in_more196);
			variabs();
			state._fsp--;

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(36, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "more");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "more"



	// $ANTLR start "varcte"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:38:1: varcte : ( ID | INT | FLOAT );
	public final void varcte() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "varcte");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(38, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:38:8: ( ID | INT | FLOAT )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(38,8);
			if ( input.LA(1)==FLOAT||(input.LA(1) >= ID && input.LA(1) <= INT) ) {
				input.consume();
				state.errorRecovery=false;
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				dbg.recognitionException(mse);
				throw mse;
			}
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(38, 21);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "varcte");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "varcte"



	// $ANTLR start "tipo"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:1: tipo : ( 'int' | 'float' );
	public final void tipo() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "tipo");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(40, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:6: ( 'int' | 'float' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(40,6);
			if ( (input.LA(1) >= 26 && input.LA(1) <= 27) ) {
				input.consume();
				state.errorRecovery=false;
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				dbg.recognitionException(mse);
				throw mse;
			}
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(40, 20);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "tipo");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "tipo"



	// $ANTLR start "opsum"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:1: opsum : ( '+' | '-' );
	public final void opsum() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opsum");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(42, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:7: ( '+' | '-' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(42,7);
			if ( input.LA(1)==17||input.LA(1)==19 ) {
				input.consume();
				state.errorRecovery=false;
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				dbg.recognitionException(mse);
				throw mse;
			}
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(42, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opsum");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opsum"



	// $ANTLR start "opmul"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:1: opmul : ( '*' | '/' );
	public final void opmul() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opmul");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(44, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:7: ( '*' | '/' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(44,7);
			if ( input.LA(1)==16||input.LA(1)==20 ) {
				input.consume();
				state.errorRecovery=false;
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				dbg.recognitionException(mse);
				throw mse;
			}
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(44, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opmul");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opmul"

	// Delegated rules



	public static final BitSet FOLLOW_tipo_in_parse10 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_parse12 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_28_in_escritura22 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_14_in_escritura24 = new BitSet(new long[]{0x00000000000A4B40L});
	public static final BitSet FOLLOW_stmt_in_escritura26 = new BitSet(new long[]{0x0000000000008000L});
	public static final BitSet FOLLOW_15_in_escritura28 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_escritura30 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_strgstmt_in_stmt38 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_stmt2_in_stmt40 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_18_in_stmt249 = new BitSet(new long[]{0x00000000000A4B40L});
	public static final BitSet FOLLOW_stmt_in_stmt251 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_STRING_in_strgstmt58 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_expresion_in_strgstmt62 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_exp_in_expresion71 = new BitSet(new long[]{0x0000000003800000L});
	public static final BitSet FOLLOW_opexp_in_expresion73 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_25_in_opexp81 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp83 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_23_in_opexp88 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp90 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_24_in_opexp95 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp97 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_termino_in_exp107 = new BitSet(new long[]{0x00000000000A0002L});
	public static final BitSet FOLLOW_opsum_in_exp110 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_exp112 = new BitSet(new long[]{0x00000000000A0002L});
	public static final BitSet FOLLOW_14_in_factor123 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_expresion_in_factor125 = new BitSet(new long[]{0x0000000000008000L});
	public static final BitSet FOLLOW_15_in_factor127 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_opsum_in_factor132 = new BitSet(new long[]{0x0000000000000340L});
	public static final BitSet FOLLOW_varcte_in_factor135 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_factor_in_termino143 = new BitSet(new long[]{0x0000000000110002L});
	public static final BitSet FOLLOW_opmul_in_termino146 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_termino_in_termino148 = new BitSet(new long[]{0x0000000000110002L});
	public static final BitSet FOLLOW_29_in_vars158 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_decl_in_vars160 = new BitSet(new long[]{0x0000000000000102L});
	public static final BitSet FOLLOW_variabs_in_decl169 = new BitSet(new long[]{0x0000000000200000L});
	public static final BitSet FOLLOW_21_in_decl171 = new BitSet(new long[]{0x000000000C000000L});
	public static final BitSet FOLLOW_tipo_in_decl173 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_decl175 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ID_in_variabs183 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_more_in_variabs185 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_18_in_more194 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_variabs_in_more196 = new BitSet(new long[]{0x0000000000000002L});
}
