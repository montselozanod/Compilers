%{
#include <cstdio>
#include <iostream>
using namespace std;
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

%start Programa

%%
//grammar

Programa:
  PROGRAM IDENTIFIER ';' Vars Bloque
  | PROGRAM IDENTIFIER ';' Bloque
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
  | '<>'
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

int main()
{

}
