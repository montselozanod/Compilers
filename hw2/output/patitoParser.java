// $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 11:06:32

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
		"'*'", "'+'", "','", "'-'", "'/'", "':'", "';'", "'float'", "'int'", "'var'"
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
		"invalidRule", "variabs", "tipo", "vars", "more", "decl", "opsum", "opmul", 
		"parse", "varcte"
	};

	public static final boolean[] decisionCanBacktrack = new boolean[] {
		false, // invalid decision
		false, false
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



	// $ANTLR start "vars"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:1: vars : 'var' ( decl )+ ;
	public final void vars() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "vars");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(5, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:6: ( 'var' ( decl )+ )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:8: 'var' ( decl )+
			{
			dbg.location(5,8);
			match(input,23,FOLLOW_23_in_vars20); dbg.location(5,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:14: ( decl )+
			int cnt1=0;
			try { dbg.enterSubRule(1);

			loop1:
			while (true) {
				int alt1=2;
				try { dbg.enterDecision(1, decisionCanBacktrack[1]);

				int LA1_0 = input.LA(1);
				if ( (LA1_0==ID) ) {
					alt1=1;
				}

				} finally {dbg.exitDecision(1);}

				switch (alt1) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:14: decl
					{
					dbg.location(5,14);
					pushFollow(FOLLOW_decl_in_vars22);
					decl();
					state._fsp--;

					}
					break;

				default :
					if ( cnt1 >= 1 ) break loop1;
					EarlyExitException eee = new EarlyExitException(1, input);
					dbg.recognitionException(eee);

					throw eee;
				}
				cnt1++;
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
		dbg.location(5, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "vars");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "vars"



	// $ANTLR start "decl"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:1: decl : variabs ':' tipo ';' ;
	public final void decl() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "decl");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(7, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:6: ( variabs ':' tipo ';' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:8: variabs ':' tipo ';'
			{
			dbg.location(7,8);
			pushFollow(FOLLOW_variabs_in_decl31);
			variabs();
			state._fsp--;
			dbg.location(7,16);
			match(input,19,FOLLOW_19_in_decl33); dbg.location(7,20);
			pushFollow(FOLLOW_tipo_in_decl35);
			tipo();
			state._fsp--;
			dbg.location(7,25);
			match(input,20,FOLLOW_20_in_decl37); 
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
			dbg.exitRule(getGrammarFileName(), "decl");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "decl"



	// $ANTLR start "variabs"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: variabs : ID ( more )* ;
	public final void variabs() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "variabs");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(9, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ( ID ( more )* )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:11: ID ( more )*
			{
			dbg.location(9,11);
			match(input,ID,FOLLOW_ID_in_variabs45); dbg.location(9,14);
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:14: ( more )*
			try { dbg.enterSubRule(2);

			loop2:
			while (true) {
				int alt2=2;
				try { dbg.enterDecision(2, decisionCanBacktrack[2]);

				int LA2_0 = input.LA(1);
				if ( (LA2_0==16) ) {
					alt2=1;
				}

				} finally {dbg.exitDecision(2);}

				switch (alt2) {
				case 1 :
					dbg.enterAlt(1);

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:14: more
					{
					dbg.location(9,14);
					pushFollow(FOLLOW_more_in_variabs47);
					more();
					state._fsp--;

					}
					break;

				default :
					break loop2;
				}
			}
			} finally {dbg.exitSubRule(2);}

			}

		}
		catch (RecognitionException re) {
			reportError(re);
			recover(input,re);
		}
		finally {
			// do for sure before leaving
		}
		dbg.location(9, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "variabs");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "variabs"



	// $ANTLR start "more"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:1: more : ',' variabs ;
	public final void more() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "more");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(11, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:6: ( ',' variabs )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:8: ',' variabs
			{
			dbg.location(11,8);
			match(input,16,FOLLOW_16_in_more56); dbg.location(11,12);
			pushFollow(FOLLOW_variabs_in_more58);
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
		dbg.location(11, 18);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "more");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "more"



	// $ANTLR start "varcte"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:1: varcte : ( ID | INT | FLOAT );
	public final void varcte() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "varcte");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(13, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:8: ( ID | INT | FLOAT )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(13,8);
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
		dbg.location(13, 21);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "varcte");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "varcte"



	// $ANTLR start "tipo"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:1: tipo : ( 'int' | 'float' );
	public final void tipo() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "tipo");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(15, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:6: ( 'int' | 'float' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(15,6);
			if ( (input.LA(1) >= 21 && input.LA(1) <= 22) ) {
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
		dbg.location(15, 20);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "tipo");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "tipo"



	// $ANTLR start "opsum"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:1: opsum : ( '+' | '-' );
	public final void opsum() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opsum");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(17, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:7: ( '+' | '-' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(17,7);
			if ( input.LA(1)==15||input.LA(1)==17 ) {
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
		dbg.location(17, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opsum");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opsum"



	// $ANTLR start "opmul"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:1: opmul : ( '*' | '/' );
	public final void opmul() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opmul");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(19, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:7: ( '*' | '/' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(19,7);
			if ( input.LA(1)==14||input.LA(1)==18 ) {
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
		dbg.location(19, 15);

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
	public static final BitSet FOLLOW_23_in_vars20 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_decl_in_vars22 = new BitSet(new long[]{0x0000000000000102L});
	public static final BitSet FOLLOW_variabs_in_decl31 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_decl33 = new BitSet(new long[]{0x0000000000600000L});
	public static final BitSet FOLLOW_tipo_in_decl35 = new BitSet(new long[]{0x0000000000100000L});
	public static final BitSet FOLLOW_20_in_decl37 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ID_in_variabs45 = new BitSet(new long[]{0x0000000000010002L});
	public static final BitSet FOLLOW_more_in_variabs47 = new BitSet(new long[]{0x0000000000010002L});
	public static final BitSet FOLLOW_16_in_more56 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_variabs_in_more58 = new BitSet(new long[]{0x0000000000000002L});
}
