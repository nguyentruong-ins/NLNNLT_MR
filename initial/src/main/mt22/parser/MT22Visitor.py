# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

from lexererr import *


# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrdcl.
    def visitArrdcl(self, ctx:MT22Parser.ArrdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atom.
    def visitAtom(self, ctx:MT22Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variabledcl.
    def visitVariabledcl(self, ctx:MT22Parser.VariabledclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardcl_full.
    def visitVardcl_full(self, ctx:MT22Parser.Vardcl_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardcl_short.
    def visitVardcl_short(self, ctx:MT22Parser.Vardcl_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradcl.
    def visitParadcl(self, ctx:MT22Parser.ParadclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paratype.
    def visitParatype(self, ctx:MT22Parser.ParatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdcl.
    def visitFuncdcl(self, ctx:MT22Parser.FuncdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functype.
    def visitFunctype(self, ctx:MT22Parser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paralist.
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paraprime.
    def visitParaprime(self, ctx:MT22Parser.ParaprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_expr.
    def visitSub_expr(self, ctx:MT22Parser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nullable_explist.
    def visitNullable_explist(self, ctx:MT22Parser.Nullable_explistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idexop.
    def visitIdexop(self, ctx:MT22Parser.IdexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#null_stmt.
    def visitNull_stmt(self, ctx:MT22Parser.Null_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign.
    def visitAssign(self, ctx:MT22Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dwstmt.
    def visitDwstmt(self, ctx:MT22Parser.DwstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#brkstmt.
    def visitBrkstmt(self, ctx:MT22Parser.BrkstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#constmt.
    def visitConstmt(self, ctx:MT22Parser.ConstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#rtrnstmt.
    def visitRtrnstmt(self, ctx:MT22Parser.RtrnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtprime.
    def visitStmtprime(self, ctx:MT22Parser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmttype.
    def visitStmttype(self, ctx:MT22Parser.StmttypeContext):
        return self.visitChildren(ctx)



del MT22Parser