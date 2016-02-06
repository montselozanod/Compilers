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

%%
//grammar
var_cte:

  | INUM
  | FNUM
  ;
%%

int main()
{

}
