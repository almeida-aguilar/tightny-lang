# Generated from tightny.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by tightnyParser#topLevelItem.
    def visitTopLevelItem(self, ctx:tightnyParser.TopLevelItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#varDecl.
    def visitVarDecl(self, ctx:tightnyParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#constDecl.
    def visitConstDecl(self, ctx:tightnyParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#funDecl.
    def visitFunDecl(self, ctx:tightnyParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#paramList.
    def visitParamList(self, ctx:tightnyParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#parameter.
    def visitParameter(self, ctx:tightnyParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#structDecl.
    def visitStructDecl(self, ctx:tightnyParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#enumDecl.
    def visitEnumDecl(self, ctx:tightnyParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#block.
    def visitBlock(self, ctx:tightnyParser.BlockContext):
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


    # Visit a parse tree produced by tightnyParser#whileStmt.
    def visitWhileStmt(self, ctx:tightnyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#forStmt.
    def visitForStmt(self, ctx:tightnyParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#switchStmt.
    def visitSwitchStmt(self, ctx:tightnyParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#caseStmt.
    def visitCaseStmt(self, ctx:tightnyParser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#returnStmt.
    def visitReturnStmt(self, ctx:tightnyParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#breakStmt.
    def visitBreakStmt(self, ctx:tightnyParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#continueStmt.
    def visitContinueStmt(self, ctx:tightnyParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#typeSpec.
    def visitTypeSpec(self, ctx:tightnyParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#expression.
    def visitExpression(self, ctx:tightnyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#primary.
    def visitPrimary(self, ctx:tightnyParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#argument.
    def visitArgument(self, ctx:tightnyParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#structFieldInit.
    def visitStructFieldInit(self, ctx:tightnyParser.StructFieldInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#directiveCall.
    def visitDirectiveCall(self, ctx:tightnyParser.DirectiveCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tightnyParser#literal.
    def visitLiteral(self, ctx:tightnyParser.LiteralContext):
        return self.visitChildren(ctx)



del tightnyParser