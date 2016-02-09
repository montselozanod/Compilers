%{
#include <cstdio>
#include <iostream>
using namespace std;

extern "C" int yylex();
extern "C" int yyparse();
extern "C" FILE *yyin;

void yyerror(const char *s);

%}
%union{
  int ival;
  float fval;
  char *sval;
}

//tipo de token proviene de union
%token <ival> INUM
%token <fval> FNUM
%token <sval> CSTRING
%token <sval> IDENTIFIER
%token PROGRAM
%token VAR
%token INT
%token FLOAT
%token IF
%token ELSE
%token PRINT
%token NOTEQUAL

%start Programa

%%
//grammar

Programa:
  PROGRAM IDENTIFIER ';' Programa2
  ;

Programa2:
  Vars Bloque
  | Bloque
  ;

Bloque:
  '{' Es '}'
  ;

Es:
  Estatuto
  | Es Estatuto
  ;

Vars:
  VAR Dec
  ;

Dec:
  Def
  | Dec Def
  ;

Def:
  Ident ':' Tipo ';'
  ;

Ident:
  IDENTIFIER
  | Ident ',' IDENTIFIER
  ;

Estatuto:
  Asignacion
  | Condicion
  | Escritura
  ;

Asignacion:
  IDENTIFIER '=' Expresion ';'
  ;

Expresion:
  Exp
  | Exp Op Exp
  ;

Op:
  '>'
  | '<'
  | NOTEQUAL
  ;

Exp:
  Termino
  | Exp Signo Termino
  ;

Termino:
  Factor
  | Termino Fact Factor
  ;

Fact:
  '*'
  | '/'
  ;

Condicion:
  Ifin ';'
  | Ifin ELSE Bloque ';'
  ;

Ifin:
    IF '(' Expresion ')' Bloque
    ;

Escritura:
  PRINT '(' PrintSeq ')' ';'
  ;

PrintSeq:
  PrintOp
  | PrintSeq ',' PrintOp
  ;

PrintOp:
  Expresion
  | CSTRING
  ;

VarCte:
  IDENTIFIER
  | INUM
  | FNUM
  ;

Tipo:
  INT
  | FLOAT
  ;

Factor:
  '(' Expresion ')'
  | Signo VarCte
  | VarCte
  ;

Signo:
  '+'
  | '-'
  ;

%%

int main(int, char**)
{
  // open a file handle to a particular file:
	FILE *myfile = fopen("prueba.o", "r");
	// make sure it is valid:
	if (!myfile) {
		cout << "I can't open a.snazzle.file!" << endl;
		return -1;
	}
	// set flex to read from it instead of defaulting to STDIN:
	yyin = myfile;

	// parse through the input until there is no more:
	do {
		yyparse();
	} while (!feof(yyin));

}

void yyerror(const char *s) {
	cout << "EEK, parse error!  Message: " << s << endl;
	// might as well halt now:
	exit(-1);
}
