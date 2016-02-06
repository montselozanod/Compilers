%{
/*
  Montserrat Lozano Dieck A01088686
*/


%}

DIGIT [0-9]
LETTER [A-Za-z]

%%

"program" {std::cout << "PROGRAM"<< std::endl;}
"var" {std::cout << "VAR"<< std::endl;}
"int" {std::cout << "INT"<< std::endl;}
"float" {std::cout << "FLOAT"<< std::endl;}
"if"  {std::cout << "IF"<< std::endl;}
"else"  {std::cout << "ELSE"<< std::endl;}
{DIGIT}+\.{DIGIT}+  { std::cout << "FLOAT: " << yytext << std::endl; }
{DIGIT}+  { std::cout << "INTEGER: " << yytext << endl; }
{LETTER}({LETTER}|{DIGIT})* { std::cout << "IDENTIFIER: " << yytext << std::endl; }
\"(\\.|[^"])*\" { std::cout << "STRING: " << yytext << std::endl; }

%%

int main()
{
	printf("%02d: ", lines);
	yylex();

}
