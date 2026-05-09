grammar tightny;

// ========== REGLAS DEL PARSER ==========

program : topLevelItem* EOF ;

topLevelItem
    : directiveCall
    | varDecl
    | constDecl
    | funDecl
    | structDecl
    | enumDecl
    ;

varDecl : VAR ID COLON typeSpec (ASSIGN expression)? ;

constDecl : CONST ID COLON typeSpec ASSIGN expression ;

funDecl : FUN (ID | AT_ID) LPAREN paramList? RPAREN (COLON typeSpec)? ASSIGN block END ;

paramList : parameter (COMMA parameter)* ;

parameter : (VAR | CONST)? ID COLON typeSpec ;

structDecl : STRUCT ID ASSIGN (varDecl | constDecl)* END ;

enumDecl : ENUM ID ASSIGN ID (COMMA ID)* END ;

block
    : statement+
    | ELLIPSIS
    ;

statement
    : varDecl
    | constDecl
    | assignment
    | ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | returnStmt
    | breakStmt
    | continueStmt
    | expression
    ;

// Esto va a dajer codigo como `@print() = 10` pero nos tanto evitar el error
// es decidir donde queremos que pase, en nuestro caso, queremos que el
// el analizador semántico se encargue de revisar que las asignaciones sean válidas
assignment : expression (ASSIGN | COMPOUND_ASSIGN) expression ;

ifStmt : IF expression THEN block (ELIF expression THEN block)* (ELSE block)? END ;

whileStmt : WHILE expression DO block END ;

forStmt : FOR varDecl WHILE expression NEXT assignment DO block END ;

switchStmt : SWITCH expression DO caseStmt* (ELSE block)? END ;

caseStmt : CASE expression THEN block ;

returnStmt : RETURN expression? ;

breakStmt : BREAK ;

continueStmt : CONTINUE ;

typeSpec
    : B1_TYPE
    | U_TYPE
    | I_TYPE
    | LBRACKET INT_LIT RBRACKET typeSpec // <-- un array
    | ID // <-- un struct o enum
    ;

expression
    : (NOT | TILDE | MINUS) expression // <-- un operador unario
    | expression (STAR | SLASH | PERCENT) expression // <-- un operador binario
    | expression (PLUS | MINUS) expression // <-- un operador binario
    | expression (LSHIFT | RSHIFT) expression // <-- un operador binario
    | expression AMP expression // <-- un operador binario
    | expression CARET expression // <-- un operador binario
    | expression PIPE expression // <-- un operador binario
    | expression (EQ | NEQ | LT | GT | LE | GE) expression // <-- un operador binario
    | expression AND expression // <-- un operador binario
    | expression OR expression // <-- un operador binario
    | primary
    ;

primary
    : literal
    | ID
    | AT_ID
    | primary LPAREN (argument (COMMA argument)*)? RPAREN // <-- una llamada a función
    | primary LBRACKET expression RBRACKET // <-- un acceso a array
    | primary DOT ID // <-- un acceso a campo de struct o enum
    | LPAREN expression RPAREN // <-- un grupo de expresiones
    | LBRACE (structFieldInit (COMMA structFieldInit)*)? RBRACE // <-- un struct literal
    | LBRACKET (expression (COMMA expression)*)? RBRACKET // <-- un array literal
    ;

argument : expression | typeSpec ;

structFieldInit : ID COLON expression ;

directiveCall : AT_ID LPAREN (argument (COMMA argument)*)? RPAREN ;

literal // <-- agrupador
    : INT_LIT
    | HEX_LIT
    | BIN_LIT
    | CHAR_LIT
    | STRING_LIT
    ;

// ========== REGLAS DEL LEXER ==========

// Keywords (22)
VAR      : 'var' ;
CONST    : 'const' ;
FUN      : 'fun' ;
IF       : 'if' ;
THEN     : 'then' ;
ELIF     : 'elif' ;
ELSE     : 'else' ;
END      : 'end' ;
WHILE    : 'while' ;
DO       : 'do' ;
FOR      : 'for' ;
NEXT     : 'next' ;
BREAK    : 'break' ;
CONTINUE : 'continue' ;
SWITCH   : 'switch' ;
CASE     : 'case' ;
RETURN   : 'return' ;
STRUCT   : 'struct' ;
ENUM     : 'enum' ;
AND      : 'and' ;
OR       : 'or' ;
NOT      : 'not' ;

// Types
B1_TYPE : 'b1' ;
U_TYPE  : 'u' ('8' | '16' | '32') ;
I_TYPE  : 'i' ('8' | '16' | '32') ;

// Operators
ASSIGN : '=' ;
COMPOUND_ASSIGN : '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' ;

PLUS     : '+' ;
MINUS    : '-' ;
STAR     : '*' ;
SLASH    : '/' ;
PERCENT  : '%' ;

AMP      : '&' ;
PIPE     : '|' ;
CARET    : '^' ;
TILDE    : '~' ;
LSHIFT   : '<<' ;
RSHIFT   : '>>' ;

EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
GT : '>' ;
LE : '<=' ;
GE : '>=' ;

// Delimiters
LPAREN   : '(' ;
RPAREN   : ')' ;
LBRACE   : '{' ;
RBRACE   : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
COLON    : ':' ;
COMMA    : ',' ;
DOT      : '.' ;
ELLIPSIS : '...' ;

// Directives and IDs
AT_ID : '@' [a-zA-Z_] [a-zA-Z_0-9]* ;
ID    : [a-zA-Z_] [a-zA-Z_0-9]* ;

// Literals
HEX_LIT : '0x' [0-9a-fA-F]+ ;
BIN_LIT : '0b' [01]+ ;
INT_LIT : [0-9]+ ;
CHAR_LIT : '\'' ( '\\' . | ~['\r\n] ) '\'' ;
STRING_LIT : '"' ( '\\' . | ~[\\"\r\n] )* '"' ;

// Comments
BLOCK_COMMENT : '--[[' .*? ']]' -> skip ;
COMMENT       : '--' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;
