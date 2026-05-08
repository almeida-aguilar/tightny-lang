# Generated from tightny.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .tightnyParser import tightnyParser
else:
    from tightnyParser import tightnyParser

# This class defines a complete listener for a parse tree produced by tightnyParser.
class tightnyListener(ParseTreeListener):

    # Enter a parse tree produced by tightnyParser#program.
    def enterProgram(self, ctx:tightnyParser.ProgramContext):
        pass

    # Exit a parse tree produced by tightnyParser#program.
    def exitProgram(self, ctx:tightnyParser.ProgramContext):
        pass


    # Enter a parse tree produced by tightnyParser#topLevelItem.
    def enterTopLevelItem(self, ctx:tightnyParser.TopLevelItemContext):
        pass

    # Exit a parse tree produced by tightnyParser#topLevelItem.
    def exitTopLevelItem(self, ctx:tightnyParser.TopLevelItemContext):
        pass


    # Enter a parse tree produced by tightnyParser#varDecl.
    def enterVarDecl(self, ctx:tightnyParser.VarDeclContext):
        pass

    # Exit a parse tree produced by tightnyParser#varDecl.
    def exitVarDecl(self, ctx:tightnyParser.VarDeclContext):
        pass


    # Enter a parse tree produced by tightnyParser#constDecl.
    def enterConstDecl(self, ctx:tightnyParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by tightnyParser#constDecl.
    def exitConstDecl(self, ctx:tightnyParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by tightnyParser#funDecl.
    def enterFunDecl(self, ctx:tightnyParser.FunDeclContext):
        pass

    # Exit a parse tree produced by tightnyParser#funDecl.
    def exitFunDecl(self, ctx:tightnyParser.FunDeclContext):
        pass


    # Enter a parse tree produced by tightnyParser#paramList.
    def enterParamList(self, ctx:tightnyParser.ParamListContext):
        pass

    # Exit a parse tree produced by tightnyParser#paramList.
    def exitParamList(self, ctx:tightnyParser.ParamListContext):
        pass


    # Enter a parse tree produced by tightnyParser#parameter.
    def enterParameter(self, ctx:tightnyParser.ParameterContext):
        pass

    # Exit a parse tree produced by tightnyParser#parameter.
    def exitParameter(self, ctx:tightnyParser.ParameterContext):
        pass


    # Enter a parse tree produced by tightnyParser#structDecl.
    def enterStructDecl(self, ctx:tightnyParser.StructDeclContext):
        pass

    # Exit a parse tree produced by tightnyParser#structDecl.
    def exitStructDecl(self, ctx:tightnyParser.StructDeclContext):
        pass


    # Enter a parse tree produced by tightnyParser#enumDecl.
    def enterEnumDecl(self, ctx:tightnyParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by tightnyParser#enumDecl.
    def exitEnumDecl(self, ctx:tightnyParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by tightnyParser#block.
    def enterBlock(self, ctx:tightnyParser.BlockContext):
        pass

    # Exit a parse tree produced by tightnyParser#block.
    def exitBlock(self, ctx:tightnyParser.BlockContext):
        pass


    # Enter a parse tree produced by tightnyParser#statement.
    def enterStatement(self, ctx:tightnyParser.StatementContext):
        pass

    # Exit a parse tree produced by tightnyParser#statement.
    def exitStatement(self, ctx:tightnyParser.StatementContext):
        pass


    # Enter a parse tree produced by tightnyParser#assignment.
    def enterAssignment(self, ctx:tightnyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by tightnyParser#assignment.
    def exitAssignment(self, ctx:tightnyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by tightnyParser#ifStmt.
    def enterIfStmt(self, ctx:tightnyParser.IfStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#ifStmt.
    def exitIfStmt(self, ctx:tightnyParser.IfStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#whileStmt.
    def enterWhileStmt(self, ctx:tightnyParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#whileStmt.
    def exitWhileStmt(self, ctx:tightnyParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#forStmt.
    def enterForStmt(self, ctx:tightnyParser.ForStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#forStmt.
    def exitForStmt(self, ctx:tightnyParser.ForStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#switchStmt.
    def enterSwitchStmt(self, ctx:tightnyParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#switchStmt.
    def exitSwitchStmt(self, ctx:tightnyParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#caseStmt.
    def enterCaseStmt(self, ctx:tightnyParser.CaseStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#caseStmt.
    def exitCaseStmt(self, ctx:tightnyParser.CaseStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#returnStmt.
    def enterReturnStmt(self, ctx:tightnyParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#returnStmt.
    def exitReturnStmt(self, ctx:tightnyParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#breakStmt.
    def enterBreakStmt(self, ctx:tightnyParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#breakStmt.
    def exitBreakStmt(self, ctx:tightnyParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#continueStmt.
    def enterContinueStmt(self, ctx:tightnyParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by tightnyParser#continueStmt.
    def exitContinueStmt(self, ctx:tightnyParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by tightnyParser#typeSpec.
    def enterTypeSpec(self, ctx:tightnyParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by tightnyParser#typeSpec.
    def exitTypeSpec(self, ctx:tightnyParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by tightnyParser#expression.
    def enterExpression(self, ctx:tightnyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by tightnyParser#expression.
    def exitExpression(self, ctx:tightnyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by tightnyParser#primary.
    def enterPrimary(self, ctx:tightnyParser.PrimaryContext):
        pass

    # Exit a parse tree produced by tightnyParser#primary.
    def exitPrimary(self, ctx:tightnyParser.PrimaryContext):
        pass


    # Enter a parse tree produced by tightnyParser#argument.
    def enterArgument(self, ctx:tightnyParser.ArgumentContext):
        pass

    # Exit a parse tree produced by tightnyParser#argument.
    def exitArgument(self, ctx:tightnyParser.ArgumentContext):
        pass


    # Enter a parse tree produced by tightnyParser#structFieldInit.
    def enterStructFieldInit(self, ctx:tightnyParser.StructFieldInitContext):
        pass

    # Exit a parse tree produced by tightnyParser#structFieldInit.
    def exitStructFieldInit(self, ctx:tightnyParser.StructFieldInitContext):
        pass


    # Enter a parse tree produced by tightnyParser#directiveCall.
    def enterDirectiveCall(self, ctx:tightnyParser.DirectiveCallContext):
        pass

    # Exit a parse tree produced by tightnyParser#directiveCall.
    def exitDirectiveCall(self, ctx:tightnyParser.DirectiveCallContext):
        pass


    # Enter a parse tree produced by tightnyParser#literal.
    def enterLiteral(self, ctx:tightnyParser.LiteralContext):
        pass

    # Exit a parse tree produced by tightnyParser#literal.
    def exitLiteral(self, ctx:tightnyParser.LiteralContext):
        pass



del tightnyParser