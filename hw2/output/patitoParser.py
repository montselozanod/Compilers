# $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 19:56:08

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.debug import *


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
T__36=36
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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ESC_SEQ", "EXPONENT", "FLOAT", "HEX_DIGIT", "ID", "INT", "OCTAL_ESC", 
    "STRING", "UNICODE_ESC", "WS", "'('", "')'", "'*'", "'+'", "','", "'-'", 
    "'/'", "':'", "';'", "'<'", "'<>'", "'='", "'>'", "'else'", "'float'", 
    "'id'", "'if'", "'int'", "'print'", "'program'", "'var'", "'{'", "'}'"
]




class patitoParser(DebugParser):
    grammarFileName = "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        debug_socket = kwargs.pop('debug_socket', None)
        port = kwargs.pop('port', None)
        super(patitoParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self.ruleLevel = 0

	if self._dbg is None:
	    proxy = DebugEventSocketProxy(self, debug=debug_socket, port=port)

	    self.setDebugListener(proxy)
	    proxy.handshake()




    ruleNames = [
        "invalidRule", "decl", "condicion", "escritura", "factor", "opsum", 
        "exp", "expresion", "varcte", "tipo", "stmt", "opexp", "estatuto", 
        "variabs", "asignacion", "strgstmt", "termino", "vars", "condelse", 
        "parse", "programa", "bloque", "opmul"
        ]

    decisionCanBacktrack = [
        False, # invalid decision
        False, False, False, False, False, False, False, False, False, False, 
            False, False, False
        ]
     
    def getRuleLevel(self):
        return self.ruleLevel

    def incRuleLevel(self):
        self.ruleLevel += 1

    def decRuleLevel(self):
        self.ruleLevel -= 1

    def evalPredicate(self, result, predicate):
        self._dbg.semanticPredicate(result, predicate)
        return result





    # $ANTLR start "parse"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:1: parse : programa EOF ;
    def parse(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "parse")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(7, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:7: ( programa EOF )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:9: programa EOF
                    pass 
                    self._dbg.location(7, 9)
                    self._state.following.append(self.FOLLOW_programa_in_parse22)
                    self.programa()

                    self._state.following.pop()
                    self._dbg.location(7, 18)
                    self.match(self.input, EOF, self.FOLLOW_EOF_in_parse24)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(7, 20+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "parse")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "parse"



    # $ANTLR start "programa"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: programa : 'program' 'id' ';' ( vars )? bloque ;
    def programa(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "programa")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(9, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ( 'program' 'id' ';' ( vars )? bloque )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:11: 'program' 'id' ';' ( vars )? bloque
                    pass 
                    self._dbg.location(9, 11)
                    self.match(self.input, 33, self.FOLLOW_33_in_programa31)
                    self._dbg.location(9, 21)
                    self.match(self.input, 29, self.FOLLOW_29_in_programa33)
                    self._dbg.location(9, 26)
                    self.match(self.input, 22, self.FOLLOW_22_in_programa35)
                    self._dbg.location(9, 30)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:30: ( vars )?
                    alt1 = 2
                    try:
                        self._dbg.enterSubRule(1)
                        try:
                            self._dbg.enterDecision(
                                1, self.decisionCanBacktrack[1])
                            LA1_0 = self.input.LA(1)

                            if (LA1_0 == 34) :
                                alt1 = 1
                        finally:
                            self._dbg.exitDecision(1)
                        if alt1 == 1:
                            self._dbg.enterAlt(1)

                            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:30: vars
                            pass 
                            self._dbg.location(9, 30)
                            self._state.following.append(self.FOLLOW_vars_in_programa37)
                            self.vars()

                            self._state.following.pop()



                    finally:
                        self._dbg.exitSubRule(1)
                    self._dbg.location(9, 36)
                    self._state.following.append(self.FOLLOW_bloque_in_programa40)
                    self.bloque()

                    self._state.following.pop()




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(9, 41+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "programa")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "programa"



    # $ANTLR start "bloque"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:1: bloque : '{' ( estatuto )* '}' ;
    def bloque(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "bloque")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(11, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:8: ( '{' ( estatuto )* '}' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:10: '{' ( estatuto )* '}'
                    pass 
                    self._dbg.location(11, 10)
                    self.match(self.input, 35, self.FOLLOW_35_in_bloque48)
                    self._dbg.location(11, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: ( estatuto )*
                    try:
                        self._dbg.enterSubRule(2)
                        while True: #loop2
                            alt2 = 2
                            try:
                                self._dbg.enterDecision(
                                    2, self.decisionCanBacktrack[2])
                                LA2_0 = self.input.LA(1)

                                if (LA2_0 == ID or LA2_0 == 30 or LA2_0 == 32) :
                                    alt2 = 1


                            finally:
                                self._dbg.exitDecision(2)
                            if alt2 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: estatuto
                                pass 
                                self._dbg.location(11, 14)
                                self._state.following.append(self.FOLLOW_estatuto_in_bloque50)
                                self.estatuto()

                                self._state.following.pop()


                            else:
                                break #loop2

                    finally:
                        self._dbg.exitSubRule(2)

                    self._dbg.location(11, 24)
                    self.match(self.input, 36, self.FOLLOW_36_in_bloque53)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(11, 26+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "bloque")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "bloque"



    # $ANTLR start "estatuto"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:1: estatuto : ( asignacion | escritura | condicion );
    def estatuto(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "estatuto")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(13, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:9: ( asignacion | escritura | condicion )
                    alt3 = 3
                    try:
                        self._dbg.enterDecision(
                            3, self.decisionCanBacktrack[3])
                        LA3 = self.input.LA(1)
                        if LA3 == ID:
                            alt3 = 1
                        elif LA3 == 32:
                            alt3 = 2
                        elif LA3 == 30:
                            alt3 = 3
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            self._dbg.recognitionException(nvae)
                            raise nvae


                    finally:
                        self._dbg.exitDecision(3)
                    if alt3 == 1:
                        self._dbg.enterAlt(1)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:11: asignacion
                        pass 
                        self._dbg.location(13, 11)
                        self._state.following.append(self.FOLLOW_asignacion_in_estatuto60)
                        self.asignacion()

                        self._state.following.pop()


                    elif alt3 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:4: escritura
                        pass 
                        self._dbg.location(14, 4)
                        self._state.following.append(self.FOLLOW_escritura_in_estatuto65)
                        self.escritura()

                        self._state.following.pop()


                    elif alt3 == 3:
                        self._dbg.enterAlt(3)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:3: condicion
                        pass 
                        self._dbg.location(15, 3)
                        self._state.following.append(self.FOLLOW_condicion_in_estatuto69)
                        self.condicion()

                        self._state.following.pop()



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(15, 11+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "estatuto")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "estatuto"



    # $ANTLR start "condicion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:1: condicion : 'if' '(' expresion ')' bloque ( condelse )? ';' ;
    def condicion(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "condicion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(17, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:2: ( 'if' '(' expresion ')' bloque ( condelse )? ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:4: 'if' '(' expresion ')' bloque ( condelse )? ';'
                    pass 
                    self._dbg.location(18, 4)
                    self.match(self.input, 30, self.FOLLOW_30_in_condicion78)
                    self._dbg.location(18, 9)
                    self.match(self.input, 14, self.FOLLOW_14_in_condicion80)
                    self._dbg.location(18, 13)
                    self._state.following.append(self.FOLLOW_expresion_in_condicion82)
                    self.expresion()

                    self._state.following.pop()
                    self._dbg.location(18, 23)
                    self.match(self.input, 15, self.FOLLOW_15_in_condicion84)
                    self._dbg.location(18, 27)
                    self._state.following.append(self.FOLLOW_bloque_in_condicion86)
                    self.bloque()

                    self._state.following.pop()
                    self._dbg.location(18, 34)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:34: ( condelse )?
                    alt4 = 2
                    try:
                        self._dbg.enterSubRule(4)
                        try:
                            self._dbg.enterDecision(
                                4, self.decisionCanBacktrack[4])
                            LA4_0 = self.input.LA(1)

                            if (LA4_0 == 27) :
                                alt4 = 1
                        finally:
                            self._dbg.exitDecision(4)
                        if alt4 == 1:
                            self._dbg.enterAlt(1)

                            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:34: condelse
                            pass 
                            self._dbg.location(18, 34)
                            self._state.following.append(self.FOLLOW_condelse_in_condicion88)
                            self.condelse()

                            self._state.following.pop()



                    finally:
                        self._dbg.exitSubRule(4)
                    self._dbg.location(18, 44)
                    self.match(self.input, 22, self.FOLLOW_22_in_condicion91)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(18, 46+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "condicion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "condicion"



    # $ANTLR start "condelse"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:1: condelse : 'else' bloque ;
    def condelse(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "condelse")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(20, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:9: ( 'else' bloque )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:11: 'else' bloque
                    pass 
                    self._dbg.location(20, 11)
                    self.match(self.input, 27, self.FOLLOW_27_in_condelse98)
                    self._dbg.location(20, 18)
                    self._state.following.append(self.FOLLOW_bloque_in_condelse100)
                    self.bloque()

                    self._state.following.pop()




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(20, 23+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "condelse")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "condelse"



    # $ANTLR start "asignacion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:1: asignacion : ID '=' expresion ';' ;
    def asignacion(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "asignacion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(22, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:2: ( ID '=' expresion ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:4: ID '=' expresion ';'
                    pass 
                    self._dbg.location(23, 4)
                    self.match(self.input, ID, self.FOLLOW_ID_in_asignacion109)
                    self._dbg.location(23, 7)
                    self.match(self.input, 25, self.FOLLOW_25_in_asignacion111)
                    self._dbg.location(23, 11)
                    self._state.following.append(self.FOLLOW_expresion_in_asignacion113)
                    self.expresion()

                    self._state.following.pop()
                    self._dbg.location(23, 21)
                    self.match(self.input, 22, self.FOLLOW_22_in_asignacion115)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(23, 23+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "asignacion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "asignacion"



    # $ANTLR start "escritura"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:1: escritura : 'print' '(' stmt ')' ';' ;
    def escritura(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "escritura")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(24, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:2: ( 'print' '(' stmt ')' ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:4: 'print' '(' stmt ')' ';'
                    pass 
                    self._dbg.location(25, 4)
                    self.match(self.input, 32, self.FOLLOW_32_in_escritura123)
                    self._dbg.location(25, 12)
                    self.match(self.input, 14, self.FOLLOW_14_in_escritura125)
                    self._dbg.location(25, 16)
                    self._state.following.append(self.FOLLOW_stmt_in_escritura127)
                    self.stmt()

                    self._state.following.pop()
                    self._dbg.location(25, 21)
                    self.match(self.input, 15, self.FOLLOW_15_in_escritura129)
                    self._dbg.location(25, 25)
                    self.match(self.input, 22, self.FOLLOW_22_in_escritura131)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(25, 27+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "escritura")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "escritura"



    # $ANTLR start "stmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:1: stmt : strgstmt ( ',' strgstmt )* ;
    def stmt(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "stmt")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(27, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:6: ( strgstmt ( ',' strgstmt )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:8: strgstmt ( ',' strgstmt )*
                    pass 
                    self._dbg.location(27, 8)
                    self._state.following.append(self.FOLLOW_strgstmt_in_stmt139)
                    self.strgstmt()

                    self._state.following.pop()
                    self._dbg.location(27, 17)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:17: ( ',' strgstmt )*
                    try:
                        self._dbg.enterSubRule(5)
                        while True: #loop5
                            alt5 = 2
                            try:
                                self._dbg.enterDecision(
                                    5, self.decisionCanBacktrack[5])
                                LA5_0 = self.input.LA(1)

                                if (LA5_0 == 18) :
                                    alt5 = 1


                            finally:
                                self._dbg.exitDecision(5)
                            if alt5 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:18: ',' strgstmt
                                pass 
                                self._dbg.location(27, 18)
                                self.match(self.input, 18, self.FOLLOW_18_in_stmt142)
                                self._dbg.location(27, 22)
                                self._state.following.append(self.FOLLOW_strgstmt_in_stmt144)
                                self.strgstmt()

                                self._state.following.pop()


                            else:
                                break #loop5

                    finally:
                        self._dbg.exitSubRule(5)





                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(27, 31+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "stmt")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "stmt"



    # $ANTLR start "strgstmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:1: strgstmt : ( STRING | expresion );
    def strgstmt(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "strgstmt")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(29, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:9: ( STRING | expresion )
                    alt6 = 2
                    try:
                        self._dbg.enterDecision(
                            6, self.decisionCanBacktrack[6])
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == STRING) :
                            alt6 = 1
                        elif (LA6_0 == FLOAT or (ID <= LA6_0 <= INT) or LA6_0 == 14 or LA6_0 == 17 or LA6_0 == 19) :
                            alt6 = 2
                        else:
                            nvae = NoViableAltException("", 6, 0, self.input)

                            self._dbg.recognitionException(nvae)
                            raise nvae


                    finally:
                        self._dbg.exitDecision(6)
                    if alt6 == 1:
                        self._dbg.enterAlt(1)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:11: STRING
                        pass 
                        self._dbg.location(29, 11)
                        self.match(self.input, STRING, self.FOLLOW_STRING_in_strgstmt153)


                    elif alt6 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:20: expresion
                        pass 
                        self._dbg.location(29, 20)
                        self._state.following.append(self.FOLLOW_expresion_in_strgstmt157)
                        self.expresion()

                        self._state.following.pop()



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(29, 28+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "strgstmt")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "strgstmt"



    # $ANTLR start "expresion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:31:1: expresion : exp opexp ;
    def expresion(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "expresion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(31, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:2: ( exp opexp )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:4: exp opexp
                    pass 
                    self._dbg.location(32, 4)
                    self._state.following.append(self.FOLLOW_exp_in_expresion166)
                    self.exp()

                    self._state.following.pop()
                    self._dbg.location(32, 8)
                    self._state.following.append(self.FOLLOW_opexp_in_expresion168)
                    self.opexp()

                    self._state.following.pop()




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(32, 12+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "expresion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "expresion"



    # $ANTLR start "opexp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:1: opexp : ( '>' exp | '<' exp | '<>' exp );
    def opexp(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opexp")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(34, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:7: ( '>' exp | '<' exp | '<>' exp )
                    alt7 = 3
                    try:
                        self._dbg.enterDecision(
                            7, self.decisionCanBacktrack[7])
                        LA7 = self.input.LA(1)
                        if LA7 == 26:
                            alt7 = 1
                        elif LA7 == 23:
                            alt7 = 2
                        elif LA7 == 24:
                            alt7 = 3
                        else:
                            nvae = NoViableAltException("", 7, 0, self.input)

                            self._dbg.recognitionException(nvae)
                            raise nvae


                    finally:
                        self._dbg.exitDecision(7)
                    if alt7 == 1:
                        self._dbg.enterAlt(1)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:9: '>' exp
                        pass 
                        self._dbg.location(34, 9)
                        self.match(self.input, 26, self.FOLLOW_26_in_opexp176)
                        self._dbg.location(34, 13)
                        self._state.following.append(self.FOLLOW_exp_in_opexp178)
                        self.exp()

                        self._state.following.pop()


                    elif alt7 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:4: '<' exp
                        pass 
                        self._dbg.location(35, 4)
                        self.match(self.input, 23, self.FOLLOW_23_in_opexp183)
                        self._dbg.location(35, 8)
                        self._state.following.append(self.FOLLOW_exp_in_opexp185)
                        self.exp()

                        self._state.following.pop()


                    elif alt7 == 3:
                        self._dbg.enterAlt(3)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:4: '<>' exp
                        pass 
                        self._dbg.location(36, 4)
                        self.match(self.input, 24, self.FOLLOW_24_in_opexp190)
                        self._dbg.location(36, 9)
                        self._state.following.append(self.FOLLOW_exp_in_opexp192)
                        self.exp()

                        self._state.following.pop()



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(37, 1+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opexp")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "opexp"



    # $ANTLR start "exp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:1: exp : termino ( opsum termino )* ;
    def exp(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "exp")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(39, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:5: ( termino ( opsum termino )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:7: termino ( opsum termino )*
                    pass 
                    self._dbg.location(39, 7)
                    self._state.following.append(self.FOLLOW_termino_in_exp202)
                    self.termino()

                    self._state.following.pop()
                    self._dbg.location(39, 15)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:15: ( opsum termino )*
                    try:
                        self._dbg.enterSubRule(8)
                        while True: #loop8
                            alt8 = 2
                            try:
                                self._dbg.enterDecision(
                                    8, self.decisionCanBacktrack[8])
                                LA8_0 = self.input.LA(1)

                                if (LA8_0 == 17 or LA8_0 == 19) :
                                    alt8 = 1


                            finally:
                                self._dbg.exitDecision(8)
                            if alt8 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:16: opsum termino
                                pass 
                                self._dbg.location(39, 16)
                                self._state.following.append(self.FOLLOW_opsum_in_exp205)
                                self.opsum()

                                self._state.following.pop()
                                self._dbg.location(39, 22)
                                self._state.following.append(self.FOLLOW_termino_in_exp207)
                                self.termino()

                                self._state.following.pop()


                            else:
                                break #loop8

                    finally:
                        self._dbg.exitSubRule(8)





                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(39, 30+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "exp")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "exp"



    # $ANTLR start "factor"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:1: factor : ( '(' expresion ')' | ( opsum )? varcte );
    def factor(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "factor")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(41, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:8: ( '(' expresion ')' | ( opsum )? varcte )
                    alt10 = 2
                    try:
                        self._dbg.enterDecision(
                            10, self.decisionCanBacktrack[10])
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == 14) :
                            alt10 = 1
                        elif (LA10_0 == FLOAT or (ID <= LA10_0 <= INT) or LA10_0 == 17 or LA10_0 == 19) :
                            alt10 = 2
                        else:
                            nvae = NoViableAltException("", 10, 0, self.input)

                            self._dbg.recognitionException(nvae)
                            raise nvae


                    finally:
                        self._dbg.exitDecision(10)
                    if alt10 == 1:
                        self._dbg.enterAlt(1)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:11: '(' expresion ')'
                        pass 
                        self._dbg.location(41, 11)
                        self.match(self.input, 14, self.FOLLOW_14_in_factor218)
                        self._dbg.location(41, 15)
                        self._state.following.append(self.FOLLOW_expresion_in_factor220)
                        self.expresion()

                        self._state.following.pop()
                        self._dbg.location(41, 25)
                        self.match(self.input, 15, self.FOLLOW_15_in_factor222)


                    elif alt10 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )? varcte
                        pass 
                        self._dbg.location(42, 4)
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )?
                        alt9 = 2
                        try:
                            self._dbg.enterSubRule(9)
                            try:
                                self._dbg.enterDecision(
                                    9, self.decisionCanBacktrack[9])
                                LA9_0 = self.input.LA(1)

                                if (LA9_0 == 17 or LA9_0 == 19) :
                                    alt9 = 1
                            finally:
                                self._dbg.exitDecision(9)
                            if alt9 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: opsum
                                pass 
                                self._dbg.location(42, 4)
                                self._state.following.append(self.FOLLOW_opsum_in_factor227)
                                self.opsum()

                                self._state.following.pop()



                        finally:
                            self._dbg.exitSubRule(9)
                        self._dbg.location(42, 11)
                        self._state.following.append(self.FOLLOW_varcte_in_factor230)
                        self.varcte()

                        self._state.following.pop()



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(42, 16+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "factor")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "factor"



    # $ANTLR start "termino"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:1: termino : factor ( opmul factor )* ;
    def termino(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "termino")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(44, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:9: ( factor ( opmul factor )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:11: factor ( opmul factor )*
                    pass 
                    self._dbg.location(44, 11)
                    self._state.following.append(self.FOLLOW_factor_in_termino239)
                    self.factor()

                    self._state.following.pop()
                    self._dbg.location(44, 18)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:18: ( opmul factor )*
                    try:
                        self._dbg.enterSubRule(11)
                        while True: #loop11
                            alt11 = 2
                            try:
                                self._dbg.enterDecision(
                                    11, self.decisionCanBacktrack[11])
                                LA11_0 = self.input.LA(1)

                                if (LA11_0 == 16 or LA11_0 == 20) :
                                    alt11 = 1


                            finally:
                                self._dbg.exitDecision(11)
                            if alt11 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:19: opmul factor
                                pass 
                                self._dbg.location(44, 19)
                                self._state.following.append(self.FOLLOW_opmul_in_termino242)
                                self.opmul()

                                self._state.following.pop()
                                self._dbg.location(44, 25)
                                self._state.following.append(self.FOLLOW_factor_in_termino244)
                                self.factor()

                                self._state.following.pop()


                            else:
                                break #loop11

                    finally:
                        self._dbg.exitSubRule(11)





                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(44, 32+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "termino")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "termino"



    # $ANTLR start "vars"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:1: vars : 'var' ( decl )+ ;
    def vars(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "vars")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(46, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:6: ( 'var' ( decl )+ )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:8: 'var' ( decl )+
                    pass 
                    self._dbg.location(46, 8)
                    self.match(self.input, 34, self.FOLLOW_34_in_vars254)
                    self._dbg.location(46, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: ( decl )+
                    cnt12 = 0
                    try:
                        self._dbg.enterSubRule(12)
                        while True: #loop12
                            alt12 = 2
                            try:
                                self._dbg.enterDecision(
                                    12, self.decisionCanBacktrack[12])
                                LA12_0 = self.input.LA(1)

                                if (LA12_0 == ID) :
                                    alt12 = 1


                            finally:
                                self._dbg.exitDecision(12)
                            if alt12 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: decl
                                pass 
                                self._dbg.location(46, 14)
                                self._state.following.append(self.FOLLOW_decl_in_vars256)
                                self.decl()

                                self._state.following.pop()


                            else:
                                if cnt12 >= 1:
                                    break #loop12

                                eee = EarlyExitException(12, self.input)
                                self._dbg.recognitionException(eee)

                                raise eee

                            cnt12 += 1

                    finally:
                        self._dbg.exitSubRule(12)





                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(46, 18+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "vars")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "vars"



    # $ANTLR start "decl"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:1: decl : variabs ':' tipo ';' ;
    def decl(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "decl")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(48, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:6: ( variabs ':' tipo ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:8: variabs ':' tipo ';'
                    pass 
                    self._dbg.location(48, 8)
                    self._state.following.append(self.FOLLOW_variabs_in_decl265)
                    self.variabs()

                    self._state.following.pop()
                    self._dbg.location(48, 16)
                    self.match(self.input, 21, self.FOLLOW_21_in_decl267)
                    self._dbg.location(48, 20)
                    self._state.following.append(self.FOLLOW_tipo_in_decl269)
                    self.tipo()

                    self._state.following.pop()
                    self._dbg.location(48, 25)
                    self.match(self.input, 22, self.FOLLOW_22_in_decl271)




                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(48, 27+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "decl")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "decl"



    # $ANTLR start "variabs"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:1: variabs : ID ( ',' ID )* ;
    def variabs(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "variabs")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(50, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:9: ( ID ( ',' ID )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:11: ID ( ',' ID )*
                    pass 
                    self._dbg.location(50, 11)
                    self.match(self.input, ID, self.FOLLOW_ID_in_variabs279)
                    self._dbg.location(50, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:14: ( ',' ID )*
                    try:
                        self._dbg.enterSubRule(13)
                        while True: #loop13
                            alt13 = 2
                            try:
                                self._dbg.enterDecision(
                                    13, self.decisionCanBacktrack[13])
                                LA13_0 = self.input.LA(1)

                                if (LA13_0 == 18) :
                                    alt13 = 1


                            finally:
                                self._dbg.exitDecision(13)
                            if alt13 == 1:
                                self._dbg.enterAlt(1)

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:15: ',' ID
                                pass 
                                self._dbg.location(50, 15)
                                self.match(self.input, 18, self.FOLLOW_18_in_variabs282)
                                self._dbg.location(50, 19)
                                self.match(self.input, ID, self.FOLLOW_ID_in_variabs284)


                            else:
                                break #loop13

                    finally:
                        self._dbg.exitSubRule(13)





                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(50, 22+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "variabs")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "variabs"



    # $ANTLR start "varcte"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:1: varcte : ( ID | INT | FLOAT );
    def varcte(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "varcte")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(52, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:8: ( ID | INT | FLOAT )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    self._dbg.location(52, 8)
                    if self.input.LA(1) == FLOAT or (ID <= self.input.LA(1) <= INT):
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse






                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(52, 21+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "varcte")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "varcte"



    # $ANTLR start "tipo"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:1: tipo : ( 'int' | 'float' );
    def tipo(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "tipo")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(54, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:6: ( 'int' | 'float' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    self._dbg.location(54, 6)
                    if self.input.LA(1) == 28 or self.input.LA(1) == 31:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse






                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(54, 20+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "tipo")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "tipo"



    # $ANTLR start "opsum"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:1: opsum : ( '+' | '-' );
    def opsum(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opsum")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(56, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:7: ( '+' | '-' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    self._dbg.location(56, 7)
                    if self.input.LA(1) == 17 or self.input.LA(1) == 19:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse






                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(56, 15+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opsum")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "opsum"



    # $ANTLR start "opmul"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:58:1: opmul : ( '*' | '/' );
    def opmul(self, ):
        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opmul")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(58, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:58:7: ( '*' | '/' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    self._dbg.location(58, 7)
                    if self.input.LA(1) == 16 or self.input.LA(1) == 20:
                        self.input.consume()
                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse






                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)

            finally:
                pass

            self._dbg.location(58, 15+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opmul")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return 

    # $ANTLR end "opmul"



 

    FOLLOW_programa_in_parse22 = frozenset([])
    FOLLOW_EOF_in_parse24 = frozenset([1])
    FOLLOW_33_in_programa31 = frozenset([29])
    FOLLOW_29_in_programa33 = frozenset([22])
    FOLLOW_22_in_programa35 = frozenset([34, 35])
    FOLLOW_vars_in_programa37 = frozenset([35])
    FOLLOW_bloque_in_programa40 = frozenset([1])
    FOLLOW_35_in_bloque48 = frozenset([8, 30, 32, 36])
    FOLLOW_estatuto_in_bloque50 = frozenset([8, 30, 32, 36])
    FOLLOW_36_in_bloque53 = frozenset([1])
    FOLLOW_asignacion_in_estatuto60 = frozenset([1])
    FOLLOW_escritura_in_estatuto65 = frozenset([1])
    FOLLOW_condicion_in_estatuto69 = frozenset([1])
    FOLLOW_30_in_condicion78 = frozenset([14])
    FOLLOW_14_in_condicion80 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_condicion82 = frozenset([15])
    FOLLOW_15_in_condicion84 = frozenset([35])
    FOLLOW_bloque_in_condicion86 = frozenset([22, 27])
    FOLLOW_condelse_in_condicion88 = frozenset([22])
    FOLLOW_22_in_condicion91 = frozenset([1])
    FOLLOW_27_in_condelse98 = frozenset([35])
    FOLLOW_bloque_in_condelse100 = frozenset([1])
    FOLLOW_ID_in_asignacion109 = frozenset([25])
    FOLLOW_25_in_asignacion111 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_asignacion113 = frozenset([22])
    FOLLOW_22_in_asignacion115 = frozenset([1])
    FOLLOW_32_in_escritura123 = frozenset([14])
    FOLLOW_14_in_escritura125 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_stmt_in_escritura127 = frozenset([15])
    FOLLOW_15_in_escritura129 = frozenset([22])
    FOLLOW_22_in_escritura131 = frozenset([1])
    FOLLOW_strgstmt_in_stmt139 = frozenset([1, 18])
    FOLLOW_18_in_stmt142 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_strgstmt_in_stmt144 = frozenset([1, 18])
    FOLLOW_STRING_in_strgstmt153 = frozenset([1])
    FOLLOW_expresion_in_strgstmt157 = frozenset([1])
    FOLLOW_exp_in_expresion166 = frozenset([23, 24, 26])
    FOLLOW_opexp_in_expresion168 = frozenset([1])
    FOLLOW_26_in_opexp176 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp178 = frozenset([1])
    FOLLOW_23_in_opexp183 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp185 = frozenset([1])
    FOLLOW_24_in_opexp190 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp192 = frozenset([1])
    FOLLOW_termino_in_exp202 = frozenset([1, 17, 19])
    FOLLOW_opsum_in_exp205 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_termino_in_exp207 = frozenset([1, 17, 19])
    FOLLOW_14_in_factor218 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_factor220 = frozenset([15])
    FOLLOW_15_in_factor222 = frozenset([1])
    FOLLOW_opsum_in_factor227 = frozenset([6, 8, 9])
    FOLLOW_varcte_in_factor230 = frozenset([1])
    FOLLOW_factor_in_termino239 = frozenset([1, 16, 20])
    FOLLOW_opmul_in_termino242 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_factor_in_termino244 = frozenset([1, 16, 20])
    FOLLOW_34_in_vars254 = frozenset([8])
    FOLLOW_decl_in_vars256 = frozenset([1, 8])
    FOLLOW_variabs_in_decl265 = frozenset([21])
    FOLLOW_21_in_decl267 = frozenset([28, 31])
    FOLLOW_tipo_in_decl269 = frozenset([22])
    FOLLOW_22_in_decl271 = frozenset([1])
    FOLLOW_ID_in_variabs279 = frozenset([1, 18])
    FOLLOW_18_in_variabs282 = frozenset([8])
    FOLLOW_ID_in_variabs284 = frozenset([1, 18])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("patitoLexer", patitoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
