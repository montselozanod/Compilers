# $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 22:43:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__14=14
T__15=15
T__16=16
T__17=17
T__18=18
T__19=19
T__20=20
T__21=21
T__22=22
T__23=23
T__24=24
T__25=25
T__26=26
T__27=27
T__28=28
T__29=29
T__30=30
T__31=31
T__32=32
T__33=33
T__34=34
T__35=35
ESC_SEQ=4
EXPONENT=5
FLOAT=6
HEX_DIGIT=7
ID=8
INT=9
OCTAL_ESC=10
STRING=11
UNICODE_ESC=12
WS=13


class patitoLexer(Lexer):

    grammarFileName = "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(patitoLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
            )






    # $ANTLR start "T__14"
    def mT__14(self, ):
        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:7: ( '(' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):
        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:7: ( ')' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__15"



    # $ANTLR start "T__16"
    def mT__16(self, ):
        try:
            _type = T__16
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:7: ( '*' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__16"



    # $ANTLR start "T__17"
    def mT__17(self, ):
        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:7: ( '+' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):
        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:7: ( ',' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):
        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:7: ( '-' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):
        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:7: ( '/' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:9: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):
        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:7: ( ':' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):
        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:7: ( ';' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):
        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:7: ( '<' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):
        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:7: ( '<>' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:9: '<>'
            pass 
            self.match("<>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):
        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:7: ( '=' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):
        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:7: ( '>' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):
        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:7: ( 'else' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:9: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):
        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:7: ( 'float' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:9: 'float'
            pass 
            self.match("float")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):
        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:7: ( 'if' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:9: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):
        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:7: ( 'int' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:9: 'int'
            pass 
            self.match("int")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):
        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:7: ( 'print' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:9: 'print'
            pass 
            self.match("print")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):
        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:7: ( 'program' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:9: 'program'
            pass 
            self.match("program")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):
        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:7: ( 'var' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:9: 'var'
            pass 
            self.match("var")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):
        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:7: ( '{' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):
        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:7: ( '}' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__35"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:60:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )* )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:60:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:60:31: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:5: ( ( '0' .. '9' )+ )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:7: ( '0' .. '9' )+
            pass 
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:63:7: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt9 = 3
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                pass 
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:9: ( '0' .. '9' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(46)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:25: ( '0' .. '9' )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop4


                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:37: ( EXPONENT )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 69 or LA5_0 == 101) :
                    alt5 = 1
                if alt5 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:67:37: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt9 == 2:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
                pass 
                self.match(46)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:13: ( '0' .. '9' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 57)) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:25: ( EXPONENT )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 69 or LA7_0 == 101) :
                    alt7 = 1
                if alt7 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:68:25: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt9 == 3:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:69:9: ( '0' .. '9' )+ EXPONENT
                pass 
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:69:9: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((48 <= LA8_0 <= 57)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.mEXPONENT()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:72:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:72:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:80:5: ( '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"' )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:80:8: '\"' ( ESC_SEQ |~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)

            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:80:12: ( ESC_SEQ |~ ( '\\\\' | '\"' ) )*
            while True: #loop10
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 92) :
                    alt10 = 1
                elif ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 91) or (93 <= LA10_0 <= 65535)) :
                    alt10 = 2


                if alt10 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:80:14: ESC_SEQ
                    pass 
                    self.mESC_SEQ()



                elif alt10 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:80:24: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:85:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:85:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:85:22: ( '+' | '-' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 43 or LA11_0 == 45) :
                alt11 = 1
            if alt11 == 1:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:85:33: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)) :
                    alt12 = 1


                if alt12 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:88:11: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "ESC_SEQ"
    def mESC_SEQ(self, ):
        try:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:92:5: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESC | OCTAL_ESC )
            alt13 = 3
            LA13_0 = self.input.LA(1)

            if (LA13_0 == 92) :
                LA13 = self.input.LA(2)
                if LA13 == 34 or LA13 == 39 or LA13 == 92 or LA13 == 98 or LA13 == 102 or LA13 == 110 or LA13 == 114 or LA13 == 116:
                    alt13 = 1
                elif LA13 == 117:
                    alt13 = 2
                elif LA13 == 48 or LA13 == 49 or LA13 == 50 or LA13 == 51 or LA13 == 52 or LA13 == 53 or LA13 == 54 or LA13 == 55:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 13, 0, self.input)

                raise nvae


            if alt13 == 1:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:92:9: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)

                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt13 == 2:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:93:9: UNICODE_ESC
                pass 
                self.mUNICODE_ESC()



            elif alt13 == 3:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:94:9: OCTAL_ESC
                pass 
                self.mOCTAL_ESC()




        finally:
            pass

    # $ANTLR end "ESC_SEQ"



    # $ANTLR start "OCTAL_ESC"
    def mOCTAL_ESC(self, ):
        try:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:99:5: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt14 = 3
            LA14_0 = self.input.LA(1)

            if (LA14_0 == 92) :
                LA14_1 = self.input.LA(2)

                if ((48 <= LA14_1 <= 51)) :
                    LA14_2 = self.input.LA(3)

                    if ((48 <= LA14_2 <= 55)) :
                        LA14_4 = self.input.LA(4)

                        if ((48 <= LA14_4 <= 55)) :
                            alt14 = 1
                        else:
                            alt14 = 2

                    else:
                        alt14 = 3

                elif ((52 <= LA14_1 <= 55)) :
                    LA14_3 = self.input.LA(3)

                    if ((48 <= LA14_3 <= 55)) :
                        alt14 = 2
                    else:
                        alt14 = 3

                else:
                    nvae = NoViableAltException("", 14, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 14, 0, self.input)

                raise nvae


            if alt14 == 1:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:99:9: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 51):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 2:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:100:9: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            elif alt14 == 3:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:101:9: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)

                if (48 <= self.input.LA(1) <= 55):
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse





        finally:
            pass

    # $ANTLR end "OCTAL_ESC"



    # $ANTLR start "UNICODE_ESC"
    def mUNICODE_ESC(self, ):
        try:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:106:5: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:106:9: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)

            self.match(117)

            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()


            self.mHEX_DIGIT()





        finally:
            pass

    # $ANTLR end "UNICODE_ESC"



    def mTokens(self):
        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:8: ( T__14 | T__15 | T__16 | T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | ID | INT | FLOAT | WS | STRING )
        alt15 = 27
        alt15 = self.dfa15.predict(self.input)
        if alt15 == 1:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:10: T__14
            pass 
            self.mT__14()



        elif alt15 == 2:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:16: T__15
            pass 
            self.mT__15()



        elif alt15 == 3:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:22: T__16
            pass 
            self.mT__16()



        elif alt15 == 4:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:28: T__17
            pass 
            self.mT__17()



        elif alt15 == 5:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:34: T__18
            pass 
            self.mT__18()



        elif alt15 == 6:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:40: T__19
            pass 
            self.mT__19()



        elif alt15 == 7:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:46: T__20
            pass 
            self.mT__20()



        elif alt15 == 8:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:52: T__21
            pass 
            self.mT__21()



        elif alt15 == 9:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:58: T__22
            pass 
            self.mT__22()



        elif alt15 == 10:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:64: T__23
            pass 
            self.mT__23()



        elif alt15 == 11:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:70: T__24
            pass 
            self.mT__24()



        elif alt15 == 12:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:76: T__25
            pass 
            self.mT__25()



        elif alt15 == 13:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:82: T__26
            pass 
            self.mT__26()



        elif alt15 == 14:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:88: T__27
            pass 
            self.mT__27()



        elif alt15 == 15:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:94: T__28
            pass 
            self.mT__28()



        elif alt15 == 16:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:100: T__29
            pass 
            self.mT__29()



        elif alt15 == 17:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:106: T__30
            pass 
            self.mT__30()



        elif alt15 == 18:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:112: T__31
            pass 
            self.mT__31()



        elif alt15 == 19:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:118: T__32
            pass 
            self.mT__32()



        elif alt15 == 20:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:124: T__33
            pass 
            self.mT__33()



        elif alt15 == 21:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:130: T__34
            pass 
            self.mT__34()



        elif alt15 == 22:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:136: T__35
            pass 
            self.mT__35()



        elif alt15 == 23:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:142: ID
            pass 
            self.mID()



        elif alt15 == 24:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:145: INT
            pass 
            self.mINT()



        elif alt15 == 25:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:149: FLOAT
            pass 
            self.mFLOAT()



        elif alt15 == 26:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:155: WS
            pass 
            self.mWS()



        elif alt15 == 27:
            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:1:158: STRING
            pass 
            self.mSTRING()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\71\1\145\3\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\3"
        )

    DFA9_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA9_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\12\uffff\1\32\2\uffff\5\24\3\uffff\1\41\5\uffff\2\24\1\44\3\24"
        u"\1\uffff\2\24\1\uffff\1\53\2\24\1\56\1\57\1\24\1\uffff\2\24\2\uffff"
        u"\1\63\1\64\1\24\2\uffff\1\24\1\67\1\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\70\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\11\11\uffff\1\76\2\uffff\2\154\1\146\1\162\1\141\3\uffff\1\56"
        u"\5\uffff\1\163\1\157\1\60\1\164\1\151\1\162\1\uffff\1\145\1\141"
        u"\1\uffff\1\60\1\156\1\147\2\60\1\164\1\uffff\1\164\1\162\2\uffff"
        u"\2\60\1\141\2\uffff\1\155\1\60\1\uffff"
        )

    DFA15_max = DFA.unpack(
        u"\1\175\11\uffff\1\76\2\uffff\2\154\1\156\1\162\1\141\3\uffff\1"
        u"\145\5\uffff\1\163\1\157\1\172\1\164\1\157\1\162\1\uffff\1\145"
        u"\1\141\1\uffff\1\172\1\156\1\147\2\172\1\164\1\uffff\1\164\1\162"
        u"\2\uffff\2\172\1\141\2\uffff\1\155\1\172\1\uffff"
        )

    DFA15_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\uffff\1\14\1\15"
        u"\5\uffff\1\25\1\26\1\27\1\uffff\1\31\1\32\1\33\1\13\1\12\6\uffff"
        u"\1\30\2\uffff\1\20\6\uffff\1\21\2\uffff\1\24\1\16\3\uffff\1\17"
        u"\1\22\2\uffff\1\23"
        )

    DFA15_special = DFA.unpack(
        u"\70\uffff"
        )


    DFA15_transition = [
        DFA.unpack(u"\2\27\2\uffff\1\27\22\uffff\1\27\1\uffff\1\30\5\uffff"
        u"\1\1\1\2\1\3\1\4\1\5\1\6\1\26\1\7\12\25\1\10\1\11\1\12\1\13\1\14"
        u"\2\uffff\32\24\4\uffff\1\24\1\uffff\4\24\1\15\1\16\2\24\1\17\6"
        u"\24\1\20\5\24\1\21\4\24\1\22\1\uffff\1\23"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35\7\uffff\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26\1\uffff\12\25\13\uffff\1\26\37\uffff\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46\5\uffff\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\12\24\7\uffff\32\24\4\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(patitoLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
