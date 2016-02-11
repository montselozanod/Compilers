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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ESC_SEQ", "EXPONENT", "FLOAT", "HEX_DIGIT", "ID", "INT", "OCTAL_ESC", 
    "STRING", "UNICODE_ESC", "WS", "'('", "')'", "'*'", "'+'", "','", "'-'", 
    "'/'", "':'", "';'", "'<'", "'<>'", "'='", "'>'", "'else'", "'float'", 
    "'if'", "'int'", "'print'", "'program'", "'var'", "'{'", "'}'"
]




class patitoParser(Parser):
    grammarFileName = "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(patitoParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:1: start : programa EOF ;
    def start(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:7: ( programa EOF )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:9: programa EOF
                pass 
                self._state.following.append(self.FOLLOW_programa_in_start24)
                self.programa()

                self._state.following.pop()

                self.match(self.input, EOF, self.FOLLOW_EOF_in_start26)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "start"



    # $ANTLR start "programa"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: programa : 'program' ID ';' ( vars )? bloque ;
    def programa(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ( 'program' ID ';' ( vars )? bloque )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:11: 'program' ID ';' ( vars )? bloque
                pass 
                self.match(self.input, 32, self.FOLLOW_32_in_programa33)

                self.match(self.input, ID, self.FOLLOW_ID_in_programa35)

                self.match(self.input, 22, self.FOLLOW_22_in_programa37)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:28: ( vars )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 33) :
                    alt1 = 1
                if alt1 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:28: vars
                    pass 
                    self._state.following.append(self.FOLLOW_vars_in_programa39)
                    self.vars()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_bloque_in_programa42)
                self.bloque()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "programa"



    # $ANTLR start "bloque"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:1: bloque : '{' ( estatuto )* '}' ;
    def bloque(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:8: ( '{' ( estatuto )* '}' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:10: '{' ( estatuto )* '}'
                pass 
                self.match(self.input, 34, self.FOLLOW_34_in_bloque50)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: ( estatuto )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID or LA2_0 == 29 or LA2_0 == 31) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: estatuto
                        pass 
                        self._state.following.append(self.FOLLOW_estatuto_in_bloque52)
                        self.estatuto()

                        self._state.following.pop()


                    else:
                        break #loop2


                self.match(self.input, 35, self.FOLLOW_35_in_bloque55)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "bloque"



    # $ANTLR start "estatuto"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:1: estatuto : ( asignacion | escritura | condicion );
    def estatuto(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:9: ( asignacion | escritura | condicion )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == ID:
                    alt3 = 1
                elif LA3 == 31:
                    alt3 = 2
                elif LA3 == 29:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:11: asignacion
                    pass 
                    self._state.following.append(self.FOLLOW_asignacion_in_estatuto62)
                    self.asignacion()

                    self._state.following.pop()


                elif alt3 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:4: escritura
                    pass 
                    self._state.following.append(self.FOLLOW_escritura_in_estatuto67)
                    self.escritura()

                    self._state.following.pop()


                elif alt3 == 3:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:3: condicion
                    pass 
                    self._state.following.append(self.FOLLOW_condicion_in_estatuto71)
                    self.condicion()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "estatuto"



    # $ANTLR start "condicion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:17:1: condicion : 'if' '(' expresion ')' bloque ( condelse )? ';' ;
    def condicion(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:2: ( 'if' '(' expresion ')' bloque ( condelse )? ';' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:4: 'if' '(' expresion ')' bloque ( condelse )? ';'
                pass 
                self.match(self.input, 29, self.FOLLOW_29_in_condicion80)

                self.match(self.input, 14, self.FOLLOW_14_in_condicion82)

                self._state.following.append(self.FOLLOW_expresion_in_condicion84)
                self.expresion()

                self._state.following.pop()

                self.match(self.input, 15, self.FOLLOW_15_in_condicion86)

                self._state.following.append(self.FOLLOW_bloque_in_condicion88)
                self.bloque()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:34: ( condelse )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 27) :
                    alt4 = 1
                if alt4 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:34: condelse
                    pass 
                    self._state.following.append(self.FOLLOW_condelse_in_condicion90)
                    self.condelse()

                    self._state.following.pop()




                self.match(self.input, 22, self.FOLLOW_22_in_condicion93)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "condicion"



    # $ANTLR start "condelse"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:1: condelse : 'else' bloque ;
    def condelse(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:9: ( 'else' bloque )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:20:11: 'else' bloque
                pass 
                self.match(self.input, 27, self.FOLLOW_27_in_condelse100)

                self._state.following.append(self.FOLLOW_bloque_in_condelse102)
                self.bloque()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "condelse"



    # $ANTLR start "asignacion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:22:1: asignacion : ID '=' expresion ';' ;
    def asignacion(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:2: ( ID '=' expresion ';' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:4: ID '=' expresion ';'
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_asignacion111)

                self.match(self.input, 25, self.FOLLOW_25_in_asignacion113)

                self._state.following.append(self.FOLLOW_expresion_in_asignacion115)
                self.expresion()

                self._state.following.pop()

                self.match(self.input, 22, self.FOLLOW_22_in_asignacion117)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "asignacion"



    # $ANTLR start "escritura"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:1: escritura : 'print' '(' stmt ')' ';' ;
    def escritura(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:2: ( 'print' '(' stmt ')' ';' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:4: 'print' '(' stmt ')' ';'
                pass 
                self.match(self.input, 31, self.FOLLOW_31_in_escritura125)

                self.match(self.input, 14, self.FOLLOW_14_in_escritura127)

                self._state.following.append(self.FOLLOW_stmt_in_escritura129)
                self.stmt()

                self._state.following.pop()

                self.match(self.input, 15, self.FOLLOW_15_in_escritura131)

                self.match(self.input, 22, self.FOLLOW_22_in_escritura133)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "escritura"



    # $ANTLR start "stmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:1: stmt : strgstmt ( ',' strgstmt )* ;
    def stmt(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:6: ( strgstmt ( ',' strgstmt )* )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:8: strgstmt ( ',' strgstmt )*
                pass 
                self._state.following.append(self.FOLLOW_strgstmt_in_stmt141)
                self.strgstmt()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:17: ( ',' strgstmt )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 18) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:27:18: ',' strgstmt
                        pass 
                        self.match(self.input, 18, self.FOLLOW_18_in_stmt144)

                        self._state.following.append(self.FOLLOW_strgstmt_in_stmt146)
                        self.strgstmt()

                        self._state.following.pop()


                    else:
                        break #loop5





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "stmt"



    # $ANTLR start "strgstmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:1: strgstmt : ( STRING | expresion );
    def strgstmt(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:9: ( STRING | expresion )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == STRING) :
                    alt6 = 1
                elif (LA6_0 == FLOAT or (ID <= LA6_0 <= INT) or LA6_0 == 14 or LA6_0 == 17 or LA6_0 == 19) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:11: STRING
                    pass 
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_strgstmt155)


                elif alt6 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:20: expresion
                    pass 
                    self._state.following.append(self.FOLLOW_expresion_in_strgstmt159)
                    self.expresion()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "strgstmt"



    # $ANTLR start "expresion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:31:1: expresion : exp ( opexp )? ;
    def expresion(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:2: ( exp ( opexp )? )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:4: exp ( opexp )?
                pass 
                self._state.following.append(self.FOLLOW_exp_in_expresion168)
                self.exp()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:8: ( opexp )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((23 <= LA7_0 <= 24) or LA7_0 == 26) :
                    alt7 = 1
                if alt7 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:8: opexp
                    pass 
                    self._state.following.append(self.FOLLOW_opexp_in_expresion170)
                    self.opexp()

                    self._state.following.pop()







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "expresion"



    # $ANTLR start "opexp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:1: opexp : ( '>' exp | '<' exp | '<>' exp );
    def opexp(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:7: ( '>' exp | '<' exp | '<>' exp )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == 26:
                    alt8 = 1
                elif LA8 == 23:
                    alt8 = 2
                elif LA8 == 24:
                    alt8 = 3
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:9: '>' exp
                    pass 
                    self.match(self.input, 26, self.FOLLOW_26_in_opexp179)

                    self._state.following.append(self.FOLLOW_exp_in_opexp181)
                    self.exp()

                    self._state.following.pop()


                elif alt8 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:4: '<' exp
                    pass 
                    self.match(self.input, 23, self.FOLLOW_23_in_opexp186)

                    self._state.following.append(self.FOLLOW_exp_in_opexp188)
                    self.exp()

                    self._state.following.pop()


                elif alt8 == 3:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:4: '<>' exp
                    pass 
                    self.match(self.input, 24, self.FOLLOW_24_in_opexp193)

                    self._state.following.append(self.FOLLOW_exp_in_opexp195)
                    self.exp()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "opexp"



    # $ANTLR start "exp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:1: exp : termino ( opsum termino )* ;
    def exp(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:5: ( termino ( opsum termino )* )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:7: termino ( opsum termino )*
                pass 
                self._state.following.append(self.FOLLOW_termino_in_exp205)
                self.termino()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:15: ( opsum termino )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 17 or LA9_0 == 19) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:16: opsum termino
                        pass 
                        self._state.following.append(self.FOLLOW_opsum_in_exp208)
                        self.opsum()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_termino_in_exp210)
                        self.termino()

                        self._state.following.pop()


                    else:
                        break #loop9





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "exp"



    # $ANTLR start "factor"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:1: factor : ( '(' expresion ')' | ( opsum )? varcte );
    def factor(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:8: ( '(' expresion ')' | ( opsum )? varcte )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 14) :
                    alt11 = 1
                elif (LA11_0 == FLOAT or (ID <= LA11_0 <= INT) or LA11_0 == 17 or LA11_0 == 19) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:11: '(' expresion ')'
                    pass 
                    self.match(self.input, 14, self.FOLLOW_14_in_factor221)

                    self._state.following.append(self.FOLLOW_expresion_in_factor223)
                    self.expresion()

                    self._state.following.pop()

                    self.match(self.input, 15, self.FOLLOW_15_in_factor225)


                elif alt11 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )? varcte
                    pass 
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 17 or LA10_0 == 19) :
                        alt10 = 1
                    if alt10 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: opsum
                        pass 
                        self._state.following.append(self.FOLLOW_opsum_in_factor230)
                        self.opsum()

                        self._state.following.pop()




                    self._state.following.append(self.FOLLOW_varcte_in_factor233)
                    self.varcte()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "factor"



    # $ANTLR start "termino"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:1: termino : factor ( opmul factor )* ;
    def termino(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:9: ( factor ( opmul factor )* )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:11: factor ( opmul factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_termino242)
                self.factor()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:18: ( opmul factor )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 16 or LA12_0 == 20) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:19: opmul factor
                        pass 
                        self._state.following.append(self.FOLLOW_opmul_in_termino245)
                        self.opmul()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_factor_in_termino247)
                        self.factor()

                        self._state.following.pop()


                    else:
                        break #loop12





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "termino"



    # $ANTLR start "vars"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:1: vars : 'var' ( decl )+ ;
    def vars(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:6: ( 'var' ( decl )+ )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:8: 'var' ( decl )+
                pass 
                self.match(self.input, 33, self.FOLLOW_33_in_vars257)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: ( decl )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ID) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: decl
                        pass 
                        self._state.following.append(self.FOLLOW_decl_in_vars259)
                        self.decl()

                        self._state.following.pop()


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "vars"



    # $ANTLR start "decl"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:1: decl : variabs ':' tipo ';' ;
    def decl(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:6: ( variabs ':' tipo ';' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:48:8: variabs ':' tipo ';'
                pass 
                self._state.following.append(self.FOLLOW_variabs_in_decl268)
                self.variabs()

                self._state.following.pop()

                self.match(self.input, 21, self.FOLLOW_21_in_decl270)

                self._state.following.append(self.FOLLOW_tipo_in_decl272)
                self.tipo()

                self._state.following.pop()

                self.match(self.input, 22, self.FOLLOW_22_in_decl274)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "decl"



    # $ANTLR start "variabs"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:1: variabs : ID ( ',' ID )* ;
    def variabs(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:9: ( ID ( ',' ID )* )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:11: ID ( ',' ID )*
                pass 
                self.match(self.input, ID, self.FOLLOW_ID_in_variabs282)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:14: ( ',' ID )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 18) :
                        alt14 = 1


                    if alt14 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:15: ',' ID
                        pass 
                        self.match(self.input, 18, self.FOLLOW_18_in_variabs285)

                        self.match(self.input, ID, self.FOLLOW_ID_in_variabs287)


                    else:
                        break #loop14





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "variabs"



    # $ANTLR start "varcte"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:1: varcte : ( ID | INT | FLOAT );
    def varcte(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:52:8: ( ID | INT | FLOAT )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                pass 
                if self.input.LA(1) == FLOAT or (ID <= self.input.LA(1) <= INT):
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "varcte"



    # $ANTLR start "tipo"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:1: tipo : ( 'int' | 'float' );
    def tipo(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:54:6: ( 'int' | 'float' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                pass 
                if self.input.LA(1) == 28 or self.input.LA(1) == 30:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "tipo"



    # $ANTLR start "opsum"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:1: opsum : ( '+' | '-' );
    def opsum(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:56:7: ( '+' | '-' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                pass 
                if self.input.LA(1) == 17 or self.input.LA(1) == 19:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "opsum"



    # $ANTLR start "opmul"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:58:1: opmul : ( '*' | '/' );
    def opmul(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:58:7: ( '*' | '/' )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                pass 
                if self.input.LA(1) == 16 or self.input.LA(1) == 20:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "opmul"



 

    FOLLOW_programa_in_start24 = frozenset([])
    FOLLOW_EOF_in_start26 = frozenset([1])
    FOLLOW_32_in_programa33 = frozenset([8])
    FOLLOW_ID_in_programa35 = frozenset([22])
    FOLLOW_22_in_programa37 = frozenset([33, 34])
    FOLLOW_vars_in_programa39 = frozenset([34])
    FOLLOW_bloque_in_programa42 = frozenset([1])
    FOLLOW_34_in_bloque50 = frozenset([8, 29, 31, 35])
    FOLLOW_estatuto_in_bloque52 = frozenset([8, 29, 31, 35])
    FOLLOW_35_in_bloque55 = frozenset([1])
    FOLLOW_asignacion_in_estatuto62 = frozenset([1])
    FOLLOW_escritura_in_estatuto67 = frozenset([1])
    FOLLOW_condicion_in_estatuto71 = frozenset([1])
    FOLLOW_29_in_condicion80 = frozenset([14])
    FOLLOW_14_in_condicion82 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_condicion84 = frozenset([15])
    FOLLOW_15_in_condicion86 = frozenset([34])
    FOLLOW_bloque_in_condicion88 = frozenset([22, 27])
    FOLLOW_condelse_in_condicion90 = frozenset([22])
    FOLLOW_22_in_condicion93 = frozenset([1])
    FOLLOW_27_in_condelse100 = frozenset([34])
    FOLLOW_bloque_in_condelse102 = frozenset([1])
    FOLLOW_ID_in_asignacion111 = frozenset([25])
    FOLLOW_25_in_asignacion113 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_asignacion115 = frozenset([22])
    FOLLOW_22_in_asignacion117 = frozenset([1])
    FOLLOW_31_in_escritura125 = frozenset([14])
    FOLLOW_14_in_escritura127 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_stmt_in_escritura129 = frozenset([15])
    FOLLOW_15_in_escritura131 = frozenset([22])
    FOLLOW_22_in_escritura133 = frozenset([1])
    FOLLOW_strgstmt_in_stmt141 = frozenset([1, 18])
    FOLLOW_18_in_stmt144 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_strgstmt_in_stmt146 = frozenset([1, 18])
    FOLLOW_STRING_in_strgstmt155 = frozenset([1])
    FOLLOW_expresion_in_strgstmt159 = frozenset([1])
    FOLLOW_exp_in_expresion168 = frozenset([1, 23, 24, 26])
    FOLLOW_opexp_in_expresion170 = frozenset([1])
    FOLLOW_26_in_opexp179 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp181 = frozenset([1])
    FOLLOW_23_in_opexp186 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp188 = frozenset([1])
    FOLLOW_24_in_opexp193 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp195 = frozenset([1])
    FOLLOW_termino_in_exp205 = frozenset([1, 17, 19])
    FOLLOW_opsum_in_exp208 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_termino_in_exp210 = frozenset([1, 17, 19])
    FOLLOW_14_in_factor221 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_factor223 = frozenset([15])
    FOLLOW_15_in_factor225 = frozenset([1])
    FOLLOW_opsum_in_factor230 = frozenset([6, 8, 9])
    FOLLOW_varcte_in_factor233 = frozenset([1])
    FOLLOW_factor_in_termino242 = frozenset([1, 16, 20])
    FOLLOW_opmul_in_termino245 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_factor_in_termino247 = frozenset([1, 16, 20])
    FOLLOW_33_in_vars257 = frozenset([8])
    FOLLOW_decl_in_vars259 = frozenset([1, 8])
    FOLLOW_variabs_in_decl268 = frozenset([21])
    FOLLOW_21_in_decl270 = frozenset([28, 30])
    FOLLOW_tipo_in_decl272 = frozenset([22])
    FOLLOW_22_in_decl274 = frozenset([1])
    FOLLOW_ID_in_variabs282 = frozenset([1, 18])
    FOLLOW_18_in_variabs285 = frozenset([8])
    FOLLOW_ID_in_variabs287 = frozenset([1, 18])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("patitoLexer", patitoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
