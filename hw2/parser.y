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




VarCte:
  IDENTIFIER
  | INUM
  | FNUM
  ;

Tipo:
  INT
  | FLOAT
  ;

Vars:
  VAR A
  ;

A:
  B ':' Tipo ';' D
  ;

B:
  IDENTIFIER C;



%%

int main()
{

}
