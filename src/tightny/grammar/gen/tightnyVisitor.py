# Generated from /var/home/alm/Projects/tightny-lang/src/tightny/grammar/tightny.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .tightnyParser import tightnyParser
else:
    from tightnyParser import tightnyParser

# This class defines a complete generic visitor for a parse tree produced by tightnyParser.

class tightnyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tightnyParser#program.
    def visitProgram(self, ctx:tightnyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#declaration.
    def visitDeclaration(self, ctx:tightnyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#pinDecl.
    def visitPinDecl(self, ctx:tightnyParser.PinDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#pinMode.
    def visitPinMode(self, ctx:tightnyParser.PinModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#varDecl.
    def visitVarDecl(self, ctx:tightnyParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#statement.
    def visitStatement(self, ctx:tightnyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#assignment.
    def visitAssignment(self, ctx:tightnyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#ifStmt.
    def visitIfStmt(self, ctx:tightnyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#elseIfChain.
    def visitElseIfChain(self, ctx:tightnyParser.ElseIfChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#elseClause.
    def visitElseClause(self, ctx:tightnyParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#whileStmt.
    def visitWhileStmt(self, ctx:tightnyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#writeCall.
    def visitWriteCall(self, ctx:tightnyParser.WriteCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#waitCall.
    def visitWaitCall(self, ctx:tightnyParser.WaitCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#readCall.
    def visitReadCall(self, ctx:tightnyParser.ReadCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#expression.
    def visitExpression(self, ctx:tightnyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#andExpr.
    def visitAndExpr(self, ctx:tightnyParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#notExpr.
    def visitNotExpr(self, ctx:tightnyParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#cmpExpr.
    def visitCmpExpr(self, ctx:tightnyParser.CmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#cmpOp.
    def visitCmpOp(self, ctx:tightnyParser.CmpOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#addExpr.
    def visitAddExpr(self, ctx:tightnyParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#addOp.
    def visitAddOp(self, ctx:tightnyParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#mulExpr.
    def visitMulExpr(self, ctx:tightnyParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#mulOp.
    def visitMulOp(self, ctx:tightnyParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tightnyParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#primary.
    def visitPrimary(self, ctx:tightnyParser.PrimaryContext):
        return self.visitChildren(ctx)



del tightnyParser