grammar tightny;

// ===== PARSER =====

program
    : declaration statement
    | declaration
    | statement
    |
    ;

// Declaraciones Globales
declaration
    : pinDecl declaration
    | varDecl declaration
    | pinDecl
    | varDecl
    ;

pinDecl : PIN ID COLON pinMode ASSIGN INT_LIT ;

pinMode
    : IN
    | OUT
    | PULLUP
    ;

varDecl : VAR ID ASSIGN expression ;

// Statements
statement
    : assignment statement
    | ifStmt statement
    | whileStmt statement
    | writeCall statement
    | waitCall statement
    | assignment
    | ifStmt
    | whileStmt
    | writeCall
    | waitCall
    ;

assignment : ID ASSIGN expression ;

// Condicionales
ifStmt : IF expression THEN statement elseIfChain elseClause END ;

elseIfChain
    : ELSE IF expression THEN statement elseIfChain
    |
    ;

elseClause
    : ELSE statement
    |
    ;

// Bucles
whileStmt : WHILE expression DO statement END ;

// Llamadas built-in
writeCall : WRITE LPAREN expression COMMA expression RPAREN ;
waitCall  : WAIT  LPAREN expression RPAREN ;
readCall  : READ  LPAREN expression RPAREN ;

// Expresiones
expression
    : expression OR andExpr
    | andExpr
    ;

andExpr
    : andExpr AND notExpr
    | notExpr
    ;

notExpr
    : NOT notExpr
    | cmpExpr
    ;

cmpExpr
    : addExpr cmpOp addExpr
    | addExpr
    ;

cmpOp : EQ | NEQ | LT | GT | LE | GE ;

addExpr
    : addExpr addOp mulExpr
    | mulExpr
    ;

addOp : PLUS | MINUS ;

mulExpr
    : mulExpr mulOp unaryExpr
    | unaryExpr
    ;

mulOp : STAR | SLASH ;

unaryExpr
    : MINUS unaryExpr
    | primary
    ;

primary
    : INT_LIT
    | ONE
    | ZERO
    | ID
    | readCall
    | LPAREN expression RPAREN
    ;

// ===== LEXER =====

// Keywords
PIN    : 'pin'    ;
VAR    : 'var'    ;
IF     : 'if'     ;
THEN   : 'then'   ;
ELSE   : 'else'   ;
END    : 'end'    ;
WHILE  : 'while'  ;
DO     : 'do'     ;
AND    : 'and'    ;
OR     : 'or'     ;
NOT    : 'not'    ;

// Modos de pin
IN     : 'in'     ;
OUT    : 'out'    ;
PULLUP : 'pullup' ;

// Funciones predefinidas
WRITE  : 'write'  ; // digital
READ   : 'read'   ; // digital
WAIT   : 'wait'   ;

// Constantes
ONE : 'high' | 'true' ;
ZERO : 'low' | 'false' ;

// Operadores de comparación (antes que los simples < > =)
EQ  : '==' ;
NEQ : '!=' ;
LE  : '<=' ;
GE  : '>=' ;

// Asignación
ASSIGN : '=' ;

// Operadores aritméticos
PLUS    : '+' ;
MINUS   : '-' ;
STAR    : '*' ;
SLASH   : '/' ;

// Operadores de comparación
LT : '<' ;
GT : '>' ;

// Delimiteradores
LPAREN   : '(' ;
RPAREN   : ')' ;
COLON    : ':' ;
COMMA    : ',' ;

// ID y literales
ID      : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT_LIT : [0-9]+ ;

// Ignorar
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;
