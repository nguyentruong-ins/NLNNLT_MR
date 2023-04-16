// Student ID: 2010468

grammar MT22;

@lexer::header {
from lexererr import *
}

@parser::header{
from lexererr import *
}

options{
	language=Python3;
}

program: 	decllist EOF;

// Declaration list
decllist: 	decl decllist | decl;
decl: 		variabledcl | funcdcl;

// Declare Array
arrdcl: 	ARRAY LSB intlist RSB OF atom;
atom: 		BOOLEAN | INTEGER| FLOAT | STRING;
intlist: 	(INTTYPE COMMA) intlist | INTTYPE;
	
// Variable declarations
variabledcl: (vardcl_full | vardcl_short) SEMI;
vardcl_full: IDENTIFIER COMMA vardcl_full COMMA expr
			| IDENTIFIER ':' paratype '=' expr;
vardcl_short: idlist ':' paratype;
idlist: 	(IDENTIFIER COMMA) idlist | IDENTIFIER;	

// parameter declarations
paradcl: 	(INHERIT)? (OUT)? IDENTIFIER COLON paratype;
paratype: BOOLEAN | INTEGER | FLOAT | STRING | arrdcl | AUTO;

// Function declarations
funcdcl: 	IDENTIFIER COLON FUNCTION functype LB paralist RB (INHERIT IDENTIFIER)? blockstmt;
functype: BOOLEAN | INTEGER | FLOAT | STRING | VOID | arrdcl | AUTO;
paralist: 	paraprime |;
paraprime: 	(paradcl COMMA) paraprime | paradcl;

// Expressions
expr: expr1 CONC expr1 | expr1;
expr1: expr2 Binary1 expr2 | expr2;
Binary1: EQUAL | DIF | LT | GT | LTE | GTE;
expr2: expr2 Binary2 expr3 | expr3;
Binary2: AND | OR;
expr3: expr3 (PLUS | SUB) expr4 | expr4;
// Binary3: (PLUS | SUB);
expr4: expr4 Binary4 expr5 | expr5;
Binary4: (MUL | DIV | MOD);
expr5: NEG expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | arraylit | lhs | func_call | sub_expr ;

sub_expr: (LB expr RB);
arraylit: 	LCB nullable_explist RCB;
nullable_explist: exprlist | ;
idexop: 	IDENTIFIER LSB exprlist RSB;
func_call: 	IDENTIFIER LB nullable_explist RB;

// Statements
stmt: 		assignstmt | ifstmt | forstmt | whilestmt | dwstmt | callstmt | blockstmt | rtrnstmt | brkstmt | constmt | null_stmt;

// Null statements
null_stmt: ';';

//Assign statement
assignstmt: assign SEMI;
lhs: 		IDENTIFIER | idexop;

// If statement
ifstmt: 	IF LB expr RB stmt (ELSE stmt)?;

// For statement
forstmt: 	FOR LB assign COMMA expr COMMA expr RB stmt;
assign: lhs '=' expr;


// While statement
whilestmt: 	WHILE LB expr RB stmt;

// Do-while statement
dwstmt: 	DO blockstmt WHILE LB expr RB SEMI;

// Break statement
brkstmt: 	BREAK SEMI;

// Continue statement
constmt: 	CONTINUE SEMI;

// Return statement
rtrnstmt: 	RETURN expr? SEMI;

// Call statement
exprlist: 	expr COMMA exprlist | expr;
callstmt: 	IDENTIFIER LB exprlist? RB SEMI;

// Block statement
blockstmt: 	LCB	stmtlist RCB;
stmtlist: 	stmtprime |;
stmtprime: 	stmttype stmtprime | stmttype;
stmttype: stmt | variabledcl;

// Keywords
AUTO: 		'auto';
BREAK: 		'break';
BOOLEAN: 	'boolean';
DO: 		'do';
ELSE: 		'else';
FLOAT: 		'float';
FOR: 		'for';
FUNCTION: 	'function';
IF: 		'if';
INTEGER: 	'integer';
RETURN: 	'return';
STRING: 	'string';
WHILE: 		'while';
VOID: 		'void';
OUT: 		'out';
CONTINUE: 	'continue';
OF: 		'of';
INHERIT: 	'inherit';
ARRAY: 		'array';
fragment TRUE: 'true';
fragment FALSE: 'false';

// Boolean Op
NEG: 	'!';	
AND: 	'&&';
OR: 	'||';
EQUAL: 	'==';
DIF: 	'!=';

// Integer and Float Op
PLUS: 	'+';
SUB: 	'-';
MUL: 	'*';
DIV: 	'/';
MOD: 	'%';
LT: 	'<';
LTE: 	'<=';
GT: 	'>';
GTE: 	'>=';

// String op
CONC: '::';

// Seperators
LB: 	'(';		// Left bracket
RB: 	')';		// Right bracket
LSB: 	'[';		// Left Square Bracket
RSB: 	']';		// Right Square Bracket
LCB: 	'{';		// Left BraCes		
RCB: 	'}';		// Right BraCes
DOT: 	'.';		
COMMA: 	',';
SEMI: 	';';
COLON: 	':';
ASSIGN: '=';

// Literals
// Integer
INTTYPE: 	('0'|([1-9] [0-9]* ('_' [0-9]+)*)) {self.text = self.text.replace("_","")};

// FLoat
FLOATTYPE: 	(INTTYPE DECIMAL EXP) {self.text = self.text.replace("_","")}
			| (INTTYPE DECIMAL) {self.text = self.text.replace("_","")}
			| (INTTYPE EXP) {self.text = self.text.replace("_","")}
			| (DECIMAL EXP);
			fragment DECIMAL: '.' [0-9]*;
			fragment EXP: [eE] [-+]? [0-9]+;

// Boolean
BOOLTYPE: 	TRUE 
			| FALSE;

// String
STRINGTYPE: '"' (~[\\\r\n\b\f] | EscSeq | '\\"')*? '"' {self.text = self.text[1:(len(self.text)-1)]};

// Identifiers
IDENTIFIER: [A-Za-z_] [A-Za-z0-9_]*;


CPPCMT: '//' ~[\r\n]* -> skip;
CCMT:  	'/*' .*? '*/' -> skip;
WS : 	[ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment EscSeq: '\\' [bfrnt"'\\];
fragment StringChar: EscSeq | ~[\b\f\r\n\t\\"'];
UNCLOSE_STRING: '"' StringChar* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' StringChar* ('\\' ~[bfrnt'"\\])* {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};