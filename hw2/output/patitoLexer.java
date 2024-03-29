// $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 20:33:58

import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

@SuppressWarnings("all")
public class patitoLexer extends Lexer {
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
	// delegators
	public Lexer[] getDelegates() {
		return new Lexer[] {};
	}

	public patitoLexer() {} 
	public patitoLexer(CharStream input) {
		this(input, new RecognizerSharedState());
	}
	public patitoLexer(CharStream input, RecognizerSharedState state) {
		super(input,state);
	}
	@Override public String getGrammarFileName() { return "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"; }

	// $ANTLR start "T__14"
	public final void mT__14() throws RecognitionException {
		try {
			int _type = T__14;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:2:7: ( '(' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:2:9: '('
			{
			match('('); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__14"

	// $ANTLR start "T__15"
	public final void mT__15() throws RecognitionException {
		try {
			int _type = T__15;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:7: ( ')' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:3:9: ')'
			{
			match(')'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__15"

	// $ANTLR start "T__16"
	public final void mT__16() throws RecognitionException {
		try {
			int _type = T__16;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:4:7: ( '*' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:4:9: '*'
			{
			match('*'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__16"

	// $ANTLR start "T__17"
	public final void mT__17() throws RecognitionException {
		try {
			int _type = T__17;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:7: ( '+' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:5:9: '+'
			{
			match('+'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__17"

	// $ANTLR start "T__18"
	public final void mT__18() throws RecognitionException {
		try {
			int _type = T__18;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:6:7: ( ',' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:6:9: ','
			{
			match(','); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__18"

	// $ANTLR start "T__19"
	public final void mT__19() throws RecognitionException {
		try {
			int _type = T__19;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:7: ( '-' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:9: '-'
			{
			match('-'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__19"

	// $ANTLR start "T__20"
	public final void mT__20() throws RecognitionException {
		try {
			int _type = T__20;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:7: ( '/' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:9: '/'
			{
			match('/'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__20"

	// $ANTLR start "T__21"
	public final void mT__21() throws RecognitionException {
		try {
			int _type = T__21;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:7: ( ':' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ':'
			{
			match(':'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__21"

	// $ANTLR start "T__22"
	public final void mT__22() throws RecognitionException {
		try {
			int _type = T__22;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:7: ( ';' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:9: ';'
			{
			match(';'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__22"

	// $ANTLR start "T__23"
	public final void mT__23() throws RecognitionException {
		try {
			int _type = T__23;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:7: ( '<' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:9: '<'
			{
			match('<'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__23"

	// $ANTLR start "T__24"
	public final void mT__24() throws RecognitionException {
		try {
			int _type = T__24;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:7: ( '<>' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:9: '<>'
			{
			match("<>"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__24"

	// $ANTLR start "T__25"
	public final void mT__25() throws RecognitionException {
		try {
			int _type = T__25;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:7: ( '=' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:9: '='
			{
			match('='); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__25"

	// $ANTLR start "T__26"
	public final void mT__26() throws RecognitionException {
		try {
			int _type = T__26;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:7: ( '>' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:9: '>'
			{
			match('>'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__26"

	// $ANTLR start "T__27"
	public final void mT__27() throws RecognitionException {
		try {
			int _type = T__27;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:7: ( 'else' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:9: 'else'
			{
			match("else"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__27"

	// $ANTLR start "T__28"
	public final void mT__28() throws RecognitionException {
		try {
			int _type = T__28;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:7: ( 'float' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:9: 'float'
			{
			match("float"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__28"

	// $ANTLR start "T__29"
	public final void mT__29() throws RecognitionException {
		try {
			int _type = T__29;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:7: ( 'if' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:9: 'if'
			{
			match("if"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__29"

	// $ANTLR start "T__30"
	public final void mT__30() throws RecognitionException {
		try {
			int _type = T__30;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:7: ( 'int' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:9: 'int'
			{
			match("int"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__30"

	// $ANTLR start "T__31"
	public final void mT__31() throws RecognitionException {
		try {
			int _type = T__31;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:7: ( 'print' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:9: 'print'
			{
			match("print"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__31"

	// $ANTLR start "T__32"
	public final void mT__32() throws RecognitionException {
		try {
			int _type = T__32;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:7: ( 'program' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:9: 'program'
			{
			match("program"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__32"

	// $ANTLR start "T__33"
	public final void mT__33() throws RecognitionException {
		try {
			int _type = T__33;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:7: ( 'var' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:9: 'var'
			{
			match("var"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__33"

	// $ANTLR start "T__34"
	public final void mT__34() throws RecognitionException {
		try {
			int _type = T__34;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:7: ( '{' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:9: '{'
			{
			match('{'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__34"

	// $ANTLR start "T__35"
	public final void mT__35() throws RecognitionException {
		try {
			int _type = T__35;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:7: ( '}' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:9: '}'
			{
			match('}'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__35"

	// $ANTLR start "ID"
	public final void mID() throws RecognitionException {
		try {
			int _type = ID;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
			{
			if ( (input.LA(1) >= 'A' && input.LA(1) <= 'Z')||input.LA(1)=='_'||(input.LA(1) >= 'a' && input.LA(1) <= 'z') ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
			loop1:
			while (true) {
				int alt1=2;
				int LA1_0 = input.LA(1);
				if ( ((LA1_0 >= '0' && LA1_0 <= '9')||(LA1_0 >= 'A' && LA1_0 <= 'Z')||LA1_0=='_'||(LA1_0 >= 'a' && LA1_0 <= 'z')) ) {
					alt1=1;
				}

				switch (alt1) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9')||(input.LA(1) >= 'A' && input.LA(1) <= 'Z')||input.LA(1)=='_'||(input.LA(1) >= 'a' && input.LA(1) <= 'z') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					break loop1;
				}
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "ID"

	// $ANTLR start "INT"
	public final void mINT() throws RecognitionException {
		try {
			int _type = INT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:59:5: ( ( '0' .. '9' )+ )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:59:7: ( '0' .. '9' )+
			{
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:59:7: ( '0' .. '9' )+
			int cnt2=0;
			loop2:
			while (true) {
				int alt2=2;
				int LA2_0 = input.LA(1);
				if ( ((LA2_0 >= '0' && LA2_0 <= '9')) ) {
					alt2=1;
				}

				switch (alt2) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					if ( cnt2 >= 1 ) break loop2;
					EarlyExitException eee = new EarlyExitException(2, input);
					throw eee;
				}
				cnt2++;
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "INT"

	// $ANTLR start "FLOAT"
	public final void mFLOAT() throws RecognitionException {
		try {
			int _type = FLOAT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
			int alt9=3;
			alt9 = dfa9.predict(input);
			switch (alt9) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
					{
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:9: ( '0' .. '9' )+
					int cnt3=0;
					loop3:
					while (true) {
						int alt3=2;
						int LA3_0 = input.LA(1);
						if ( ((LA3_0 >= '0' && LA3_0 <= '9')) ) {
							alt3=1;
						}

						switch (alt3) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
							{
							if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
								input.consume();
							}
							else {
								MismatchedSetException mse = new MismatchedSetException(null,input);
								recover(mse);
								throw mse;
							}
							}
							break;

						default :
							if ( cnt3 >= 1 ) break loop3;
							EarlyExitException eee = new EarlyExitException(3, input);
							throw eee;
						}
						cnt3++;
					}

					match('.'); 
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:25: ( '0' .. '9' )*
					loop4:
					while (true) {
						int alt4=2;
						int LA4_0 = input.LA(1);
						if ( ((LA4_0 >= '0' && LA4_0 <= '9')) ) {
							alt4=1;
						}

						switch (alt4) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
							{
							if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
								input.consume();
							}
							else {
								MismatchedSetException mse = new MismatchedSetException(null,input);
								recover(mse);
								throw mse;
							}
							}
							break;

						default :
							break loop4;
						}
					}

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:37: ( EXPONENT )?
					int alt5=2;
					int LA5_0 = input.LA(1);
					if ( (LA5_0=='E'||LA5_0=='e') ) {
						alt5=1;
					}
					switch (alt5) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:37: EXPONENT
							{
							mEXPONENT(); 

							}
							break;

					}

					}
					break;
				case 2 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:64:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
					{
					match('.'); 
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:64:13: ( '0' .. '9' )+
					int cnt6=0;
					loop6:
					while (true) {
						int alt6=2;
						int LA6_0 = input.LA(1);
						if ( ((LA6_0 >= '0' && LA6_0 <= '9')) ) {
							alt6=1;
						}

						switch (alt6) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
							{
							if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
								input.consume();
							}
							else {
								MismatchedSetException mse = new MismatchedSetException(null,input);
								recover(mse);
								throw mse;
							}
							}
							break;

						default :
							if ( cnt6 >= 1 ) break loop6;
							EarlyExitException eee = new EarlyExitException(6, input);
							throw eee;
						}
						cnt6++;
					}

					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:64:25: ( EXPONENT )?
					int alt7=2;
					int LA7_0 = input.LA(1);
					if ( (LA7_0=='E'||LA7_0=='e') ) {
						alt7=1;
					}
					switch (alt7) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:64:25: EXPONENT
							{
							mEXPONENT(); 

							}
							break;

					}

					}
					break;
				case 3 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:65:9: ( '0' .. '9' )+ EXPONENT
					{
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:65:9: ( '0' .. '9' )+
					int cnt8=0;
					loop8:
					while (true) {
						int alt8=2;
						int LA8_0 = input.LA(1);
						if ( ((LA8_0 >= '0' && LA8_0 <= '9')) ) {
							alt8=1;
						}

						switch (alt8) {
						case 1 :
							// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
							{
							if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
								input.consume();
							}
							else {
								MismatchedSetException mse = new MismatchedSetException(null,input);
								recover(mse);
								throw mse;
							}
							}
							break;

						default :
							if ( cnt8 >= 1 ) break loop8;
							EarlyExitException eee = new EarlyExitException(8, input);
							throw eee;
						}
						cnt8++;
					}

					mEXPONENT(); 

					}
					break;

			}
			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "FLOAT"

	// $ANTLR start "WS"
	public final void mWS() throws RecognitionException {
		try {
			int _type = WS;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:9: ( ' ' | '\\t' | '\\r' | '\\n' )
			{
			if ( (input.LA(1) >= '\t' && input.LA(1) <= '\n')||input.LA(1)=='\r'||input.LA(1)==' ' ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			_channel=HIDDEN;
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "WS"

	// $ANTLR start "STRING"
	public final void mSTRING() throws RecognitionException {
		try {
			int _type = STRING;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:76:5: ( '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"' )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:76:8: '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"'
			{
			match('\"'); 
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:76:12: ( ESC_SEQ |~ ( '\\\\' | '\"' ) )*
			loop10:
			while (true) {
				int alt10=3;
				int LA10_0 = input.LA(1);
				if ( (LA10_0=='\\') ) {
					alt10=1;
				}
				else if ( ((LA10_0 >= '\u0000' && LA10_0 <= '!')||(LA10_0 >= '#' && LA10_0 <= '[')||(LA10_0 >= ']' && LA10_0 <= '\uFFFF')) ) {
					alt10=2;
				}

				switch (alt10) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:76:14: ESC_SEQ
					{
					mESC_SEQ(); 

					}
					break;
				case 2 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:76:24: ~ ( '\\\\' | '\"' )
					{
					if ( (input.LA(1) >= '\u0000' && input.LA(1) <= '!')||(input.LA(1) >= '#' && input.LA(1) <= '[')||(input.LA(1) >= ']' && input.LA(1) <= '\uFFFF') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					break loop10;
				}
			}

			match('\"'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "STRING"

	// $ANTLR start "EXPONENT"
	public final void mEXPONENT() throws RecognitionException {
		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:81:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:81:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
			{
			if ( input.LA(1)=='E'||input.LA(1)=='e' ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:81:22: ( '+' | '-' )?
			int alt11=2;
			int LA11_0 = input.LA(1);
			if ( (LA11_0=='+'||LA11_0=='-') ) {
				alt11=1;
			}
			switch (alt11) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
					{
					if ( input.LA(1)=='+'||input.LA(1)=='-' ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

			}

			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:81:33: ( '0' .. '9' )+
			int cnt12=0;
			loop12:
			while (true) {
				int alt12=2;
				int LA12_0 = input.LA(1);
				if ( ((LA12_0 >= '0' && LA12_0 <= '9')) ) {
					alt12=1;
				}

				switch (alt12) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					if ( cnt12 >= 1 ) break loop12;
					EarlyExitException eee = new EarlyExitException(12, input);
					throw eee;
				}
				cnt12++;
			}

			}

		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "EXPONENT"

	// $ANTLR start "HEX_DIGIT"
	public final void mHEX_DIGIT() throws RecognitionException {
		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:84:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
			{
			if ( (input.LA(1) >= '0' && input.LA(1) <= '9')||(input.LA(1) >= 'A' && input.LA(1) <= 'F')||(input.LA(1) >= 'a' && input.LA(1) <= 'f') ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			}

		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "HEX_DIGIT"

	// $ANTLR start "ESC_SEQ"
	public final void mESC_SEQ() throws RecognitionException {
		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:88:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
			int alt13=3;
			int LA13_0 = input.LA(1);
			if ( (LA13_0=='\\') ) {
				switch ( input.LA(2) ) {
				case '\"':
				case '\'':
				case '\\':
				case 'b':
				case 'f':
				case 'n':
				case 'r':
				case 't':
					{
					alt13=1;
					}
					break;
				case 'u':
					{
					alt13=2;
					}
					break;
				case '0':
				case '1':
				case '2':
				case '3':
				case '4':
				case '5':
				case '6':
				case '7':
					{
					alt13=3;
					}
					break;
				default:
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 13, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 13, 0, input);
				throw nvae;
			}

			switch (alt13) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:88:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
					{
					match('\\'); 
					if ( input.LA(1)=='\"'||input.LA(1)=='\''||input.LA(1)=='\\'||input.LA(1)=='b'||input.LA(1)=='f'||input.LA(1)=='n'||input.LA(1)=='r'||input.LA(1)=='t' ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;
				case 2 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:89:9: UNICODE_ESC
					{
					mUNICODE_ESC(); 

					}
					break;
				case 3 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:90:9: OCTAL_ESC
					{
					mOCTAL_ESC(); 

					}
					break;

			}
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "ESC_SEQ"

	// $ANTLR start "OCTAL_ESC"
	public final void mOCTAL_ESC() throws RecognitionException {
		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:95:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
			int alt14=3;
			int LA14_0 = input.LA(1);
			if ( (LA14_0=='\\') ) {
				int LA14_1 = input.LA(2);
				if ( ((LA14_1 >= '0' && LA14_1 <= '3')) ) {
					int LA14_2 = input.LA(3);
					if ( ((LA14_2 >= '0' && LA14_2 <= '7')) ) {
						int LA14_4 = input.LA(4);
						if ( ((LA14_4 >= '0' && LA14_4 <= '7')) ) {
							alt14=1;
						}

						else {
							alt14=2;
						}

					}

					else {
						alt14=3;
					}

				}
				else if ( ((LA14_1 >= '4' && LA14_1 <= '7')) ) {
					int LA14_3 = input.LA(3);
					if ( ((LA14_3 >= '0' && LA14_3 <= '7')) ) {
						alt14=2;
					}

					else {
						alt14=3;
					}

				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 14, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 14, 0, input);
				throw nvae;
			}

			switch (alt14) {
				case 1 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:95:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
					{
					match('\\'); 
					if ( (input.LA(1) >= '0' && input.LA(1) <= '3') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					if ( (input.LA(1) >= '0' && input.LA(1) <= '7') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					if ( (input.LA(1) >= '0' && input.LA(1) <= '7') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;
				case 2 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:96:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
					{
					match('\\'); 
					if ( (input.LA(1) >= '0' && input.LA(1) <= '7') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					if ( (input.LA(1) >= '0' && input.LA(1) <= '7') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;
				case 3 :
					// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:97:9: '\\\\' ( '0' .. '7' )
					{
					match('\\'); 
					if ( (input.LA(1) >= '0' && input.LA(1) <= '7') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

			}
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "OCTAL_ESC"

	// $ANTLR start "UNICODE_ESC"
	public final void mUNICODE_ESC() throws RecognitionException {
		try {
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:102:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
			// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:102:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
			{
			match('\\'); 
			match('u'); 
			mHEX_DIGIT(); 

			mHEX_DIGIT(); 

			mHEX_DIGIT(); 

			mHEX_DIGIT(); 

			}

		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "UNICODE_ESC"

	@Override
	public void mTokens() throws RecognitionException {
		// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:8: ( T__14 | T__15 | T__16 | T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | ID | INT | FLOAT | WS | STRING )
		int alt15=27;
		alt15 = dfa15.predict(input);
		switch (alt15) {
			case 1 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:10: T__14
				{
				mT__14(); 

				}
				break;
			case 2 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:16: T__15
				{
				mT__15(); 

				}
				break;
			case 3 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:22: T__16
				{
				mT__16(); 

				}
				break;
			case 4 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:28: T__17
				{
				mT__17(); 

				}
				break;
			case 5 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:34: T__18
				{
				mT__18(); 

				}
				break;
			case 6 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:40: T__19
				{
				mT__19(); 

				}
				break;
			case 7 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:46: T__20
				{
				mT__20(); 

				}
				break;
			case 8 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:52: T__21
				{
				mT__21(); 

				}
				break;
			case 9 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:58: T__22
				{
				mT__22(); 

				}
				break;
			case 10 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:64: T__23
				{
				mT__23(); 

				}
				break;
			case 11 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:70: T__24
				{
				mT__24(); 

				}
				break;
			case 12 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:76: T__25
				{
				mT__25(); 

				}
				break;
			case 13 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:82: T__26
				{
				mT__26(); 

				}
				break;
			case 14 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:88: T__27
				{
				mT__27(); 

				}
				break;
			case 15 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:94: T__28
				{
				mT__28(); 

				}
				break;
			case 16 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:100: T__29
				{
				mT__29(); 

				}
				break;
			case 17 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:106: T__30
				{
				mT__30(); 

				}
				break;
			case 18 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:112: T__31
				{
				mT__31(); 

				}
				break;
			case 19 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:118: T__32
				{
				mT__32(); 

				}
				break;
			case 20 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:124: T__33
				{
				mT__33(); 

				}
				break;
			case 21 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:130: T__34
				{
				mT__34(); 

				}
				break;
			case 22 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:136: T__35
				{
				mT__35(); 

				}
				break;
			case 23 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:142: ID
				{
				mID(); 

				}
				break;
			case 24 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:145: INT
				{
				mINT(); 

				}
				break;
			case 25 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:149: FLOAT
				{
				mFLOAT(); 

				}
				break;
			case 26 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:155: WS
				{
				mWS(); 

				}
				break;
			case 27 :
				// /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:158: STRING
				{
				mSTRING(); 

				}
				break;

		}
	}


	protected DFA9 dfa9 = new DFA9(this);
	protected DFA15 dfa15 = new DFA15(this);
	static final String DFA9_eotS =
		"\5\uffff";
	static final String DFA9_eofS =
		"\5\uffff";
	static final String DFA9_minS =
		"\2\56\3\uffff";
	static final String DFA9_maxS =
		"\1\71\1\145\3\uffff";
	static final String DFA9_acceptS =
		"\2\uffff\1\2\1\1\1\3";
	static final String DFA9_specialS =
		"\5\uffff}>";
	static final String[] DFA9_transitionS = {
			"\1\2\1\uffff\12\1",
			"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4",
			"",
			"",
			""
	};

	static final short[] DFA9_eot = DFA.unpackEncodedString(DFA9_eotS);
	static final short[] DFA9_eof = DFA.unpackEncodedString(DFA9_eofS);
	static final char[] DFA9_min = DFA.unpackEncodedStringToUnsignedChars(DFA9_minS);
	static final char[] DFA9_max = DFA.unpackEncodedStringToUnsignedChars(DFA9_maxS);
	static final short[] DFA9_accept = DFA.unpackEncodedString(DFA9_acceptS);
	static final short[] DFA9_special = DFA.unpackEncodedString(DFA9_specialS);
	static final short[][] DFA9_transition;

	static {
		int numStates = DFA9_transitionS.length;
		DFA9_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA9_transition[i] = DFA.unpackEncodedString(DFA9_transitionS[i]);
		}
	}

	protected class DFA9 extends DFA {

		public DFA9(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 9;
			this.eot = DFA9_eot;
			this.eof = DFA9_eof;
			this.min = DFA9_min;
			this.max = DFA9_max;
			this.accept = DFA9_accept;
			this.special = DFA9_special;
			this.transition = DFA9_transition;
		}
		@Override
		public String getDescription() {
			return "62:1: FLOAT : ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT );";
		}
	}

	static final String DFA15_eotS =
		"\12\uffff\1\32\2\uffff\5\24\3\uffff\1\41\5\uffff\2\24\1\44\3\24\1\uffff"+
		"\2\24\1\uffff\1\53\2\24\1\56\1\57\1\24\1\uffff\2\24\2\uffff\1\63\1\64"+
		"\1\24\2\uffff\1\24\1\67\1\uffff";
	static final String DFA15_eofS =
		"\70\uffff";
	static final String DFA15_minS =
		"\1\11\11\uffff\1\76\2\uffff\2\154\1\146\1\162\1\141\3\uffff\1\56\5\uffff"+
		"\1\163\1\157\1\60\1\164\1\151\1\162\1\uffff\1\145\1\141\1\uffff\1\60\1"+
		"\156\1\147\2\60\1\164\1\uffff\1\164\1\162\2\uffff\2\60\1\141\2\uffff\1"+
		"\155\1\60\1\uffff";
	static final String DFA15_maxS =
		"\1\175\11\uffff\1\76\2\uffff\2\154\1\156\1\162\1\141\3\uffff\1\145\5\uffff"+
		"\1\163\1\157\1\172\1\164\1\157\1\162\1\uffff\1\145\1\141\1\uffff\1\172"+
		"\1\156\1\147\2\172\1\164\1\uffff\1\164\1\162\2\uffff\2\172\1\141\2\uffff"+
		"\1\155\1\172\1\uffff";
	static final String DFA15_acceptS =
		"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\uffff\1\14\1\15\5\uffff"+
		"\1\25\1\26\1\27\1\uffff\1\31\1\32\1\33\1\13\1\12\6\uffff\1\30\2\uffff"+
		"\1\20\6\uffff\1\21\2\uffff\1\24\1\16\3\uffff\1\17\1\22\2\uffff\1\23";
	static final String DFA15_specialS =
		"\70\uffff}>";
	static final String[] DFA15_transitionS = {
			"\2\27\2\uffff\1\27\22\uffff\1\27\1\uffff\1\30\5\uffff\1\1\1\2\1\3\1\4"+
			"\1\5\1\6\1\26\1\7\12\25\1\10\1\11\1\12\1\13\1\14\2\uffff\32\24\4\uffff"+
			"\1\24\1\uffff\4\24\1\15\1\16\2\24\1\17\6\24\1\20\5\24\1\21\4\24\1\22"+
			"\1\uffff\1\23",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"\1\31",
			"",
			"",
			"\1\33",
			"\1\34",
			"\1\35\7\uffff\1\36",
			"\1\37",
			"\1\40",
			"",
			"",
			"",
			"\1\26\1\uffff\12\25\13\uffff\1\26\37\uffff\1\26",
			"",
			"",
			"",
			"",
			"",
			"\1\42",
			"\1\43",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\1\45",
			"\1\46\5\uffff\1\47",
			"\1\50",
			"",
			"\1\51",
			"\1\52",
			"",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\1\54",
			"\1\55",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\1\60",
			"",
			"\1\61",
			"\1\62",
			"",
			"",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			"\1\65",
			"",
			"",
			"\1\66",
			"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24",
			""
	};

	static final short[] DFA15_eot = DFA.unpackEncodedString(DFA15_eotS);
	static final short[] DFA15_eof = DFA.unpackEncodedString(DFA15_eofS);
	static final char[] DFA15_min = DFA.unpackEncodedStringToUnsignedChars(DFA15_minS);
	static final char[] DFA15_max = DFA.unpackEncodedStringToUnsignedChars(DFA15_maxS);
	static final short[] DFA15_accept = DFA.unpackEncodedString(DFA15_acceptS);
	static final short[] DFA15_special = DFA.unpackEncodedString(DFA15_specialS);
	static final short[][] DFA15_transition;

	static {
		int numStates = DFA15_transitionS.length;
		DFA15_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA15_transition[i] = DFA.unpackEncodedString(DFA15_transitionS[i]);
		}
	}

	protected class DFA15 extends DFA {

		public DFA15(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 15;
			this.eot = DFA15_eot;
			this.eof = DFA15_eof;
			this.min = DFA15_min;
			this.max = DFA15_max;
			this.accept = DFA15_accept;
			this.special = DFA15_special;
			this.transition = DFA15_transition;
		}
		@Override
		public String getDescription() {
			return "1:1: Tokens : ( T__14 | T__15 | T__16 | T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | ID | INT | FLOAT | WS | STRING );";
		}
	}

}
