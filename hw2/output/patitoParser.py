# $ANTLR 3.5.1 /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g 2016-02-10 20:15:09

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.debug import *
from antlr3.tree import *




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

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()
	self.ruleLevel = 0

	if self._dbg is None:
	    proxy = DebugEventSocketProxy(self, adaptor=self._adaptor,
	                                  debug=debug_socket, port=port)
	    self.setDebugListener(proxy)
	    self.adaptor.setDebugListener(proxy)
	    self.input.setDebugListener(proxy)
	    #self.setTokenStream(DebugTokenStream(self.input, proxy))
	    proxy.handshake()



    ruleNames = [
        "invalidRule", "programa", "tipo", "condicion", "estatuto", "variabs", 
        "exp", "factor", "expresion", "opsum", "bloque", "stmt", "escritura", 
        "opmul", "condelse", "start", "opexp", "strgstmt", "varcte", "termino", 
        "decl", "vars", "asignacion"
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


    def setTreeAdaptor(self, adaptor):
        self._adaptor = DebugTreeAdaptor(self.dbg, adaptor)

    def getTreeAdaptor(self):
        return self._adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)



    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:1: start : programa EOF ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EOF2 = None
        programa1 = None

        EOF2_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "start")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(8, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:7: ( programa EOF )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:8:9: programa EOF
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(8, 9)
                    self._state.following.append(self.FOLLOW_programa_in_start32)
                    programa1 = self.programa()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, programa1.tree)

                    self._dbg.location(8, 18)
                    EOF2 = self.match(self.input, EOF, self.FOLLOW_EOF_in_start34)
                    EOF2_tree = self._adaptor.createWithPayload(EOF2)
                    self._adaptor.addChild(root_0, EOF2_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(8, 20+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "start")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "start"


    class programa_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.programa_return, self).__init__()

            self.tree = None





    # $ANTLR start "programa"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:1: programa : 'program' 'id' ';' ( vars )? bloque ;
    def programa(self, ):
        retval = self.programa_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal3 = None
        string_literal4 = None
        char_literal5 = None
        vars6 = None
        bloque7 = None

        string_literal3_tree = None
        string_literal4_tree = None
        char_literal5_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "programa")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(10, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:9: ( 'program' 'id' ';' ( vars )? bloque )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:11: 'program' 'id' ';' ( vars )? bloque
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(10, 11)
                    string_literal3 = self.match(self.input, 33, self.FOLLOW_33_in_programa41)
                    string_literal3_tree = self._adaptor.createWithPayload(string_literal3)
                    self._adaptor.addChild(root_0, string_literal3_tree)


                    self._dbg.location(10, 21)
                    string_literal4 = self.match(self.input, 29, self.FOLLOW_29_in_programa43)
                    string_literal4_tree = self._adaptor.createWithPayload(string_literal4)
                    self._adaptor.addChild(root_0, string_literal4_tree)


                    self._dbg.location(10, 26)
                    char_literal5 = self.match(self.input, 22, self.FOLLOW_22_in_programa45)
                    char_literal5_tree = self._adaptor.createWithPayload(char_literal5)
                    self._adaptor.addChild(root_0, char_literal5_tree)


                    self._dbg.location(10, 30)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:30: ( vars )?
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

                            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:10:30: vars
                            pass 
                            self._dbg.location(10, 30)
                            self._state.following.append(self.FOLLOW_vars_in_programa47)
                            vars6 = self.vars()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, vars6.tree)




                    finally:
                        self._dbg.exitSubRule(1)
                    self._dbg.location(10, 36)
                    self._state.following.append(self.FOLLOW_bloque_in_programa50)
                    bloque7 = self.bloque()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bloque7.tree)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(10, 41+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "programa")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "programa"


    class bloque_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.bloque_return, self).__init__()

            self.tree = None





    # $ANTLR start "bloque"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:1: bloque : '{' ( estatuto )* '}' ;
    def bloque(self, ):
        retval = self.bloque_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal8 = None
        char_literal10 = None
        estatuto9 = None

        char_literal8_tree = None
        char_literal10_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "bloque")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(12, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:8: ( '{' ( estatuto )* '}' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:10: '{' ( estatuto )* '}'
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(12, 10)
                    char_literal8 = self.match(self.input, 35, self.FOLLOW_35_in_bloque58)
                    char_literal8_tree = self._adaptor.createWithPayload(char_literal8)
                    self._adaptor.addChild(root_0, char_literal8_tree)


                    self._dbg.location(12, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:14: ( estatuto )*
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:12:14: estatuto
                                pass 
                                self._dbg.location(12, 14)
                                self._state.following.append(self.FOLLOW_estatuto_in_bloque60)
                                estatuto9 = self.estatuto()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, estatuto9.tree)



                            else:
                                break #loop2

                    finally:
                        self._dbg.exitSubRule(2)

                    self._dbg.location(12, 24)
                    char_literal10 = self.match(self.input, 36, self.FOLLOW_36_in_bloque63)
                    char_literal10_tree = self._adaptor.createWithPayload(char_literal10)
                    self._adaptor.addChild(root_0, char_literal10_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(12, 26+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "bloque")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "bloque"


    class estatuto_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.estatuto_return, self).__init__()

            self.tree = None





    # $ANTLR start "estatuto"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:1: estatuto : ( asignacion | escritura | condicion );
    def estatuto(self, ):
        retval = self.estatuto_return()
        retval.start = self.input.LT(1)


        root_0 = None

        asignacion11 = None
        escritura12 = None
        condicion13 = None


        try:
            self._dbg.enterRule(self.getGrammarFileName(), "estatuto")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(14, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:9: ( asignacion | escritura | condicion )
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

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:14:11: asignacion
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(14, 11)
                        self._state.following.append(self.FOLLOW_asignacion_in_estatuto70)
                        asignacion11 = self.asignacion()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, asignacion11.tree)



                    elif alt3 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:15:4: escritura
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(15, 4)
                        self._state.following.append(self.FOLLOW_escritura_in_estatuto75)
                        escritura12 = self.escritura()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, escritura12.tree)



                    elif alt3 == 3:
                        self._dbg.enterAlt(3)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:16:3: condicion
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(16, 3)
                        self._state.following.append(self.FOLLOW_condicion_in_estatuto79)
                        condicion13 = self.condicion()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, condicion13.tree)



                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(16, 11+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "estatuto")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "estatuto"


    class condicion_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.condicion_return, self).__init__()

            self.tree = None





    # $ANTLR start "condicion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:18:1: condicion : 'if' '(' expresion ')' bloque ( condelse )? ';' ;
    def condicion(self, ):
        retval = self.condicion_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal14 = None
        char_literal15 = None
        char_literal17 = None
        char_literal20 = None
        expresion16 = None
        bloque18 = None
        condelse19 = None

        string_literal14_tree = None
        char_literal15_tree = None
        char_literal17_tree = None
        char_literal20_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "condicion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(18, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:2: ( 'if' '(' expresion ')' bloque ( condelse )? ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:4: 'if' '(' expresion ')' bloque ( condelse )? ';'
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(19, 4)
                    string_literal14 = self.match(self.input, 30, self.FOLLOW_30_in_condicion88)
                    string_literal14_tree = self._adaptor.createWithPayload(string_literal14)
                    self._adaptor.addChild(root_0, string_literal14_tree)


                    self._dbg.location(19, 9)
                    char_literal15 = self.match(self.input, 14, self.FOLLOW_14_in_condicion90)
                    char_literal15_tree = self._adaptor.createWithPayload(char_literal15)
                    self._adaptor.addChild(root_0, char_literal15_tree)


                    self._dbg.location(19, 13)
                    self._state.following.append(self.FOLLOW_expresion_in_condicion92)
                    expresion16 = self.expresion()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expresion16.tree)

                    self._dbg.location(19, 23)
                    char_literal17 = self.match(self.input, 15, self.FOLLOW_15_in_condicion94)
                    char_literal17_tree = self._adaptor.createWithPayload(char_literal17)
                    self._adaptor.addChild(root_0, char_literal17_tree)


                    self._dbg.location(19, 27)
                    self._state.following.append(self.FOLLOW_bloque_in_condicion96)
                    bloque18 = self.bloque()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bloque18.tree)

                    self._dbg.location(19, 34)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:34: ( condelse )?
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

                            # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:19:34: condelse
                            pass 
                            self._dbg.location(19, 34)
                            self._state.following.append(self.FOLLOW_condelse_in_condicion98)
                            condelse19 = self.condelse()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, condelse19.tree)




                    finally:
                        self._dbg.exitSubRule(4)
                    self._dbg.location(19, 44)
                    char_literal20 = self.match(self.input, 22, self.FOLLOW_22_in_condicion101)
                    char_literal20_tree = self._adaptor.createWithPayload(char_literal20)
                    self._adaptor.addChild(root_0, char_literal20_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(19, 46+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "condicion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "condicion"


    class condelse_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.condelse_return, self).__init__()

            self.tree = None





    # $ANTLR start "condelse"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:1: condelse : 'else' bloque ;
    def condelse(self, ):
        retval = self.condelse_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal21 = None
        bloque22 = None

        string_literal21_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "condelse")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(21, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:9: ( 'else' bloque )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:21:11: 'else' bloque
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(21, 11)
                    string_literal21 = self.match(self.input, 27, self.FOLLOW_27_in_condelse108)
                    string_literal21_tree = self._adaptor.createWithPayload(string_literal21)
                    self._adaptor.addChild(root_0, string_literal21_tree)


                    self._dbg.location(21, 18)
                    self._state.following.append(self.FOLLOW_bloque_in_condelse110)
                    bloque22 = self.bloque()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, bloque22.tree)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(21, 23+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "condelse")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "condelse"


    class asignacion_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.asignacion_return, self).__init__()

            self.tree = None





    # $ANTLR start "asignacion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:23:1: asignacion : ID '=' expresion ';' ;
    def asignacion(self, ):
        retval = self.asignacion_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID23 = None
        char_literal24 = None
        char_literal26 = None
        expresion25 = None

        ID23_tree = None
        char_literal24_tree = None
        char_literal26_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "asignacion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(23, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:2: ( ID '=' expresion ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:24:4: ID '=' expresion ';'
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(24, 4)
                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_asignacion119)
                    ID23_tree = self._adaptor.createWithPayload(ID23)
                    self._adaptor.addChild(root_0, ID23_tree)


                    self._dbg.location(24, 7)
                    char_literal24 = self.match(self.input, 25, self.FOLLOW_25_in_asignacion121)
                    char_literal24_tree = self._adaptor.createWithPayload(char_literal24)
                    self._adaptor.addChild(root_0, char_literal24_tree)


                    self._dbg.location(24, 11)
                    self._state.following.append(self.FOLLOW_expresion_in_asignacion123)
                    expresion25 = self.expresion()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expresion25.tree)

                    self._dbg.location(24, 21)
                    char_literal26 = self.match(self.input, 22, self.FOLLOW_22_in_asignacion125)
                    char_literal26_tree = self._adaptor.createWithPayload(char_literal26)
                    self._adaptor.addChild(root_0, char_literal26_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(24, 23+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "asignacion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "asignacion"


    class escritura_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.escritura_return, self).__init__()

            self.tree = None





    # $ANTLR start "escritura"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:25:1: escritura : 'print' '(' stmt ')' ';' ;
    def escritura(self, ):
        retval = self.escritura_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal27 = None
        char_literal28 = None
        char_literal30 = None
        char_literal31 = None
        stmt29 = None

        string_literal27_tree = None
        char_literal28_tree = None
        char_literal30_tree = None
        char_literal31_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "escritura")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(25, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:2: ( 'print' '(' stmt ')' ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:26:4: 'print' '(' stmt ')' ';'
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(26, 4)
                    string_literal27 = self.match(self.input, 32, self.FOLLOW_32_in_escritura133)
                    string_literal27_tree = self._adaptor.createWithPayload(string_literal27)
                    self._adaptor.addChild(root_0, string_literal27_tree)


                    self._dbg.location(26, 12)
                    char_literal28 = self.match(self.input, 14, self.FOLLOW_14_in_escritura135)
                    char_literal28_tree = self._adaptor.createWithPayload(char_literal28)
                    self._adaptor.addChild(root_0, char_literal28_tree)


                    self._dbg.location(26, 16)
                    self._state.following.append(self.FOLLOW_stmt_in_escritura137)
                    stmt29 = self.stmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, stmt29.tree)

                    self._dbg.location(26, 21)
                    char_literal30 = self.match(self.input, 15, self.FOLLOW_15_in_escritura139)
                    char_literal30_tree = self._adaptor.createWithPayload(char_literal30)
                    self._adaptor.addChild(root_0, char_literal30_tree)


                    self._dbg.location(26, 25)
                    char_literal31 = self.match(self.input, 22, self.FOLLOW_22_in_escritura141)
                    char_literal31_tree = self._adaptor.createWithPayload(char_literal31)
                    self._adaptor.addChild(root_0, char_literal31_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(26, 27+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "escritura")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "escritura"


    class stmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.stmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "stmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:1: stmt : strgstmt ( ',' strgstmt )* ;
    def stmt(self, ):
        retval = self.stmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal33 = None
        strgstmt32 = None
        strgstmt34 = None

        char_literal33_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "stmt")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(28, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:6: ( strgstmt ( ',' strgstmt )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:8: strgstmt ( ',' strgstmt )*
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(28, 8)
                    self._state.following.append(self.FOLLOW_strgstmt_in_stmt149)
                    strgstmt32 = self.strgstmt()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, strgstmt32.tree)

                    self._dbg.location(28, 17)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:17: ( ',' strgstmt )*
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:28:18: ',' strgstmt
                                pass 
                                self._dbg.location(28, 18)
                                char_literal33 = self.match(self.input, 18, self.FOLLOW_18_in_stmt152)
                                char_literal33_tree = self._adaptor.createWithPayload(char_literal33)
                                self._adaptor.addChild(root_0, char_literal33_tree)


                                self._dbg.location(28, 22)
                                self._state.following.append(self.FOLLOW_strgstmt_in_stmt154)
                                strgstmt34 = self.strgstmt()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, strgstmt34.tree)



                            else:
                                break #loop5

                    finally:
                        self._dbg.exitSubRule(5)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(28, 31+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "stmt")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "stmt"


    class strgstmt_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.strgstmt_return, self).__init__()

            self.tree = None





    # $ANTLR start "strgstmt"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:1: strgstmt : ( STRING | expresion );
    def strgstmt(self, ):
        retval = self.strgstmt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STRING35 = None
        expresion36 = None

        STRING35_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "strgstmt")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(30, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:9: ( STRING | expresion )
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

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:11: STRING
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(30, 11)
                        STRING35 = self.match(self.input, STRING, self.FOLLOW_STRING_in_strgstmt163)
                        STRING35_tree = self._adaptor.createWithPayload(STRING35)
                        self._adaptor.addChild(root_0, STRING35_tree)




                    elif alt6 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:30:20: expresion
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(30, 20)
                        self._state.following.append(self.FOLLOW_expresion_in_strgstmt167)
                        expresion36 = self.expresion()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expresion36.tree)



                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(30, 28+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "strgstmt")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "strgstmt"


    class expresion_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.expresion_return, self).__init__()

            self.tree = None





    # $ANTLR start "expresion"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:32:1: expresion : exp opexp ;
    def expresion(self, ):
        retval = self.expresion_return()
        retval.start = self.input.LT(1)


        root_0 = None

        exp37 = None
        opexp38 = None


        try:
            self._dbg.enterRule(self.getGrammarFileName(), "expresion")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(32, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:33:2: ( exp opexp )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:33:4: exp opexp
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(33, 4)
                    self._state.following.append(self.FOLLOW_exp_in_expresion176)
                    exp37 = self.exp()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, exp37.tree)

                    self._dbg.location(33, 8)
                    self._state.following.append(self.FOLLOW_opexp_in_expresion178)
                    opexp38 = self.opexp()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, opexp38.tree)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(33, 12+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "expresion")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "expresion"


    class opexp_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.opexp_return, self).__init__()

            self.tree = None





    # $ANTLR start "opexp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:1: opexp : ( '>' exp | '<' exp | '<>' exp );
    def opexp(self, ):
        retval = self.opexp_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal39 = None
        char_literal41 = None
        string_literal43 = None
        exp40 = None
        exp42 = None
        exp44 = None

        char_literal39_tree = None
        char_literal41_tree = None
        string_literal43_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opexp")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(35, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:7: ( '>' exp | '<' exp | '<>' exp )
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

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:35:9: '>' exp
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(35, 9)
                        char_literal39 = self.match(self.input, 26, self.FOLLOW_26_in_opexp186)
                        char_literal39_tree = self._adaptor.createWithPayload(char_literal39)
                        self._adaptor.addChild(root_0, char_literal39_tree)


                        self._dbg.location(35, 13)
                        self._state.following.append(self.FOLLOW_exp_in_opexp188)
                        exp40 = self.exp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exp40.tree)



                    elif alt7 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:36:4: '<' exp
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(36, 4)
                        char_literal41 = self.match(self.input, 23, self.FOLLOW_23_in_opexp193)
                        char_literal41_tree = self._adaptor.createWithPayload(char_literal41)
                        self._adaptor.addChild(root_0, char_literal41_tree)


                        self._dbg.location(36, 8)
                        self._state.following.append(self.FOLLOW_exp_in_opexp195)
                        exp42 = self.exp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exp42.tree)



                    elif alt7 == 3:
                        self._dbg.enterAlt(3)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:37:4: '<>' exp
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(37, 4)
                        string_literal43 = self.match(self.input, 24, self.FOLLOW_24_in_opexp200)
                        string_literal43_tree = self._adaptor.createWithPayload(string_literal43)
                        self._adaptor.addChild(root_0, string_literal43_tree)


                        self._dbg.location(37, 9)
                        self._state.following.append(self.FOLLOW_exp_in_opexp202)
                        exp44 = self.exp()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, exp44.tree)



                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(38, 1+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opexp")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "opexp"


    class exp_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.exp_return, self).__init__()

            self.tree = None





    # $ANTLR start "exp"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:1: exp : termino ( opsum termino )* ;
    def exp(self, ):
        retval = self.exp_return()
        retval.start = self.input.LT(1)


        root_0 = None

        termino45 = None
        opsum46 = None
        termino47 = None


        try:
            self._dbg.enterRule(self.getGrammarFileName(), "exp")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(40, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:5: ( termino ( opsum termino )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:7: termino ( opsum termino )*
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(40, 7)
                    self._state.following.append(self.FOLLOW_termino_in_exp212)
                    termino45 = self.termino()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, termino45.tree)

                    self._dbg.location(40, 15)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:15: ( opsum termino )*
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:40:16: opsum termino
                                pass 
                                self._dbg.location(40, 16)
                                self._state.following.append(self.FOLLOW_opsum_in_exp215)
                                opsum46 = self.opsum()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, opsum46.tree)

                                self._dbg.location(40, 22)
                                self._state.following.append(self.FOLLOW_termino_in_exp217)
                                termino47 = self.termino()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, termino47.tree)



                            else:
                                break #loop8

                    finally:
                        self._dbg.exitSubRule(8)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(40, 30+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "exp")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "exp"


    class factor_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.factor_return, self).__init__()

            self.tree = None





    # $ANTLR start "factor"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:1: factor : ( '(' expresion ')' | ( opsum )? varcte );
    def factor(self, ):
        retval = self.factor_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal48 = None
        char_literal50 = None
        expresion49 = None
        opsum51 = None
        varcte52 = None

        char_literal48_tree = None
        char_literal50_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "factor")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(42, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:8: ( '(' expresion ')' | ( opsum )? varcte )
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

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:42:11: '(' expresion ')'
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(42, 11)
                        char_literal48 = self.match(self.input, 14, self.FOLLOW_14_in_factor228)
                        char_literal48_tree = self._adaptor.createWithPayload(char_literal48)
                        self._adaptor.addChild(root_0, char_literal48_tree)


                        self._dbg.location(42, 15)
                        self._state.following.append(self.FOLLOW_expresion_in_factor230)
                        expresion49 = self.expresion()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expresion49.tree)

                        self._dbg.location(42, 25)
                        char_literal50 = self.match(self.input, 15, self.FOLLOW_15_in_factor232)
                        char_literal50_tree = self._adaptor.createWithPayload(char_literal50)
                        self._adaptor.addChild(root_0, char_literal50_tree)




                    elif alt10 == 2:
                        self._dbg.enterAlt(2)

                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:43:4: ( opsum )? varcte
                        pass 
                        root_0 = self._adaptor.nil()


                        self._dbg.location(43, 4)
                        # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:43:4: ( opsum )?
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:43:4: opsum
                                pass 
                                self._dbg.location(43, 4)
                                self._state.following.append(self.FOLLOW_opsum_in_factor237)
                                opsum51 = self.opsum()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, opsum51.tree)




                        finally:
                            self._dbg.exitSubRule(9)
                        self._dbg.location(43, 11)
                        self._state.following.append(self.FOLLOW_varcte_in_factor240)
                        varcte52 = self.varcte()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, varcte52.tree)



                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(43, 16+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "factor")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "factor"


    class termino_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.termino_return, self).__init__()

            self.tree = None





    # $ANTLR start "termino"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:45:1: termino : factor ( opmul factor )* ;
    def termino(self, ):
        retval = self.termino_return()
        retval.start = self.input.LT(1)


        root_0 = None

        factor53 = None
        opmul54 = None
        factor55 = None


        try:
            self._dbg.enterRule(self.getGrammarFileName(), "termino")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(45, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:45:9: ( factor ( opmul factor )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:45:11: factor ( opmul factor )*
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(45, 11)
                    self._state.following.append(self.FOLLOW_factor_in_termino249)
                    factor53 = self.factor()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, factor53.tree)

                    self._dbg.location(45, 18)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:45:18: ( opmul factor )*
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:45:19: opmul factor
                                pass 
                                self._dbg.location(45, 19)
                                self._state.following.append(self.FOLLOW_opmul_in_termino252)
                                opmul54 = self.opmul()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, opmul54.tree)

                                self._dbg.location(45, 25)
                                self._state.following.append(self.FOLLOW_factor_in_termino254)
                                factor55 = self.factor()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, factor55.tree)



                            else:
                                break #loop11

                    finally:
                        self._dbg.exitSubRule(11)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(45, 32+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "termino")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "termino"


    class vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.vars_return, self).__init__()

            self.tree = None





    # $ANTLR start "vars"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:47:1: vars : 'var' ( decl )+ ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal56 = None
        decl57 = None

        string_literal56_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "vars")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(47, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:47:6: ( 'var' ( decl )+ )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:47:8: 'var' ( decl )+
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(47, 8)
                    string_literal56 = self.match(self.input, 34, self.FOLLOW_34_in_vars264)
                    string_literal56_tree = self._adaptor.createWithPayload(string_literal56)
                    self._adaptor.addChild(root_0, string_literal56_tree)


                    self._dbg.location(47, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:47:14: ( decl )+
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:47:14: decl
                                pass 
                                self._dbg.location(47, 14)
                                self._state.following.append(self.FOLLOW_decl_in_vars266)
                                decl57 = self.decl()

                                self._state.following.pop()
                                self._adaptor.addChild(root_0, decl57.tree)



                            else:
                                if cnt12 >= 1:
                                    break #loop12

                                eee = EarlyExitException(12, self.input)
                                self._dbg.recognitionException(eee)

                                raise eee

                            cnt12 += 1

                    finally:
                        self._dbg.exitSubRule(12)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(47, 18+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "vars")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "vars"


    class decl_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.decl_return, self).__init__()

            self.tree = None





    # $ANTLR start "decl"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:49:1: decl : variabs ':' tipo ';' ;
    def decl(self, ):
        retval = self.decl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal59 = None
        char_literal61 = None
        variabs58 = None
        tipo60 = None

        char_literal59_tree = None
        char_literal61_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "decl")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(49, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:49:6: ( variabs ':' tipo ';' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:49:8: variabs ':' tipo ';'
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(49, 8)
                    self._state.following.append(self.FOLLOW_variabs_in_decl275)
                    variabs58 = self.variabs()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, variabs58.tree)

                    self._dbg.location(49, 16)
                    char_literal59 = self.match(self.input, 21, self.FOLLOW_21_in_decl277)
                    char_literal59_tree = self._adaptor.createWithPayload(char_literal59)
                    self._adaptor.addChild(root_0, char_literal59_tree)


                    self._dbg.location(49, 20)
                    self._state.following.append(self.FOLLOW_tipo_in_decl279)
                    tipo60 = self.tipo()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, tipo60.tree)

                    self._dbg.location(49, 25)
                    char_literal61 = self.match(self.input, 22, self.FOLLOW_22_in_decl281)
                    char_literal61_tree = self._adaptor.createWithPayload(char_literal61)
                    self._adaptor.addChild(root_0, char_literal61_tree)





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(49, 27+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "decl")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "decl"


    class variabs_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.variabs_return, self).__init__()

            self.tree = None





    # $ANTLR start "variabs"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:51:1: variabs : ID ( ',' ID )* ;
    def variabs(self, ):
        retval = self.variabs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID62 = None
        char_literal63 = None
        ID64 = None

        ID62_tree = None
        char_literal63_tree = None
        ID64_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "variabs")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(51, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:51:9: ( ID ( ',' ID )* )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:51:11: ID ( ',' ID )*
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(51, 11)
                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_variabs289)
                    ID62_tree = self._adaptor.createWithPayload(ID62)
                    self._adaptor.addChild(root_0, ID62_tree)


                    self._dbg.location(51, 14)
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:51:14: ( ',' ID )*
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

                                # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:51:15: ',' ID
                                pass 
                                self._dbg.location(51, 15)
                                char_literal63 = self.match(self.input, 18, self.FOLLOW_18_in_variabs292)
                                char_literal63_tree = self._adaptor.createWithPayload(char_literal63)
                                self._adaptor.addChild(root_0, char_literal63_tree)


                                self._dbg.location(51, 19)
                                ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_variabs294)
                                ID64_tree = self._adaptor.createWithPayload(ID64)
                                self._adaptor.addChild(root_0, ID64_tree)




                            else:
                                break #loop13

                    finally:
                        self._dbg.exitSubRule(13)




                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(51, 22+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "variabs")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "variabs"


    class varcte_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.varcte_return, self).__init__()

            self.tree = None





    # $ANTLR start "varcte"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:53:1: varcte : ( ID | INT | FLOAT );
    def varcte(self, ):
        retval = self.varcte_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set65 = None

        set65_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "varcte")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(53, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:53:8: ( ID | INT | FLOAT )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(53, 8)
                    set65 = self.input.LT(1)

                    if self.input.LA(1) == FLOAT or (ID <= self.input.LA(1) <= INT):
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set65))

                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(53, 21+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "varcte")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "varcte"


    class tipo_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.tipo_return, self).__init__()

            self.tree = None





    # $ANTLR start "tipo"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:55:1: tipo : ( 'int' | 'float' );
    def tipo(self, ):
        retval = self.tipo_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set66 = None

        set66_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "tipo")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(55, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:55:6: ( 'int' | 'float' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(55, 6)
                    set66 = self.input.LT(1)

                    if self.input.LA(1) == 28 or self.input.LA(1) == 31:
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set66))

                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(55, 20+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "tipo")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "tipo"


    class opsum_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.opsum_return, self).__init__()

            self.tree = None





    # $ANTLR start "opsum"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:57:1: opsum : ( '+' | '-' );
    def opsum(self, ):
        retval = self.opsum_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set67 = None

        set67_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opsum")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(57, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:57:7: ( '+' | '-' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(57, 7)
                    set67 = self.input.LT(1)

                    if self.input.LA(1) == 17 or self.input.LA(1) == 19:
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set67))

                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(57, 15+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opsum")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "opsum"


    class opmul_return(ParserRuleReturnScope):
        def __init__(self):
            super(patitoParser.opmul_return, self).__init__()

            self.tree = None





    # $ANTLR start "opmul"
    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:59:1: opmul : ( '*' | '/' );
    def opmul(self, ):
        retval = self.opmul_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set68 = None

        set68_tree = None

        try:
            self._dbg.enterRule(self.getGrammarFileName(), "opmul")
            if self.getRuleLevel() == 0:
                self._dbg.commence();
            self.incRuleLevel()
            self._dbg.location(59, 0+1)

            try:
                try:
                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:59:7: ( '*' | '/' )
                    self._dbg.enterAlt(1)

                    # /Users/montselozanod/Documents/Tec/Compilers/Compilers/hw2/patito.g:
                    pass 
                    root_0 = self._adaptor.nil()


                    self._dbg.location(59, 7)
                    set68 = self.input.LT(1)

                    if self.input.LA(1) == 16 or self.input.LA(1) == 20:
                        self.input.consume()
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set68))

                        self._state.errorRecovery = False


                    else:
                        mse = MismatchedSetException(None, self.input)
                        self._dbg.recognitionException(mse)
                        raise mse





                    retval.stop = self.input.LT(-1)


                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



                except RecognitionException, re:
                    self.reportError(re)
                    self.recover(self.input, re)
                    retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

            finally:
                pass

            self._dbg.location(59, 15+1)
        finally:
            self._dbg.exitRule(self.getGrammarFileName(), "opmul")
            self.decRuleLevel()
            if self.getRuleLevel() == 0:
                 self._dbg.terminate()

        return retval

    # $ANTLR end "opmul"



 

    FOLLOW_programa_in_start32 = frozenset([])
    FOLLOW_EOF_in_start34 = frozenset([1])
    FOLLOW_33_in_programa41 = frozenset([29])
    FOLLOW_29_in_programa43 = frozenset([22])
    FOLLOW_22_in_programa45 = frozenset([34, 35])
    FOLLOW_vars_in_programa47 = frozenset([35])
    FOLLOW_bloque_in_programa50 = frozenset([1])
    FOLLOW_35_in_bloque58 = frozenset([8, 30, 32, 36])
    FOLLOW_estatuto_in_bloque60 = frozenset([8, 30, 32, 36])
    FOLLOW_36_in_bloque63 = frozenset([1])
    FOLLOW_asignacion_in_estatuto70 = frozenset([1])
    FOLLOW_escritura_in_estatuto75 = frozenset([1])
    FOLLOW_condicion_in_estatuto79 = frozenset([1])
    FOLLOW_30_in_condicion88 = frozenset([14])
    FOLLOW_14_in_condicion90 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_condicion92 = frozenset([15])
    FOLLOW_15_in_condicion94 = frozenset([35])
    FOLLOW_bloque_in_condicion96 = frozenset([22, 27])
    FOLLOW_condelse_in_condicion98 = frozenset([22])
    FOLLOW_22_in_condicion101 = frozenset([1])
    FOLLOW_27_in_condelse108 = frozenset([35])
    FOLLOW_bloque_in_condelse110 = frozenset([1])
    FOLLOW_ID_in_asignacion119 = frozenset([25])
    FOLLOW_25_in_asignacion121 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_asignacion123 = frozenset([22])
    FOLLOW_22_in_asignacion125 = frozenset([1])
    FOLLOW_32_in_escritura133 = frozenset([14])
    FOLLOW_14_in_escritura135 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_stmt_in_escritura137 = frozenset([15])
    FOLLOW_15_in_escritura139 = frozenset([22])
    FOLLOW_22_in_escritura141 = frozenset([1])
    FOLLOW_strgstmt_in_stmt149 = frozenset([1, 18])
    FOLLOW_18_in_stmt152 = frozenset([6, 8, 9, 11, 14, 17, 19])
    FOLLOW_strgstmt_in_stmt154 = frozenset([1, 18])
    FOLLOW_STRING_in_strgstmt163 = frozenset([1])
    FOLLOW_expresion_in_strgstmt167 = frozenset([1])
    FOLLOW_exp_in_expresion176 = frozenset([23, 24, 26])
    FOLLOW_opexp_in_expresion178 = frozenset([1])
    FOLLOW_26_in_opexp186 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp188 = frozenset([1])
    FOLLOW_23_in_opexp193 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp195 = frozenset([1])
    FOLLOW_24_in_opexp200 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_exp_in_opexp202 = frozenset([1])
    FOLLOW_termino_in_exp212 = frozenset([1, 17, 19])
    FOLLOW_opsum_in_exp215 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_termino_in_exp217 = frozenset([1, 17, 19])
    FOLLOW_14_in_factor228 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_expresion_in_factor230 = frozenset([15])
    FOLLOW_15_in_factor232 = frozenset([1])
    FOLLOW_opsum_in_factor237 = frozenset([6, 8, 9])
    FOLLOW_varcte_in_factor240 = frozenset([1])
    FOLLOW_factor_in_termino249 = frozenset([1, 16, 20])
    FOLLOW_opmul_in_termino252 = frozenset([6, 8, 9, 14, 17, 19])
    FOLLOW_factor_in_termino254 = frozenset([1, 16, 20])
    FOLLOW_34_in_vars264 = frozenset([8])
    FOLLOW_decl_in_vars266 = frozenset([1, 8])
    FOLLOW_variabs_in_decl275 = frozenset([21])
    FOLLOW_21_in_decl277 = frozenset([28, 31])
    FOLLOW_tipo_in_decl279 = frozenset([22])
    FOLLOW_22_in_decl281 = frozenset([1])
    FOLLOW_ID_in_variabs289 = frozenset([1, 18])
    FOLLOW_18_in_variabs292 = frozenset([8])
    FOLLOW_ID_in_variabs294 = frozenset([1, 18])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("patitoLexer", patitoParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
