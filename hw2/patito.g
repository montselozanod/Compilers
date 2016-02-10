grammar patito;

parse	:	tipo EOF;


bloque	:	'{' estatuto* '}';

estatuto:	asignacion
	|	escritura
	|condicion;

condicion
	:	'if' '(' expresion ')' bloque condelse? ';';

condelse:	'else' bloque;

asignacion
	:	ID '=' expresion ';';
escritura
	:	'print' '(' stmt ')' ';';

stmt	:	strgstmt stmt2*;

stmt2	:	',' stmt;

strgstmt:	STRING | expresion;

expresion
	: exp opexp;

opexp	: '>' exp
	| '<' exp
	| '<>' exp
	;

exp	:	termino (opsum exp)*;

factor	:	 '(' expresion ')'
	|	opsum? varcte;

termino	:	factor (opmul termino)*;

vars	:	'var' decl+;

decl	:	variabs ':' tipo ';';

variabs	:	ID more*;

more	:	',' variabs;

varcte	:	ID|INT|FLOAT;

tipo	:	'int'|'float';

opsum	:	'+'|'-';

opmul	:	'*'|'/';

ID  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
    ;

INT :	'0'..'9'+
    ;

FLOAT
    :   ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
    |   '.' ('0'..'9')+ EXPONENT?
    |   ('0'..'9')+ EXPONENT
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;

STRING
    :  '"' ( ESC_SEQ | ~('\\'|'"') )* '"'
    ;

fragment
EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;

fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
ESC_SEQ
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    |   UNICODE_ESC
    |   OCTAL_ESC
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;
