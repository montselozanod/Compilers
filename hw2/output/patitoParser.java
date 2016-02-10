// $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 11:00:58

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
		"'*'", "'+'", "'-'", "'/'", "'float'", "'int'"
	};
	public static final int EOF=-1;
	public static final int T__14=14;
	public static final int T__15=15;
	public static final int T__16=16;
	public static final int T__17=17;
	public static final int T__18=18;
	public static final int T__19=19;
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
		"invalidRule", "parse", "opmul", "varcte", "opsum", "tipo"
	};

	public static final boolean[] decisionCanBacktrack = new boolean[] {
		false, // invalid decision
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



	// $ANTLR start "varcte"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:6:1: varcte : ( ID | INT | FLOAT );
	public final void varcte() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "varcte");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(6, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:6:8: ( ID | INT | FLOAT )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(6,8);
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
		dbg.location(6, 21);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "varcte");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "varcte"



	// $ANTLR start "tipo"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:1: tipo : ( 'int' | 'float' );
	public final void tipo() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "tipo");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(8, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:6: ( 'int' | 'float' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(8,6);
			if ( (input.LA(1) >= 18 && input.LA(1) <= 19) ) {
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
		dbg.location(8, 20);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "tipo");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "tipo"



	// $ANTLR start "opsum"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:1: opsum : ( '+' | '-' );
	public final void opsum() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opsum");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(10, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:7: ( '+' | '-' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(10,7);
			if ( (input.LA(1) >= 15 && input.LA(1) <= 16) ) {
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
		dbg.location(10, 15);

		}
		finally {
			dbg.exitRule(getGrammarFileName(), "opsum");
			decRuleLevel();
			if ( getRuleLevel()==0 ) {dbg.terminate();}
		}

	}
	// $ANTLR end "opsum"



	// $ANTLR start "opmul"
	// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:1: opmul : ( '*' | '/' );
	public final void opmul() throws RecognitionException {
		try { dbg.enterRule(getGrammarFileName(), "opmul");
		if ( getRuleLevel()==0 ) {dbg.commence();}
		incRuleLevel();
		dbg.location(12, 0);

		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:7: ( '*' | '/' )
			dbg.enterAlt(1);

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			dbg.location(12,7);
			if ( input.LA(1)==14||input.LA(1)==17 ) {
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
		dbg.location(12, 15);

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
}
