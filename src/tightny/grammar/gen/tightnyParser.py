# Generated from /var/home/alm/Projects/tightny-lang/src/tightny/grammar/tightny.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,235,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,1,0,
        1,0,3,0,57,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,103,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,125,8,8,1,9,1,9,1,9,3,9,130,8,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,5,14,161,8,14,10,14,12,14,164,9,14,1,15,1,15,1,
        15,1,15,1,15,1,15,5,15,172,8,15,10,15,12,15,175,9,15,1,16,1,16,1,
        16,3,16,180,8,16,1,17,1,17,1,17,1,17,1,17,3,17,187,8,17,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,198,8,19,10,19,12,19,201,
        9,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,212,8,21,
        10,21,12,21,215,9,21,1,22,1,22,1,23,1,23,1,23,3,23,222,8,23,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,233,8,24,1,24,0,4,28,
        30,38,42,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,0,4,1,0,12,14,2,0,20,23,29,30,1,0,25,26,1,0,27,
        28,238,0,56,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,75,1,0,0,0,8,77,
        1,0,0,0,10,102,1,0,0,0,12,104,1,0,0,0,14,108,1,0,0,0,16,124,1,0,
        0,0,18,129,1,0,0,0,20,131,1,0,0,0,22,137,1,0,0,0,24,144,1,0,0,0,
        26,149,1,0,0,0,28,154,1,0,0,0,30,165,1,0,0,0,32,179,1,0,0,0,34,186,
        1,0,0,0,36,188,1,0,0,0,38,190,1,0,0,0,40,202,1,0,0,0,42,204,1,0,
        0,0,44,216,1,0,0,0,46,221,1,0,0,0,48,232,1,0,0,0,50,51,3,2,1,0,51,
        52,3,10,5,0,52,57,1,0,0,0,53,57,3,2,1,0,54,57,3,10,5,0,55,57,1,0,
        0,0,56,50,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,1,
        1,0,0,0,58,59,3,4,2,0,59,60,3,2,1,0,60,67,1,0,0,0,61,62,3,8,4,0,
        62,63,3,2,1,0,63,67,1,0,0,0,64,67,3,4,2,0,65,67,3,8,4,0,66,58,1,
        0,0,0,66,61,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,3,1,0,0,0,68,
        69,5,1,0,0,69,70,5,35,0,0,70,71,5,33,0,0,71,72,3,6,3,0,72,73,5,24,
        0,0,73,74,5,36,0,0,74,5,1,0,0,0,75,76,7,0,0,0,76,7,1,0,0,0,77,78,
        5,2,0,0,78,79,5,35,0,0,79,80,5,24,0,0,80,81,3,28,14,0,81,9,1,0,0,
        0,82,83,3,12,6,0,83,84,3,10,5,0,84,103,1,0,0,0,85,86,3,14,7,0,86,
        87,3,10,5,0,87,103,1,0,0,0,88,89,3,20,10,0,89,90,3,10,5,0,90,103,
        1,0,0,0,91,92,3,22,11,0,92,93,3,10,5,0,93,103,1,0,0,0,94,95,3,24,
        12,0,95,96,3,10,5,0,96,103,1,0,0,0,97,103,3,12,6,0,98,103,3,14,7,
        0,99,103,3,20,10,0,100,103,3,22,11,0,101,103,3,24,12,0,102,82,1,
        0,0,0,102,85,1,0,0,0,102,88,1,0,0,0,102,91,1,0,0,0,102,94,1,0,0,
        0,102,97,1,0,0,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,
        101,1,0,0,0,103,11,1,0,0,0,104,105,5,35,0,0,105,106,5,24,0,0,106,
        107,3,28,14,0,107,13,1,0,0,0,108,109,5,3,0,0,109,110,3,28,14,0,110,
        111,5,4,0,0,111,112,3,10,5,0,112,113,3,16,8,0,113,114,3,18,9,0,114,
        115,5,6,0,0,115,15,1,0,0,0,116,117,5,5,0,0,117,118,5,3,0,0,118,119,
        3,28,14,0,119,120,5,4,0,0,120,121,3,10,5,0,121,122,3,16,8,0,122,
        125,1,0,0,0,123,125,1,0,0,0,124,116,1,0,0,0,124,123,1,0,0,0,125,
        17,1,0,0,0,126,127,5,5,0,0,127,130,3,10,5,0,128,130,1,0,0,0,129,
        126,1,0,0,0,129,128,1,0,0,0,130,19,1,0,0,0,131,132,5,7,0,0,132,133,
        3,28,14,0,133,134,5,8,0,0,134,135,3,10,5,0,135,136,5,6,0,0,136,21,
        1,0,0,0,137,138,5,15,0,0,138,139,5,31,0,0,139,140,3,28,14,0,140,
        141,5,34,0,0,141,142,3,28,14,0,142,143,5,32,0,0,143,23,1,0,0,0,144,
        145,5,17,0,0,145,146,5,31,0,0,146,147,3,28,14,0,147,148,5,32,0,0,
        148,25,1,0,0,0,149,150,5,16,0,0,150,151,5,31,0,0,151,152,3,28,14,
        0,152,153,5,32,0,0,153,27,1,0,0,0,154,155,6,14,-1,0,155,156,3,30,
        15,0,156,162,1,0,0,0,157,158,10,2,0,0,158,159,5,10,0,0,159,161,3,
        30,15,0,160,157,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,29,1,0,0,0,164,162,1,0,0,0,165,166,6,15,-1,0,166,167,
        3,32,16,0,167,173,1,0,0,0,168,169,10,2,0,0,169,170,5,9,0,0,170,172,
        3,32,16,0,171,168,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,31,1,0,0,0,175,173,1,0,0,0,176,177,5,11,0,0,177,180,
        3,32,16,0,178,180,3,34,17,0,179,176,1,0,0,0,179,178,1,0,0,0,180,
        33,1,0,0,0,181,182,3,38,19,0,182,183,3,36,18,0,183,184,3,38,19,0,
        184,187,1,0,0,0,185,187,3,38,19,0,186,181,1,0,0,0,186,185,1,0,0,
        0,187,35,1,0,0,0,188,189,7,1,0,0,189,37,1,0,0,0,190,191,6,19,-1,
        0,191,192,3,42,21,0,192,199,1,0,0,0,193,194,10,2,0,0,194,195,3,40,
        20,0,195,196,3,42,21,0,196,198,1,0,0,0,197,193,1,0,0,0,198,201,1,
        0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,39,1,0,0,0,201,199,1,0,
        0,0,202,203,7,2,0,0,203,41,1,0,0,0,204,205,6,21,-1,0,205,206,3,46,
        23,0,206,213,1,0,0,0,207,208,10,2,0,0,208,209,3,44,22,0,209,210,
        3,46,23,0,210,212,1,0,0,0,211,207,1,0,0,0,212,215,1,0,0,0,213,211,
        1,0,0,0,213,214,1,0,0,0,214,43,1,0,0,0,215,213,1,0,0,0,216,217,7,
        3,0,0,217,45,1,0,0,0,218,219,5,26,0,0,219,222,3,46,23,0,220,222,
        3,48,24,0,221,218,1,0,0,0,221,220,1,0,0,0,222,47,1,0,0,0,223,233,
        5,36,0,0,224,233,5,18,0,0,225,233,5,19,0,0,226,233,5,35,0,0,227,
        233,3,26,13,0,228,229,5,31,0,0,229,230,3,28,14,0,230,231,5,32,0,
        0,231,233,1,0,0,0,232,223,1,0,0,0,232,224,1,0,0,0,232,225,1,0,0,
        0,232,226,1,0,0,0,232,227,1,0,0,0,232,228,1,0,0,0,233,49,1,0,0,0,
        13,56,66,102,124,129,162,173,179,186,199,213,221,232
    ]

class tightnyParser ( Parser ):

    grammarFileName = "tightny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pin'", "'var'", "'if'", "'then'", "'else'", 
                     "'end'", "'while'", "'do'", "'and'", "'or'", "'not'", 
                     "'in'", "'out'", "'pullup'", "'write'", "'read'", "'wait'", 
                     "<INVALID>", "<INVALID>", "'=='", "'!='", "'<='", "'>='", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'('", 
                     "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "PIN", "VAR", "IF", "THEN", "ELSE", "END", 
                      "WHILE", "DO", "AND", "OR", "NOT", "IN", "OUT", "PULLUP", 
                      "WRITE", "READ", "WAIT", "ONE", "ZERO", "EQ", "NEQ", 
                      "LE", "GE", "ASSIGN", "PLUS", "MINUS", "STAR", "SLASH", 
                      "LT", "GT", "LPAREN", "RPAREN", "COLON", "COMMA", 
                      "ID", "INT_LIT", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_pinDecl = 2
    RULE_pinMode = 3
    RULE_varDecl = 4
    RULE_statement = 5
    RULE_assignment = 6
    RULE_ifStmt = 7
    RULE_elseIfChain = 8
    RULE_elseClause = 9
    RULE_whileStmt = 10
    RULE_writeCall = 11
    RULE_waitCall = 12
    RULE_readCall = 13
    RULE_expression = 14
    RULE_andExpr = 15
    RULE_notExpr = 16
    RULE_cmpExpr = 17
    RULE_cmpOp = 18
    RULE_addExpr = 19
    RULE_addOp = 20
    RULE_mulExpr = 21
    RULE_mulOp = 22
    RULE_unaryExpr = 23
    RULE_primary = 24

    ruleNames =  [ "program", "declaration", "pinDecl", "pinMode", "varDecl", 
                   "statement", "assignment", "ifStmt", "elseIfChain", "elseClause", 
                   "whileStmt", "writeCall", "waitCall", "readCall", "expression", 
                   "andExpr", "notExpr", "cmpExpr", "cmpOp", "addExpr", 
                   "addOp", "mulExpr", "mulOp", "unaryExpr", "primary" ]

    EOF = Token.EOF
    PIN=1
    VAR=2
    IF=3
    THEN=4
    ELSE=5
    END=6
    WHILE=7
    DO=8
    AND=9
    OR=10
    NOT=11
    IN=12
    OUT=13
    PULLUP=14
    WRITE=15
    READ=16
    WAIT=17
    ONE=18
    ZERO=19
    EQ=20
    NEQ=21
    LE=22
    GE=23
    ASSIGN=24
    PLUS=25
    MINUS=26
    STAR=27
    SLASH=28
    LT=29
    GT=30
    LPAREN=31
    RPAREN=32
    COLON=33
    COMMA=34
    ID=35
    INT_LIT=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(tightnyParser.DeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = tightnyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.declaration()
                self.state = 51
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pinDecl(self):
            return self.getTypedRuleContext(tightnyParser.PinDeclContext,0)


        def declaration(self):
            return self.getTypedRuleContext(tightnyParser.DeclarationContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(tightnyParser.VarDeclContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = tightnyParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.pinDecl()
                self.state = 59
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.varDecl()
                self.state = 62
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.pinDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.varDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PinDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIN(self):
            return self.getToken(tightnyParser.PIN, 0)

        def ID(self):
            return self.getToken(tightnyParser.ID, 0)

        def COLON(self):
            return self.getToken(tightnyParser.COLON, 0)

        def pinMode(self):
            return self.getTypedRuleContext(tightnyParser.PinModeContext,0)


        def ASSIGN(self):
            return self.getToken(tightnyParser.ASSIGN, 0)

        def INT_LIT(self):
            return self.getToken(tightnyParser.INT_LIT, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_pinDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPinDecl" ):
                return visitor.visitPinDecl(self)
            else:
                return visitor.visitChildren(self)




    def pinDecl(self):

        localctx = tightnyParser.PinDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pinDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(tightnyParser.PIN)
            self.state = 69
            self.match(tightnyParser.ID)
            self.state = 70
            self.match(tightnyParser.COLON)
            self.state = 71
            self.pinMode()
            self.state = 72
            self.match(tightnyParser.ASSIGN)
            self.state = 73
            self.match(tightnyParser.INT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PinModeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(tightnyParser.IN, 0)

        def OUT(self):
            return self.getToken(tightnyParser.OUT, 0)

        def PULLUP(self):
            return self.getToken(tightnyParser.PULLUP, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_pinMode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPinMode" ):
                return visitor.visitPinMode(self)
            else:
                return visitor.visitChildren(self)




    def pinMode(self):

        localctx = tightnyParser.PinModeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pinMode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tightnyParser.VAR, 0)

        def ID(self):
            return self.getToken(tightnyParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(tightnyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = tightnyParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(tightnyParser.VAR)
            self.state = 78
            self.match(tightnyParser.ID)
            self.state = 79
            self.match(tightnyParser.ASSIGN)
            self.state = 80
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(tightnyParser.AssignmentContext,0)


        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(tightnyParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(tightnyParser.WhileStmtContext,0)


        def writeCall(self):
            return self.getTypedRuleContext(tightnyParser.WriteCallContext,0)


        def waitCall(self):
            return self.getTypedRuleContext(tightnyParser.WaitCallContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = tightnyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.assignment()
                self.state = 83
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.ifStmt()
                self.state = 86
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.whileStmt()
                self.state = 89
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.writeCall()
                self.state = 92
                self.statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.waitCall()
                self.state = 95
                self.statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.ifStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.whileStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.writeCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 101
                self.waitCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(tightnyParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(tightnyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = tightnyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(tightnyParser.ID)
            self.state = 105
            self.match(tightnyParser.ASSIGN)
            self.state = 106
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(tightnyParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(tightnyParser.THEN, 0)

        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def elseIfChain(self):
            return self.getTypedRuleContext(tightnyParser.ElseIfChainContext,0)


        def elseClause(self):
            return self.getTypedRuleContext(tightnyParser.ElseClauseContext,0)


        def END(self):
            return self.getToken(tightnyParser.END, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = tightnyParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(tightnyParser.IF)
            self.state = 109
            self.expression(0)
            self.state = 110
            self.match(tightnyParser.THEN)
            self.state = 111
            self.statement()
            self.state = 112
            self.elseIfChain()
            self.state = 113
            self.elseClause()
            self.state = 114
            self.match(tightnyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfChainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(tightnyParser.ELSE, 0)

        def IF(self):
            return self.getToken(tightnyParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(tightnyParser.THEN, 0)

        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def elseIfChain(self):
            return self.getTypedRuleContext(tightnyParser.ElseIfChainContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_elseIfChain

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfChain" ):
                return visitor.visitElseIfChain(self)
            else:
                return visitor.visitChildren(self)




    def elseIfChain(self):

        localctx = tightnyParser.ElseIfChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elseIfChain)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(tightnyParser.ELSE)
                self.state = 117
                self.match(tightnyParser.IF)
                self.state = 118
                self.expression(0)
                self.state = 119
                self.match(tightnyParser.THEN)
                self.state = 120
                self.statement()
                self.state = 121
                self.elseIfChain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(tightnyParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_elseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = tightnyParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elseClause)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(tightnyParser.ELSE)
                self.state = 127
                self.statement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(tightnyParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(tightnyParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(tightnyParser.StatementContext,0)


        def END(self):
            return self.getToken(tightnyParser.END, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = tightnyParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(tightnyParser.WHILE)
            self.state = 132
            self.expression(0)
            self.state = 133
            self.match(tightnyParser.DO)
            self.state = 134
            self.statement()
            self.state = 135
            self.match(tightnyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(tightnyParser.WRITE, 0)

        def LPAREN(self):
            return self.getToken(tightnyParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tightnyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tightnyParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(tightnyParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(tightnyParser.RPAREN, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_writeCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteCall" ):
                return visitor.visitWriteCall(self)
            else:
                return visitor.visitChildren(self)




    def writeCall(self):

        localctx = tightnyParser.WriteCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_writeCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(tightnyParser.WRITE)
            self.state = 138
            self.match(tightnyParser.LPAREN)
            self.state = 139
            self.expression(0)
            self.state = 140
            self.match(tightnyParser.COMMA)
            self.state = 141
            self.expression(0)
            self.state = 142
            self.match(tightnyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(tightnyParser.WAIT, 0)

        def LPAREN(self):
            return self.getToken(tightnyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(tightnyParser.RPAREN, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_waitCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitCall" ):
                return visitor.visitWaitCall(self)
            else:
                return visitor.visitChildren(self)




    def waitCall(self):

        localctx = tightnyParser.WaitCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_waitCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(tightnyParser.WAIT)
            self.state = 145
            self.match(tightnyParser.LPAREN)
            self.state = 146
            self.expression(0)
            self.state = 147
            self.match(tightnyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(tightnyParser.READ, 0)

        def LPAREN(self):
            return self.getToken(tightnyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(tightnyParser.RPAREN, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_readCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadCall" ):
                return visitor.visitReadCall(self)
            else:
                return visitor.visitChildren(self)




    def readCall(self):

        localctx = tightnyParser.ReadCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_readCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(tightnyParser.READ)
            self.state = 150
            self.match(tightnyParser.LPAREN)
            self.state = 151
            self.expression(0)
            self.state = 152
            self.match(tightnyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self):
            return self.getTypedRuleContext(tightnyParser.AndExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(tightnyParser.OR, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tightnyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.andExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tightnyParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 157
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 158
                    self.match(tightnyParser.OR)
                    self.state = 159
                    self.andExpr(0) 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self):
            return self.getTypedRuleContext(tightnyParser.NotExprContext,0)


        def andExpr(self):
            return self.getTypedRuleContext(tightnyParser.AndExprContext,0)


        def AND(self):
            return self.getToken(tightnyParser.AND, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_andExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def andExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tightnyParser.AndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_andExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.notExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tightnyParser.AndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpr)
                    self.state = 168
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 169
                    self.match(tightnyParser.AND)
                    self.state = 170
                    self.notExpr() 
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(tightnyParser.NOT, 0)

        def notExpr(self):
            return self.getTypedRuleContext(tightnyParser.NotExprContext,0)


        def cmpExpr(self):
            return self.getTypedRuleContext(tightnyParser.CmpExprContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_notExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)




    def notExpr(self):

        localctx = tightnyParser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_notExpr)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(tightnyParser.NOT)
                self.state = 177
                self.notExpr()
                pass
            elif token in [16, 18, 19, 26, 31, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.cmpExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tightnyParser.AddExprContext)
            else:
                return self.getTypedRuleContext(tightnyParser.AddExprContext,i)


        def cmpOp(self):
            return self.getTypedRuleContext(tightnyParser.CmpOpContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_cmpExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpExpr" ):
                return visitor.visitCmpExpr(self)
            else:
                return visitor.visitChildren(self)




    def cmpExpr(self):

        localctx = tightnyParser.CmpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmpExpr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.addExpr(0)
                self.state = 182
                self.cmpOp()
                self.state = 183
                self.addExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.addExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(tightnyParser.EQ, 0)

        def NEQ(self):
            return self.getToken(tightnyParser.NEQ, 0)

        def LT(self):
            return self.getToken(tightnyParser.LT, 0)

        def GT(self):
            return self.getToken(tightnyParser.GT, 0)

        def LE(self):
            return self.getToken(tightnyParser.LE, 0)

        def GE(self):
            return self.getToken(tightnyParser.GE, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_cmpOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpOp" ):
                return visitor.visitCmpOp(self)
            else:
                return visitor.visitChildren(self)




    def cmpOp(self):

        localctx = tightnyParser.CmpOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmpOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1626341376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self):
            return self.getTypedRuleContext(tightnyParser.MulExprContext,0)


        def addExpr(self):
            return self.getTypedRuleContext(tightnyParser.AddExprContext,0)


        def addOp(self):
            return self.getTypedRuleContext(tightnyParser.AddOpContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_addExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tightnyParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tightnyParser.AddExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 193
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 194
                    self.addOp()
                    self.state = 195
                    self.mulExpr(0) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(tightnyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(tightnyParser.MINUS, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_addOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = tightnyParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(tightnyParser.UnaryExprContext,0)


        def mulExpr(self):
            return self.getTypedRuleContext(tightnyParser.MulExprContext,0)


        def mulOp(self):
            return self.getTypedRuleContext(tightnyParser.MulOpContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_mulExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tightnyParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tightnyParser.MulExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    self.mulOp()
                    self.state = 209
                    self.unaryExpr() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(tightnyParser.STAR, 0)

        def SLASH(self):
            return self.getToken(tightnyParser.SLASH, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_mulOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = tightnyParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(tightnyParser.MINUS, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(tightnyParser.UnaryExprContext,0)


        def primary(self):
            return self.getTypedRuleContext(tightnyParser.PrimaryContext,0)


        def getRuleIndex(self):
            return tightnyParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = tightnyParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryExpr)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(tightnyParser.MINUS)
                self.state = 219
                self.unaryExpr()
                pass
            elif token in [16, 18, 19, 31, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(tightnyParser.INT_LIT, 0)

        def ONE(self):
            return self.getToken(tightnyParser.ONE, 0)

        def ZERO(self):
            return self.getToken(tightnyParser.ZERO, 0)

        def ID(self):
            return self.getToken(tightnyParser.ID, 0)

        def readCall(self):
            return self.getTypedRuleContext(tightnyParser.ReadCallContext,0)


        def LPAREN(self):
            return self.getToken(tightnyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(tightnyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(tightnyParser.RPAREN, 0)

        def getRuleIndex(self):
            return tightnyParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = tightnyParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primary)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(tightnyParser.INT_LIT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(tightnyParser.ONE)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(tightnyParser.ZERO)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.match(tightnyParser.ID)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.readCall()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.match(tightnyParser.LPAREN)
                self.state = 229
                self.expression(0)
                self.state = 230
                self.match(tightnyParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        self._predicates[15] = self.andExpr_sempred
        self._predicates[19] = self.addExpr_sempred
        self._predicates[21] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def andExpr_sempred(self, localctx:AndExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




