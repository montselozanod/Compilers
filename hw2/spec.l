%{
/*
  Montserrat Lozano Dieck A01088686
*/

#include <iostream>
#define YY_DECL extern "C" int yylex()
#include "parser.tab.h"  // to get the token types that we return
%}

DIGIT [0-9]
LETTER [A-Za-z]

%%

"<>"  {yylval.sval = strdup(yytext);
	return NOTEQUAL;}
"program" {yylval.sval = strdup(yytext);
	return PROGRAM;}
"var" {yylval.sval = strdup(yytext);
	return VAR;}
"int" {yylval.sval = strdup(yytext);
	return INT;}
"float" {yylval.sval = strdup(yytext);
	return FLOAT;}
"if"  {yylval.sval = strdup(yytext);
	return IF;}
"else"  {yylval.sval = strdup(yytext);
	return ELSE;}
"print" {yylval.sval = strdup(yytext);
	return PRINT;}
{DIGIT}+\.{DIGIT}+  { yylval.fval = atof(yytext); return FNUM; }
{DIGIT}+  { yylval.ival = atof(yytext); return INUM; }
{LETTER}({LETTER}|{DIGIT})* { yylval.sval = strdup(yytext);
	return IDENTIFIER; }
\"(\\.|[^"])*\" { yylval.sval = strdup(yytext);
	return CSTRING; }

%%
