%{
/*
  Montserrat Lozano Dieck A01088686
*/


%}

DIGIT [0-9]
LETTER [A-Za-z]

%%
/*** Rules section ***/

{DIGIT}+\.{DIGIT}+  { cout << "FLOAT:" << yytext << endl; }
{DIGIT}+  { cout << "INTEGER:" << yytext << endl; }
{LETTER}({LETTER}|{DIGIT})*

%%

/*** Code section ***/
int main()
{
	printf("%02d: ", lines);
	yylex();

}
