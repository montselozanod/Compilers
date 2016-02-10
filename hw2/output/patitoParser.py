# $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 14:21:26

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




class patitoParser(Parser):
    grammarFileName = "/Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(patitoParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "parse"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:1: parse : programa EOF ;
    def parse(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:7: ( programa EOF )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:7:9: programa EOF
                pass 
                self._state.following.append(self.FOLLOW_programa_in_parse22)
                self.programa()

                self._state.following.pop()

                self.match(self.input, EOF, self.FOLLOW_EOF_in_parse24)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "parse"



    # $ANTLR start "programa"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:1: programa : 'program' 'id' ';' ( vars )? bloque ;
    def programa(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:9: ( 'program' 'id' ';' ( vars )? bloque )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:11: 'program' 'id' ';' ( vars )? bloque
                pass 
                self.match(self.input, 33, self.FOLLOW_33_in_programa31)

                self.match(self.input, 29, self.FOLLOW_29_in_programa33)

                self.match(self.input, 22, self.FOLLOW_22_in_programa35)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:30: ( vars )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 34) :
                    alt1 = 1
                if alt1 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:9:30: vars
                    pass 
                    self._state.following.append(self.FOLLOW_vars_in_programa37)
                    self.vars()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_bloque_in_programa40)
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
                self.match(self.input, 35, self.FOLLOW_35_in_bloque48)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: ( estatuto )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID or LA2_0 == 30 or LA2_0 == 32) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:11:14: estatuto
                        pass 
                        self._state.following.append(self.FOLLOW_estatuto_in_bloque50)
                        self.estatuto()

                        self._state.following.pop()


                    else:
                        break #loop2


                self.match(self.input, 36, self.FOLLOW_36_in_bloque53)




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
                elif LA3 == 32:
                    alt3 = 2
                elif LA3 == 30:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:13:11: asignacion
                    pass 
                    self._state.following.append(self.FOLLOW_asignacion_in_estatuto60)
                    self.asignacion()

                    self._state.following.pop()


                elif alt3 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:4: escritura
                    pass 
                    self._state.following.append(self.FOLLOW_escritura_in_estatuto65)
                    self.escritura()

                    self._state.following.pop()


                elif alt3 == 3:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:3: condicion
                    pass 
                    self._state.following.append(self.FOLLOW_condicion_in_estatuto69)
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
                self.match(self.input, 30, self.FOLLOW_30_in_condicion78)

                self.match(self.input, 14, self.FOLLOW_14_in_condicion80)

                self._state.following.append(self.FOLLOW_expresion_in_condicion82)
                self.expresion()

                self._state.following.pop()

                self.match(self.input, 15, self.FOLLOW_15_in_condicion84)

                self._state.following.append(self.FOLLOW_bloque_in_condicion86)
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
                    self._state.following.append(self.FOLLOW_condelse_in_condicion88)
                    self.condelse()

                    self._state.following.pop()




                self.match(self.input, 22, self.FOLLOW_22_in_condicion91)




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
                self.match(self.input, 27, self.FOLLOW_27_in_condelse98)

                self._state.following.append(self.FOLLOW_bloque_in_condelse100)
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
                self.match(self.input, ID, self.FOLLOW_ID_in_asignacion109)

                self.match(self.input, 25, self.FOLLOW_25_in_asignacion111)

                self._state.following.append(self.FOLLOW_expresion_in_asignacion113)
                self.expresion()

                self._state.following.pop()

                self.match(self.input, 22, self.FOLLOW_22_in_asignacion115)




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
                self.match(self.input, 32, self.FOLLOW_32_in_escritura123)

                self.match(self.input, 14, self.FOLLOW_14_in_escritura125)

                self._state.following.append(self.FOLLOW_stmt_in_escritura127)
                self.stmt()

                self._state.following.pop()

                self.match(self.input, 15, self.FOLLOW_15_in_escritura129)

                self.match(self.input, 22, self.FOLLOW_22_in_escritura131)




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
                self._state.following.append(self.FOLLOW_strgstmt_in_stmt139)
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
                        self.match(self.input, 18, self.FOLLOW_18_in_stmt142)

                        self._state.following.append(self.FOLLOW_strgstmt_in_stmt144)
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
                    self.match(self.input, STRING, self.FOLLOW_STRING_in_strgstmt153)


                elif alt6 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:29:20: expresion
                    pass 
                    self._state.following.append(self.FOLLOW_expresion_in_strgstmt157)
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
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:31:1: expresion : exp opexp ;
    def expresion(self, ):
        try:
            try:
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:2: ( exp opexp )
                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:4: exp opexp
                pass 
                self._state.following.append(self.FOLLOW_exp_in_expresion166)
                self.exp()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_opexp_in_expresion168)
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
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == 26:
                    alt7 = 1
                elif LA7 == 23:
                    alt7 = 2
                elif LA7 == 24:
                    alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:34:9: '>' exp
                    pass 
                    self.match(self.input, 26, self.FOLLOW_26_in_opexp176)

                    self._state.following.append(self.FOLLOW_exp_in_opexp178)
                    self.exp()

                    self._state.following.pop()


                elif alt7 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:4: '<' exp
                    pass 
                    self.match(self.input, 23, self.FOLLOW_23_in_opexp183)

                    self._state.following.append(self.FOLLOW_exp_in_opexp185)
                    self.exp()

                    self._state.following.pop()


                elif alt7 == 3:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:4: '<>' exp
                    pass 
                    self.match(self.input, 24, self.FOLLOW_24_in_opexp190)

                    self._state.following.append(self.FOLLOW_exp_in_opexp192)
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
                self._state.following.append(self.FOLLOW_termino_in_exp202)
                self.termino()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:15: ( opsum termino )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 17 or LA8_0 == 19) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:39:16: opsum termino
                        pass 
                        self._state.following.append(self.FOLLOW_opsum_in_exp205)
                        self.opsum()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_termino_in_exp207)
                        self.termino()

                        self._state.following.pop()


                    else:
                        break #loop8





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
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 14) :
                    alt10 = 1
                elif (LA10_0 == FLOAT or (ID <= LA10_0 <= INT) or LA10_0 == 17 or LA10_0 == 19) :
                    alt10 = 2
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:41:11: '(' expresion ')'
                    pass 
                    self.match(self.input, 14, self.FOLLOW_14_in_factor218)

                    self._state.following.append(self.FOLLOW_expresion_in_factor220)
                    self.expresion()

                    self._state.following.pop()

                    self.match(self.input, 15, self.FOLLOW_15_in_factor222)


                elif alt10 == 2:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )? varcte
                    pass 
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: ( opsum )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 17 or LA9_0 == 19) :
                        alt9 = 1
                    if alt9 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:4: opsum
                        pass 
                        self._state.following.append(self.FOLLOW_opsum_in_factor227)
                        self.opsum()

                        self._state.following.pop()




                    self._state.following.append(self.FOLLOW_varcte_in_factor230)
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
                self._state.following.append(self.FOLLOW_factor_in_termino239)
                self.factor()

                self._state.following.pop()

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:18: ( opmul factor )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 16 or LA11_0 == 20) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:44:19: opmul factor
                        pass 
                        self._state.following.append(self.FOLLOW_opmul_in_termino242)
                        self.opmul()

                        self._state.following.pop()

                        self._state.following.append(self.FOLLOW_factor_in_termino244)
                        self.factor()

                        self._state.following.pop()


                    else:
                        break #loop11





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
                self.match(self.input, 34, self.FOLLOW_34_in_vars254)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: ( decl )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ID) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:46:14: decl
                        pass 
                        self._state.following.append(self.FOLLOW_decl_in_vars256)
                        self.decl()

                        self._state.following.pop()


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1





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
                self._state.following.append(self.FOLLOW_variabs_in_decl265)
                self.variabs()

                self._state.following.pop()

                self.match(self.input, 21, self.FOLLOW_21_in_decl267)

                self._state.following.append(self.FOLLOW_tipo_in_decl269)
                self.tipo()

                self._state.following.pop()

                self.match(self.input, 22, self.FOLLOW_22_in_decl271)




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
                self.match(self.input, ID, self.FOLLOW_ID_in_variabs279)

                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:14: ( ',' ID )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 18) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:50:15: ',' ID
                        pass 
                        self.match(self.input, 18, self.FOLLOW_18_in_variabs282)

                        self.match(self.input, ID, self.FOLLOW_ID_in_variabs284)


                    else:
                        break #loop13





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
                if self.input.LA(1) == 28 or self.input.LA(1) == 31:
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
