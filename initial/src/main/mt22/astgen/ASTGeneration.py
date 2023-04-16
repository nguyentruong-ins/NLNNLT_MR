from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    # Visit a parse tree produced by MT22Parser#program.
    # program: 	decllist EOF;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # Visit a parse tree produced by MT22Parser#decllist.
    # decllist: 	decl decllist | decl;
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    # Visit a parse tree produced by MT22Parser#decl.
    # decl: 		variabledcl | funcdcl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.funcdcl():
            return [self.visit(ctx.funcdcl())]
        return self.visit(ctx.variabledcl())


    # Visit a parse tree produced by MT22Parser#arrdcl.
    # arrdcl: 	ARRAY LSB intlist RSB OF atom;
    def visitArrdcl(self, ctx:MT22Parser.ArrdclContext):
        dimensions = self.visit(ctx.intlist())
        typ = self.visit(ctx.atom())
        return ArrayType(dimensions, typ)


    # Visit a parse tree produced by MT22Parser#atom.
    # atom: 		BOOLEAN | INTEGER| FLOAT | STRING;
    def visitAtom(self, ctx:MT22Parser.AtomContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        return StringType()


    # Visit a parse tree produced by MT22Parser#intlist.
    # intlist: 	(INTTYPE COMMA) intlist | INTTYPE;
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [((ctx.INTTYPE().getText()))]
        return [((ctx.INTTYPE().getText()))] + self.visit(ctx.intlist())


    # Visit a parse tree produced by MT22Parser#variabledcl.
    # variabledcl: (vardcl_full | vardcl_short) SEMI;
    def visitVariabledcl(self, ctx:MT22Parser.VariabledclContext):
        if ctx.vardcl_full():
            return self.visit(ctx.vardcl_full())
        return self.visit(ctx.vardcl_short())


    # Visit a parse tree produced by MT22Parser#vardcl_full.
    # vardcl_full: IDENTIFIER COMMA vardcl_full COMMA expr
    # 			| IDENTIFIER ':' paratype '=' expr;
    def helper(self, ctx:MT22Parser.Vardcl_fullContext):
        if ctx.paratype():
            name = ctx.IDENTIFIER().getText()
            typ = self.visit(ctx.paratype())
            init = self.visit(ctx.expr())
            # init = ctx.expr()
            return [name], [init], [typ]
        deeper = self.helper(ctx.vardcl_full())
        name = ctx.IDENTIFIER().getText()
        # typ = self.visit(ctx.paratype())
        init = self.visit(ctx.expr())
        return ([name] + deeper[0], [init] + deeper[1], [] + deeper[2])
    def visitVardcl_full(self, ctx:MT22Parser.Vardcl_fullContext):
        args = self.helper(ctx)
        name_list = args[0]
        init = args[1][::-1]
        # print(init)
        typ = args[2][0]
        return list(map(lambda x, y: VarDecl(x, typ, y), name_list, init))

    # Visit a parse tree produced by MT22Parser#vardcl_short.
    # vardcl_short: idlist ':' paratype;
    def visitVardcl_short(self, ctx:MT22Parser.Vardcl_shortContext):
        idlist = self.visit(ctx.idlist())
        typ = self.visit(ctx.paratype())
        return list(map(lambda x: VarDecl(x, typ, None), idlist))


    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: 	(IDENTIFIER COMMA) idlist | IDENTIFIER;	
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [(ctx.IDENTIFIER().getText())]
        return [(ctx.IDENTIFIER().getText())] + self.visit(ctx.idlist())


    # Visit a parse tree produced by MT22Parser#paradcl.
    # paradcl: 	(INHERIT)? (OUT)? IDENTIFIER COLON paratype;
    def visitParadcl(self, ctx:MT22Parser.ParadclContext):
        name = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.paratype())
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(name, typ, out, inherit)


    # Visit a parse tree produced by MT22Parser#paratype.
    # paratype: BOOLEAN | INTEGER | FLOAT | STRING | arrdcl | AUTO;
    def visitParatype(self, ctx:MT22Parser.ParatypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arrdcl():
            return self.visit(ctx.arrdcl())
        return AutoType()


    # Visit a parse tree produced by MT22Parser#funcdcl.
    # funcdcl: 	IDENTIFIER COLON FUNCTION functype LB paralist RB (INHERIT IDENTIFIER)? blockstmt;
    def visitFuncdcl(self, ctx:MT22Parser.FuncdclContext):
        name = ctx.IDENTIFIER(0).getText()
        return_type = self.visit(ctx.functype())
        params = self.visit(ctx.paralist())
        body = self.visit(ctx.blockstmt())
        if ctx.INHERIT():
            inherit = ctx.IDENTIFIER(1).getText()
            return FuncDecl(name, return_type, params, inherit, body)
        return FuncDecl(name, return_type, params, None, body)


    # Visit a parse tree produced by MT22Parser#functype.
    # functype: BOOLEAN | INTEGER | FLOAT | STRING | VOID | arrdcl | AUTO;
    def visitFunctype(self, ctx:MT22Parser.FunctypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.arrdcl():
            return self.visit(ctx.arrdcl())
        return AutoType()


    # Visit a parse tree produced by MT22Parser#paralist.
    # paralist: 	paraprime |;
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        if ctx.paraprime():
            return self.visit(ctx.paraprime())
        return []


    # Visit a parse tree produced by MT22Parser#paraprime.
    # paraprime: 	(paradcl COMMA) paraprime | paradcl;
    def visitParaprime(self, ctx:MT22Parser.ParaprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paradcl())]
        return [self.visit(ctx.paradcl())] + self.visit(ctx.paraprime())


    # Visit a parse tree produced by MT22Parser#expr.
    # expr: expr1 CONC expr1 | expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        return BinExpr(ctx.CONC().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))


    # Visit a parse tree produced by MT22Parser#expr1.
    # expr1: expr2 Binary1 expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinExpr(ctx.Binary1().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visitChildren(ctx)

    #####################################
    # VISITOR: Binary1

    # Visit a parse tree produced by MT22Parser#expr2.
    # expr2: expr2 Binary2 expr3 | expr3;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        return BinExpr(ctx.Binary2().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visitChildren(ctx)

    #####################################
    # VISITOR: Binary2

    # Visit a parse tree produced by MT22Parser#expr3.
    # expr3: expr3 (PLUS | SUB) expr4 | expr4;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        return BinExpr(ctx.PLUS().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) if ctx.PLUS() else BinExpr(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    #####################################
    # VISITOR: Binary3

    # Visit a parse tree produced by MT22Parser#expr4.
    # expr4: expr4 Binary4 expr5 | expr5;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        return BinExpr(ctx.Binary4().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visitChildren(ctx)

    #####################################
    # VISITOR: Binary4

    # Visit a parse tree produced by MT22Parser#expr5.
    # expr5: NEG expr5 | expr6;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.NEG():
            return UnExpr(ctx.NEG().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    # expr6: SUB expr6 | expr7;   
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())


    # Visit a parse tree produced by MT22Parser#expr7.
    # expr7: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | arraylit | lhs | func_call | sub_expr;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.INTTYPE():
            return IntegerLit(int(ctx.INTTYPE().getText()))
        elif ctx.FLOATTYPE():
            # if (ctx.FLOATTYPE().getText()[:1] == ".e"):
            #     return FLoatLit(float("0" + ctx.FLOATTYPE().getText()))
            return FloatLit(float("0" + ctx.FLOATTYPE().getText()))
        elif ctx.BOOLTYPE():
            return BooleanLit(ctx.BOOLTYPE().getText() == 'true')
        elif ctx.STRINGTYPE():
            return StringLit(ctx.STRINGTYPE().getText())
        elif ctx.arraylit():
            explist = self.visit(ctx.arraylit())            
            return ArrayLit(explist)
        elif ctx.lhs():
            return self.visit(ctx.lhs())
        elif ctx.sub_expr():
            return self.visit(ctx.sub_expr())
        return self.visit(ctx.func_call())

    def visitSub_expr(self, ctx:MT22Parser.Sub_exprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#arraylit.
    # arraylit: 	LCB nullable_explist RCB;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visit(ctx.nullable_explist())


    # Visit a parse tree produced by MT22Parser#nullable_explist.
    # nullable_explist: exprlist | ;
    def visitNullable_explist(self, ctx:MT22Parser.Nullable_explistContext):
        if ctx.exprlist():
            return self.visit(ctx.exprlist())
        return []

    # Visit a parse tree produced by MT22Parser#idexop.
    # idexop: 	IDENTIFIER LSB explist RSB;
    def visitIdexop(self, ctx:MT22Parser.IdexopContext):
        name = ctx.IDENTIFIER().getText()
        cell = self.visit(ctx.exprlist())
        return ArrayCell(name, cell)


    # Visit a parse tree produced by MT22Parser#func_call.
    # func_call: 	IDENTIFIER LB nullable_explist RB;
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        name = ctx.IDENTIFIER().getText()
        args = self.visit(ctx.nullable_explist())
        return FuncCall(name, args)


    # Visit a parse tree produced by MT22Parser#stmt.
    # stmt: 		assignstmt | ifstmt | forstmt | whilestmt | dwstmt | callstmt | blockstmt | rtrnstmt | brkstmt | constmt | null_stmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        elif ctx.dwstmt():
            return self.visit(ctx.dwstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.rtrnstmt():
            return self.visit(ctx.rtrnstmt())
        elif ctx.constmt():
            return self.visit(ctx.constmt())
        elif ctx.null_stmt():
            return self.visit(ctx.null_stmt())
        return self.visit(ctx.brkstmt())

    # Visit a parse tree produced by MT22Parser#null_stmt.
    # null_stmt: ';' ;
    def visitNull_stmt(self, ctx:MT22Parser.Null_stmtContext):
        return None

    # Visit a parse tree produced by MT22Parser#assignstmt.
    # assignstmt: assign SEMI;
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visit(ctx.assign())

    def visitAssign(self, ctx:MT22Parser.AssignContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)

    # Visit a parse tree produced by MT22Parser#lhs.
    # lhs: 		IDENTIFIER | idexop;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.idexop())


    # Visit a parse tree produced by MT22Parser#ifstmt.
    # ifstmt: 	IF LB expr RB stmt (ELSE stmt)?;
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        if ctx.ELSE():
            cond = self.visit(ctx.expr())
            tstmt = self.visit(ctx.stmt(0))
            fstmt = self.visit(ctx.stmt(1))
            return IfStmt(cond, tstmt, fstmt)
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        return IfStmt(cond, tstmt)


    # Visit a parse tree produced by MT22Parser#forstmt.
    # forstmt: 	FOR LB assign COMMA expr COMMA expr RB stmt;
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        init = self.visit(ctx.assign())
        cond = self.visit(ctx.expr(0))
        upd = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    # whilestmt: 	WHILE LB expr RB stmt;
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#dwstmt.
    # dwstmt: 	DO blockstmt WHILE LB expr RB SEMI;
    def visitDwstmt(self, ctx:MT22Parser.DwstmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#brkstmt.
    def visitBrkstmt(self, ctx:MT22Parser.BrkstmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#constmt.
    def visitConstmt(self, ctx:MT22Parser.ConstmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#rtrnstmt.
    # rtrnstmt: 	RETURN expr? SEMI;
    def visitRtrnstmt(self, ctx:MT22Parser.RtrnstmtContext):
        # if ctx.expr():
        expr = self.visit(ctx.expr()) if ctx.expr() else []
        return ReturnStmt(expr)


    # Visit a parse tree produced by MT22Parser#exprlist.
    # exprlist: 	expr COMMA explist | expr;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # Visit a parse tree produced by MT22Parser#callstmt.
    # callstmt: 	IDENTIFIER LB exprlist? RB SEMI;
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        if ctx.getChildCount() == 5:
           name = (ctx.IDENTIFIER().getText())
           args = self.visit(ctx.exprlist())
           return CallStmt(name, args) 
        
        name = (ctx.IDENTIFIER().getText())
        return CallStmt(name, [])


    # Visit a parse tree produced by MT22Parser#blockstmt.
    # blockstmt: 	LCB	stmtlist RCB;
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        body = self.visit(ctx.stmtlist())
        return BlockStmt(body)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    # stmtlist: 	stmtprime |;
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmtprime())
        return []

    # Visit a parse tree produced by MT22Parser#stmtprime.
    # stmtprime: 	stmttype stmtprime | stmttype;
    def visitStmtprime(self, ctx:MT22Parser.StmtprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmttype())
        return self.visit(ctx.stmttype()) + self.visit(ctx.stmtprime())


    # Visit a parse tree produced by MT22Parser#stmttype.
    # stmttype: stmt | variabledcl;
    def visitStmttype(self, ctx:MT22Parser.StmttypeContext):
        return [self.visit(ctx.stmt())] if ctx.stmt() else self.visit(ctx.variabledcl())
