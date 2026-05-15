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

// Esto va a aceptar codigo como `@print() = 10` pero no es tanto evitar el error,
// es decidir donde queremos que pase. En nuestro caso, queremos que el
// analizador semántico se encargue de revisar que las asignaciones sean válidas.
assignment
    : expression ASSIGN        expression
    | expression PLUS_ASSIGN   expression
    | expression MINUS_ASSIGN  expression
    | expression STAR_ASSIGN   expression
    | expression SLASH_ASSIGN  expression
    | expression MOD_ASSIGN    expression
    | expression AMP_ASSIGN    expression
    | expression PIPE_ASSIGN   expression
    | expression CARET_ASSIGN  expression
    | expression LSHIFT_ASSIGN expression
    | expression RSHIFT_ASSIGN expression
    ;

ifStmt : IF expression THEN block (ELIF expression THEN block)* (ELSE block)? END ;

whileStmt : WHILE expression DO block END ;

// NEXT acepta assignment, el step siempre es una asignación explícita
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
    | ID                                 // <-- un struct o enum
    ;

// Los operadores unarios van al final para tener mayor precedencia que los binarios.
// Así `not a and b` se parsea como `(not a) and b`, no como `not (a and b)`.
expression
    : expression (STAR | SLASH | PERCENT) expression        // <-- multiplicativo
    | expression (PLUS | MINUS) expression                  // <-- aditivo
    | expression (LSHIFT | RSHIFT) expression               // <-- desplazamiento de bits
    | expression AMP expression                             // <-- AND bit a bit
    | expression CARET expression                           // <-- XOR bit a bit
    | expression PIPE expression                            // <-- OR bit a bit
    | expression (EQ | NEQ | LT | GT | LE | GE) expression // <-- comparación
    | expression AND expression                             // <-- AND lógico
    | expression OR expression                              // <-- OR lógico
    | (NOT | TILDE | MINUS) expression                      // <-- unario (mayor precedencia)
    | primary
    ;

// AT_ID se deja como base de primary para permitir llamadas a directivas (@pin_mode(...))
// pero una directiva sola sin llamada es inválida semánticamente, no gramaticalmente.
primary
    : literal
    | ID
    | AT_ID
    | primary LPAREN (argument (COMMA argument)*)? RPAREN   // <-- llamada a función o directiva
    | primary LBRACKET expression RBRACKET                  // <-- acceso a array
    | primary DOT ID                                        // <-- acceso a campo de struct o enum
    | LPAREN expression RPAREN                              // <-- expresión agrupada
    | LBRACE (structFieldInit (COMMA structFieldInit)*)? RBRACE  // <-- struct literal
    | LBRACKET (expression (COMMA expression)*)? RBRACKET   // <-- array literal
    ;

// expression | typeSpec: el semántico decide si un ID es tipo o variable.
// Permite llamadas como @as(i8, x) donde i8 es un typeSpec.
argument : expression | typeSpec ;

structFieldInit : ID COLON expression ;

directiveCall : AT_ID LPAREN (argument (COMMA argument)*)? RPAREN ;

literal
    : INT_LIT
    | HEX_LIT
    | BIN_LIT
    | CHAR_LIT
    | STRING_LIT
    ;

// ========== REGLAS DEL LEXER ==========

// Keywords
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

// Compound assignment operators (antes que los operadores simples para evitar ambigüedad)
LSHIFT_ASSIGN : '<<=' ;
RSHIFT_ASSIGN : '>>=' ;
PLUS_ASSIGN   : '+=' ;
MINUS_ASSIGN  : '-=' ;
STAR_ASSIGN   : '*=' ;
SLASH_ASSIGN  : '/=' ;
MOD_ASSIGN    : '%=' ;
AMP_ASSIGN    : '&=' ;
PIPE_ASSIGN   : '|=' ;
CARET_ASSIGN  : '^=' ;

// Comparison operators (antes que los simples < > =)
EQ  : '==' ;
NEQ : '!=' ;
LE  : '<=' ;
GE  : '>=' ;

// Simple assignment (después de == para evitar ambigüedad)
ASSIGN : '=' ;

// Arithmetic operators
PLUS    : '+' ;
MINUS   : '-' ;
STAR    : '*' ;
SLASH   : '/' ;
PERCENT : '%' ;

// Bitwise operators
AMP    : '&' ;
PIPE   : '|' ;
CARET  : '^' ;
TILDE  : '~' ;
LSHIFT : '<<' ;
RSHIFT : '>>' ;

// Comparison operators
LT : '<' ;
GT : '>' ;

// Delimiters
// ELLIPSIS va antes que DOT para que '...' no se tokenice como tres '.'
ELLIPSIS : '...' ;
LPAREN   : '(' ;
RPAREN   : ')' ;
LBRACE   : '{' ;
RBRACE   : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
COLON    : ':' ;
COMMA    : ',' ;
DOT      : '.' ;

// Directives and IDs
AT_ID : '@' [a-zA-Z_] [a-zA-Z_0-9]* ;
ID    : [a-zA-Z_] [a-zA-Z_0-9]* ;

// Literals
HEX_LIT    : '0x' [0-9a-fA-F]+ ;
BIN_LIT    : '0b' [01]+ ;
INT_LIT    : [0-9]+ ;
CHAR_LIT   : '\'' ( '\\' . | ~['\r\n] ) '\'' ;
STRING_LIT : '"' ( '\\' . | ~[\\"\r\n] )* '"' ;

// Comments
BLOCK_COMMENT : '--[[' .*? ']]' -> skip ;
COMMENT       : '--' ~[\r\n]* -> skip ;

WS : [ \t\r\n]+ -> skip ;
