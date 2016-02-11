// $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 20:33:58

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
		"'<>'", "'='", "'>'", "'else'", "'float'", "'if'", "'int'", "'print'", 
		"'program'", "'var'", "'{'", "'}'"
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
	public static final int T__30=30;
	public static final int T__31=31;
	public static final int T__32=32;
	public static final int T__33=33;
	public static final int T__34=34;
	public static final int T__35=35;
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
		"invalidRule", "asignacion", "decl", "opexp", "escritura", "varcte", "start", 
		"condicion", "tipo", "bloque", "exp", "stmt", "opsum", "estatuto", "variabs", 
		"strgstmt", "termino", "opmul", "condelse", "programa", "vars", "expresion", 
		"factor"
	};

	public static final boolean[] decisionCanBacktrack = new boolean[] {
		false, // invalid decision
		false, false, false, false, false, false, false, false, false, false, 
		    false, false, false, false
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



	// $ANTLR start "start"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:1: start : programa EOF ;
	public final void start() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "start");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(3, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:7: ( programa EOF )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:9: programa EOF
			{
			dbg.location(3,9);
			pushFollow(FOLLOW_programa_in_start10);
			programa();
			state._fsp--;
			dbg.location(3,18);
			match(input,EOF,FOLLOW_EOF_in_start12); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(3, 20);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "start");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "start"



	// $ANTLR start "programa"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:1: programa : 'program' ID ';' ( vars )? bloque ;
	public final void programa() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "programa");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(5, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:9: ( 'program' ID ';' ( vars )? bloque )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:11: 'program' ID ';' ( vars )? bloque
			{
			dbg.location(5,11);
			match(input,32,FOLLOW_32_in_programa19); dbg.location(5,21);
			match(input,ID,FOLLOW_ID_in_programa21); dbg.location(5,24);
			match(input,22,FOLLOW_22_in_programa23); dbg.location(5,28);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:28: ( vars )?
			int alt1=2;
			try { dbg.enterSubRule(1);
			try { dbg.enterDecision(1, decisionCanBacktrack[1]);

			int LA1_0 = input.LA(1);
			if ( (LA1_0==33) ) {
				alt1=1;
			}
			} finally {dbg.exitDecision(1);}

			switch (alt1) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:28: vars
					{
					dbg.location(5,28);
					pushFollow(FOLLOW_vars_in_programa25);
					vars();
					state._fsp--;

					}
					break;

			}
			} finally {dbg.exitSubRule(1);}
			dbg.location(5,34);
			pushFollow(FOLLOW_bloque_in_programa28);
			bloque();
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
		dbg.location(5, 39);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "programa");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "programa"



	// $ANTLR start "bloque"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:1: bloque : '{' ( estatuto )* '}' ;
	public final void bloque() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "bloque");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(7, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:8: ( '{' ( estatuto )* '}' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:10: '{' ( estatuto )* '}'
			{
			dbg.location(7,10);
			match(input,34,FOLLOW_34_in_bloque36); dbg.location(7,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:14: ( estatuto )*
			try { dbg.enterSubRule(2);

			loop2:
			while (true) {
				int alt2=2;
				try { dbg.enterDecision(2, decisionCanBacktrack[2]);

				int LA2_0 = input.LA(1);
				if ( (LA2_0==ID||LA2_0==29||LA2_0==31) ) {
					alt2=1;
				}

				} finally {dbg.exitDecision(2);}

				switch (alt2) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:14: estatuto
					{
					dbg.location(7,14);
					pushFollow(FOLLOW_estatuto_in_bloque38);
					estatuto();
					state._fsp--;

					}
					break;

				default :
					break loop2;
				}
			}
			} finally {dbg.exitSubRule(2);}
			dbg.location(7,24);
			match(input,35,FOLLOW_35_in_bloque41); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(7, 26);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "bloque");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "bloque"



	// $ANTLR start "estatuto"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: estatuto : ( asignacion | escritura | condicion );
	public final void estatuto() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "estatuto");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(9, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ( asignacion | escritura | condicion )
			int alt3=3;
			try { dbg.enterDecision(3, decisionCanBacktrack[3]);

			switch ( input.LA(1) ) {
			case ID:
				{
				alt3=1;
				}
				break;
			case 31:
				{
				alt3=2;
				}
				break;
			case 29:
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

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:11: asignacion
					{
					dbg.location(9,11);
					pushFollow(FOLLOW_asignacion_in_estatuto48);
					asignacion();
					state._fsp--;

					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:4: escritura
					{
					dbg.location(10,4);
					pushFollow(FOLLOW_escritura_in_estatuto53);
					escritura();
					state._fsp--;

					}
					break;
				case 3 :
					dbg.enterAlt(3);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:3: condicion
					{
					dbg.location(11,3);
					pushFollow(FOLLOW_condicion_in_estatuto57);
					condicion();
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
		dbg.location(11, 11);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "estatuto");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "estatuto"



	// $ANTLR start "condicion"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:1: condicion : 'if' '(' expresion ')' bloque ( condelse )? ';' ;
	public final void condicion() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "condicion");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(13, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:2: ( 'if' '(' expresion ')' bloque ( condelse )? ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:4: 'if' '(' expresion ')' bloque ( condelse )? ';'
			{
			dbg.location(14,4);
			match(input,29,FOLLOW_29_in_condicion66); dbg.location(14,9);
			match(input,14,FOLLOW_14_in_condicion68); dbg.location(14,13);
			pushFollow(FOLLOW_expresion_in_condicion70);
			expresion();
			state._fsp--;
			dbg.location(14,23);
			match(input,15,FOLLOW_15_in_condicion72); dbg.location(14,27);
			pushFollow(FOLLOW_bloque_in_condicion74);
			bloque();
			state._fsp--;
			dbg.location(14,34);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:34: ( condelse )?
			int alt4=2;
			try { dbg.enterSubRule(4);
			try { dbg.enterDecision(4, decisionCanBacktrack[4]);

			int LA4_0 = input.LA(1);
			if ( (LA4_0==27) ) {
				alt4=1;
			}
			} finally {dbg.exitDecision(4);}

			switch (alt4) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:34: condelse
					{
					dbg.location(14,34);
					pushFollow(FOLLOW_condelse_in_condicion76);
					condelse();
					state._fsp--;

					}
					break;

			}
			} finally {dbg.exitSubRule(4);}
			dbg.location(14,44);
			match(input,22,FOLLOW_22_in_condicion79); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(14, 46);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "condicion");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "condicion"



	// $ANTLR start "condelse"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:1: condelse : 'else' bloque ;
	public final void condelse() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "condelse");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(16, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:9: ( 'else' bloque )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:11: 'else' bloque
			{
			dbg.location(16,11);
			match(input,27,FOLLOW_27_in_condelse86); dbg.location(16,18);
			pushFollow(FOLLOW_bloque_in_condelse88);
			bloque();
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
		dbg.location(16, 23);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "condelse");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "condelse"



	// $ANTLR start "asignacion"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:1: asignacion : ID '=' expresion ';' ;
	public final void asignacion() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "asignacion");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(18, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:2: ( ID '=' expresion ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:4: ID '=' expresion ';'
			{
			dbg.location(19,4);
			match(input,ID,FOLLOW_ID_in_asignacion97); dbg.location(19,7);
			match(input,25,FOLLOW_25_in_asignacion99); dbg.location(19,11);
			pushFollow(FOLLOW_expresion_in_asignacion101);
			expresion();
			state._fsp--;
			dbg.location(19,21);
			match(input,22,FOLLOW_22_in_asignacion103); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(19, 23);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "asignacion");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "asignacion"



	// $ANTLR start "escritura"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:1: escritura : 'print' '(' stmt ')' ';' ;
	public final void escritura() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "escritura");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(20, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:2: ( 'print' '(' stmt ')' ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:4: 'print' '(' stmt ')' ';'
			{
			dbg.location(21,4);
			match(input,31,FOLLOW_31_in_escritura111); dbg.location(21,12);
			match(input,14,FOLLOW_14_in_escritura113); dbg.location(21,16);
			pushFollow(FOLLOW_stmt_in_escritura115);
			stmt();
			state._fsp--;
			dbg.location(21,21);
			match(input,15,FOLLOW_15_in_escritura117); dbg.location(21,25);
			match(input,22,FOLLOW_22_in_escritura119); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(21, 27);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "escritura");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "escritura"



	// $ANTLR start "stmt"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:1: stmt : strgstmt ( ',' strgstmt )* ;
	public final void stmt() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "stmt");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(23, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:6: ( strgstmt ( ',' strgstmt )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:8: strgstmt ( ',' strgstmt )*
			{
			dbg.location(23,8);
			pushFollow(FOLLOW_strgstmt_in_stmt127);
			strgstmt();
			state._fsp--;
			dbg.location(23,17);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:17: ( ',' strgstmt )*
			try { dbg.enterSubRule(5);

			loop5:
			while (true) {
				int alt5=2;
				try { dbg.enterDecision(5, decisionCanBacktrack[5]);

				int LA5_0 = input.LA(1);
				if ( (LA5_0==18) ) {
					alt5=1;
				}

				} finally {dbg.exitDecision(5);}

				switch (alt5) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:18: ',' strgstmt
					{
					dbg.location(23,18);
					match(input,18,FOLLOW_18_in_stmt130); dbg.location(23,22);
					pushFollow(FOLLOW_strgstmt_in_stmt132);
					strgstmt();
					state._fsp--;

					}
					break;

				default :
					break loop5;
				}
			}
			} finally {dbg.exitSubRule(5);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(23, 31);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "stmt");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "stmt"



	// $ANTLR start "strgstmt"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:1: strgstmt : ( STRING | expresion );
	public final void strgstmt() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "strgstmt");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(25, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:9: ( STRING | expresion )
			int alt6=2;
			try { dbg.enterDecision(6, decisionCanBacktrack[6]);

			int LA6_0 = input.LA(1);
			if ( (LA6_0==STRING) ) {
				alt6=1;
			}
			else if ( (LA6_0==FLOAT||(LA6_0 >= ID && LA6_0 <= INT)||LA6_0==14||LA6_0==17||LA6_0==19) ) {
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

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:11: STRING
					{
					dbg.location(25,11);
					match(input,STRING,FOLLOW_STRING_in_strgstmt141); 
					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:20: expresion
					{
					dbg.location(25,20);
					pushFollow(FOLLOW_expresion_in_strgstmt145);
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
		dbg.location(25, 28);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "strgstmt");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "strgstmt"



	// $ANTLR start "expresion"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:1: expresion : exp ( opexp )? ;
	public final void expresion() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "expresion");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(27, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:2: ( exp ( opexp )? )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:4: exp ( opexp )?
			{
			dbg.location(28,4);
			pushFollow(FOLLOW_exp_in_expresion154);
			exp();
			state._fsp--;
			dbg.location(28,8);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:8: ( opexp )?
			int alt7=2;
			try { dbg.enterSubRule(7);
			try { dbg.enterDecision(7, decisionCanBacktrack[7]);

			int LA7_0 = input.LA(1);
			if ( ((LA7_0 >= 23 && LA7_0 <= 24)||LA7_0==26) ) {
				alt7=1;
			}
			} finally {dbg.exitDecision(7);}

			switch (alt7) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:8: opexp
					{
					dbg.location(28,8);
					pushFollow(FOLLOW_opexp_in_expresion156);
					opexp();
					state._fsp--;

					}
					break;

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
		dbg.location(28, 13);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "expresion");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "expresion"



	// $ANTLR start "opexp"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:1: opexp : ( '>' exp | '<' exp | '<>' exp );
	public final void opexp() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opexp");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(30, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:7: ( '>' exp | '<' exp | '<>' exp )
			int alt8=3;
			try { dbg.enterDecision(8, decisionCanBacktrack[8]);

			switch ( input.LA(1) ) {
			case 26:
				{
				alt8=1;
				}
				break;
			case 23:
				{
				alt8=2;
				}
				break;
			case 24:
				{
				alt8=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 8, 0, input);
				dbg.recognitionException(nvae);
				throw nvae;
			}
			} finally {dbg.exitDecision(8);}

			switch (alt8) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:9: '>' exp
					{
					dbg.location(30,9);
					match(input,26,FOLLOW_26_in_opexp165); dbg.location(30,13);
					pushFollow(FOLLOW_exp_in_opexp167);
					exp();
					state._fsp--;

					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:31:4: '<' exp
					{
					dbg.location(31,4);
					match(input,23,FOLLOW_23_in_opexp172); dbg.location(31,8);
					pushFollow(FOLLOW_exp_in_opexp174);
					exp();
					state._fsp--;

					}
					break;
				case 3 :
					dbg.enterAlt(3);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:4: '<>' exp
					{
					dbg.location(32,4);
					match(input,24,FOLLOW_24_in_opexp179); dbg.location(32,9);
					pushFollow(FOLLOW_exp_in_opexp181);
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
		dbg.location(33, 1);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opexp");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opexp"



	// $ANTLR start "exp"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:1: exp : termino ( opsum termino )* ;
	public final void exp() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "exp");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(35, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:5: ( termino ( opsum termino )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:7: termino ( opsum termino )*
			{
			dbg.location(35,7);
			pushFollow(FOLLOW_termino_in_exp191);
			termino();
			state._fsp--;
			dbg.location(35,15);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:15: ( opsum termino )*
			try { dbg.enterSubRule(9);

			loop9:
			while (true) {
				int alt9=2;
				try { dbg.enterDecision(9, decisionCanBacktrack[9]);

				int LA9_0 = input.LA(1);
				if ( (LA9_0==17||LA9_0==19) ) {
					alt9=1;
				}

				} finally {dbg.exitDecision(9);}

				switch (alt9) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:16: opsum termino
					{
					dbg.location(35,16);
					pushFollow(FOLLOW_opsum_in_exp194);
					opsum();
					state._fsp--;
					dbg.location(35,22);
					pushFollow(FOLLOW_termino_in_exp196);
					termino();
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
		dbg.location(35, 30);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "exp");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "exp"



	// $ANTLR start "factor"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:37:1: factor : ( '(' expresion ')' | ( opsum )? varcte );
	public final void factor() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "factor");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(37, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:37:8: ( '(' expresion ')' | ( opsum )? varcte )
			int alt11=2;
			try { dbg.enterDecision(11, decisionCanBacktrack[11]);

			int LA11_0 = input.LA(1);
			if ( (LA11_0==14) ) {
				alt11=1;
			}
			else if ( (LA11_0==FLOAT||(LA11_0 >= ID && LA11_0 <= INT)||LA11_0==17||LA11_0==19) ) {
				alt11=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 11, 0, input);
				dbg.recognitionException(nvae);
				throw nvae;
			}

			} finally {dbg.exitDecision(11);}

			switch (alt11) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:37:11: '(' expresion ')'
					{
					dbg.location(37,11);
					match(input,14,FOLLOW_14_in_factor207); dbg.location(37,15);
					pushFollow(FOLLOW_expresion_in_factor209);
					expresion();
					state._fsp--;
					dbg.location(37,25);
					match(input,15,FOLLOW_15_in_factor211); 
					}
					break;
				case 2 :
					dbg.enterAlt(2);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:38:4: ( opsum )? varcte
					{
					dbg.location(38,4);
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:38:4: ( opsum )?
					int alt10=2;
					try { dbg.enterSubRule(10);
					try { dbg.enterDecision(10, decisionCanBacktrack[10]);

					int LA10_0 = input.LA(1);
					if ( (LA10_0==17||LA10_0==19) ) {
						alt10=1;
					}
					} finally {dbg.exitDecision(10);}

					switch (alt10) {
						case 1 :
							dbg.enterAlt(1);

							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:38:4: opsum
							{
							dbg.location(38,4);
							pushFollow(FOLLOW_opsum_in_factor216);
							opsum();
							state._fsp--;

							}
							break;

					}
					} finally {dbg.exitSubRule(10);}
					dbg.location(38,11);
					pushFollow(FOLLOW_varcte_in_factor219);
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
		dbg.location(38, 16);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "factor");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "factor"



	// $ANTLR start "termino"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:1: termino : factor ( opmul factor )* ;
	public final void termino() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "termino");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(40, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:9: ( factor ( opmul factor )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:11: factor ( opmul factor )*
			{
			dbg.location(40,11);
			pushFollow(FOLLOW_factor_in_termino228);
			factor();
			state._fsp--;
			dbg.location(40,18);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:18: ( opmul factor )*
			try { dbg.enterSubRule(12);

			loop12:
			while (true) {
				int alt12=2;
				try { dbg.enterDecision(12, decisionCanBacktrack[12]);

				int LA12_0 = input.LA(1);
				if ( (LA12_0==16||LA12_0==20) ) {
					alt12=1;
				}

				} finally {dbg.exitDecision(12);}

				switch (alt12) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:19: opmul factor
					{
					dbg.location(40,19);
					pushFollow(FOLLOW_opmul_in_termino231);
					opmul();
					state._fsp--;
					dbg.location(40,25);
					pushFollow(FOLLOW_factor_in_termino233);
					factor();
					state._fsp--;

					}
					break;

				default :
					break loop12;
				}
			}
			} finally {dbg.exitSubRule(12);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(40, 32);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "termino");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "termino"



	// $ANTLR start "vars"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:1: vars : 'var' ( decl )+ ;
	public final void vars() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "vars");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(42, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:6: ( 'var' ( decl )+ )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:8: 'var' ( decl )+
			{
			dbg.location(42,8);
			match(input,33,FOLLOW_33_in_vars243); dbg.location(42,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:14: ( decl )+
			int cnt13=0;
			try { dbg.enterSubRule(13);

			loop13:
			while (true) {
				int alt13=2;
				try { dbg.enterDecision(13, decisionCanBacktrack[13]);

				int LA13_0 = input.LA(1);
				if ( (LA13_0==ID) ) {
					alt13=1;
				}

				} finally {dbg.exitDecision(13);}

				switch (alt13) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:14: decl
					{
					dbg.location(42,14);
					pushFollow(FOLLOW_decl_in_vars245);
					decl();
					state._fsp--;

					}
					break;

				default :
					if ( cnt13 >= 1 ) break loop13;
					EarlyExitException eee = new EarlyExitException(13, input);
					dbg.recognitionException(eee);

					throw eee;
				}
				cnt13++;
			}
			} finally {dbg.exitSubRule(13);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(42, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "vars");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "vars"



	// $ANTLR start "decl"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:1: decl : variabs ':' tipo ';' ;
	public final void decl() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "decl");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(44, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:6: ( variabs ':' tipo ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:8: variabs ':' tipo ';'
			{
			dbg.location(44,8);
			pushFollow(FOLLOW_variabs_in_decl254);
			variabs();
			state._fsp--;
			dbg.location(44,16);
			match(input,21,FOLLOW_21_in_decl256); dbg.location(44,20);
			pushFollow(FOLLOW_tipo_in_decl258);
			tipo();
			state._fsp--;
			dbg.location(44,25);
			match(input,22,FOLLOW_22_in_decl260); 
			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(44, 27);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "decl");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "decl"



	// $ANTLR start "variabs"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:1: variabs : ID ( ',' ID )* ;
	public final void variabs() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "variabs");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(46, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:9: ( ID ( ',' ID )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:11: ID ( ',' ID )*
			{
			dbg.location(46,11);
			match(input,ID,FOLLOW_ID_in_variabs268); dbg.location(46,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: ( ',' ID )*
			try { dbg.enterSubRule(14);

			loop14:
			while (true) {
				int alt14=2;
				try { dbg.enterDecision(14, decisionCanBacktrack[14]);

				int LA14_0 = input.LA(1);
				if ( (LA14_0==18) ) {
					alt14=1;
				}

				} finally {dbg.exitDecision(14);}

				switch (alt14) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:15: ',' ID
					{
					dbg.location(46,15);
					match(input,18,FOLLOW_18_in_variabs271); dbg.location(46,19);
					match(input,ID,FOLLOW_ID_in_variabs273); 
					}
					break;

				default :
					break loop14;
				}
			}
			} finally {dbg.exitSubRule(14);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(46, 22);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "variabs");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "variabs"



	// $ANTLR start "varcte"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:1: varcte : ( ID | INT | FLOAT );
	public final void varcte() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "varcte");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(48, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:8: ( ID | INT | FLOAT )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(48,8);
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
		dbg.location(48, 21);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "varcte");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "varcte"



	// $ANTLR start "tipo"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:1: tipo : ( 'int' | 'float' );
	public final void tipo() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "tipo");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(50, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:6: ( 'int' | 'float' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(50,6);
			if ( input.LA(1)==28||input.LA(1)==30 ) {
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
		dbg.location(50, 20);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "tipo");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "tipo"



	// $ANTLR start "opsum"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:1: opsum : ( '+' | '-' );
	public final void opsum() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opsum");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(52, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:7: ( '+' | '-' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(52,7);
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
		dbg.location(52, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opsum");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opsum"



	// $ANTLR start "opmul"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:1: opmul : ( '*' | '/' );
	public final void opmul() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opmul");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(54, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:7: ( '*' | '/' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(54,7);
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
		dbg.location(54, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opmul");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opmul"

	// Delegated rules



	public static final BitSet FOLLOW_programa_in_start10 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_start12 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_32_in_programa19 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ID_in_programa21 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_programa23 = new BitSet(new long[]{0x0000000600000000L});
	public static final BitSet FOLLOW_vars_in_programa25 = new BitSet(new long[]{0x0000000400000000L});
	public static final BitSet FOLLOW_bloque_in_programa28 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_34_in_bloque36 = new BitSet(new long[]{0x00000008A0000100L});
	public static final BitSet FOLLOW_estatuto_in_bloque38 = new BitSet(new long[]{0x00000008A0000100L});
	public static final BitSet FOLLOW_35_in_bloque41 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_asignacion_in_estatuto48 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_escritura_in_estatuto53 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_condicion_in_estatuto57 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_29_in_condicion66 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_14_in_condicion68 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_expresion_in_condicion70 = new BitSet(new long[]{0x0000000000008000L});
	public static final BitSet FOLLOW_15_in_condicion72 = new BitSet(new long[]{0x0000000400000000L});
	public static final BitSet FOLLOW_bloque_in_condicion74 = new BitSet(new long[]{0x0000000008400000L});
	public static final BitSet FOLLOW_condelse_in_condicion76 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_condicion79 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_27_in_condelse86 = new BitSet(new long[]{0x0000000400000000L});
	public static final BitSet FOLLOW_bloque_in_condelse88 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ID_in_asignacion97 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_asignacion99 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_expresion_in_asignacion101 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_asignacion103 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_31_in_escritura111 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_14_in_escritura113 = new BitSet(new long[]{0x00000000000A4B40L});
	public static final BitSet FOLLOW_stmt_in_escritura115 = new BitSet(new long[]{0x0000000000008000L});
	public static final BitSet FOLLOW_15_in_escritura117 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_escritura119 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_strgstmt_in_stmt127 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_18_in_stmt130 = new BitSet(new long[]{0x00000000000A4B40L});
	public static final BitSet FOLLOW_strgstmt_in_stmt132 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_STRING_in_strgstmt141 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_expresion_in_strgstmt145 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_exp_in_expresion154 = new BitSet(new long[]{0x0000000005800002L});
	public static final BitSet FOLLOW_opexp_in_expresion156 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_26_in_opexp165 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp167 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_23_in_opexp172 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp174 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_24_in_opexp179 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_exp_in_opexp181 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_termino_in_exp191 = new BitSet(new long[]{0x00000000000A0002L});
	public static final BitSet FOLLOW_opsum_in_exp194 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_termino_in_exp196 = new BitSet(new long[]{0x00000000000A0002L});
	public static final BitSet FOLLOW_14_in_factor207 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_expresion_in_factor209 = new BitSet(new long[]{0x0000000000008000L});
	public static final BitSet FOLLOW_15_in_factor211 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_opsum_in_factor216 = new BitSet(new long[]{0x0000000000000340L});
	public static final BitSet FOLLOW_varcte_in_factor219 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_factor_in_termino228 = new BitSet(new long[]{0x0000000000110002L});
	public static final BitSet FOLLOW_opmul_in_termino231 = new BitSet(new long[]{0x00000000000A4340L});
	public static final BitSet FOLLOW_factor_in_termino233 = new BitSet(new long[]{0x0000000000110002L});
	public static final BitSet FOLLOW_33_in_vars243 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_decl_in_vars245 = new BitSet(new long[]{0x0000000000000102L});
	public static final BitSet FOLLOW_variabs_in_decl254 = new BitSet(new long[]{0x0000000000200000L});
	public static final BitSet FOLLOW_21_in_decl256 = new BitSet(new long[]{0x0000000050000000L});
	public static final BitSet FOLLOW_tipo_in_decl258 = new BitSet(new long[]{0x0000000000400000L});
	public static final BitSet FOLLOW_22_in_decl260 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ID_in_variabs268 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_18_in_variabs271 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ID_in_variabs273 = new BitSet(new long[]{0x0000000000040002L});
}
