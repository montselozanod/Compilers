%{
/*
  Montserrat Lozano Dieck A01088686
*/


%}

DIGIT [0-9]
LETTER [A-Za-z]

%%

"program" {return PROGRAM;}
"var" {return VAR;}
"int" {return INT;}
"float" {return FLOAT;}
"if"  {return IF;}
"else"  {return ELSE;}
{DIGIT}+\.{DIGIT}+  { cout << "FLOAT: " << yytext << endl; }
{DIGIT}+  { cout << "INTEGER: " << yytext << endl; }
{LETTER}({LETTER}|{DIGIT})* { cout << "IDENTIFIER: " << yytext << endl; }
\"(\\.|[^"])*\" { cout << "STRING: " << yytext << endl; }

%%

int main()
{
	printf("%02d: ", lines);
	yylex();

}
