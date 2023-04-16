from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Reg import *
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
    
    # def init(self):
    #     return [Symbol("getInt", MType(list(), IntegerType()), CName(self.libName)),
    #                 Symbol("putInt", MType([IntegerType()], VoidType()), CName(self.libName)),
    #                 Symbol("putIntLn", MType([IntegerType()], VoidType()), CName(self.libName))] 

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        # gl = self.init()
        gc = CodeGenVisitor(ast, None, dir_)
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".asm")

    def visitIntegerType(self, ctx, o): pass
    def visitFloatType(self, ctx, o): pass
    def visitBooleanType(self, ctx, o): pass
    def visitStringType(self, ctx, o): pass
    def visitArrayType(self, ctx, o): pass
    def visitAutoType(self, ctx, o): pass
    def visitVoidType(self, ctx, o): pass

    def visitBinExpr(self, ctx, o):
        # This visit is create In case 2 integer
        lhs_reg, lhs_type = self.visit(ctx.left, o)
        rhs_reg, rhs_type = self.visit(ctx.right, o)
        o[1].resetRegs([lhs_reg, rhs_reg])
        res_reg = o[1].getSaveReg()
        if ctx.op in ['+']:
            self.emit.printout(self.emit.emitADD(IntegerType(), res_reg, lhs_reg, rhs_reg))
        if ctx.op in ['-']:
            self.emit.printout(self.emit.emitSUB(IntegerType(), res_reg, lhs_reg, rhs_reg))
        
        return res_reg, IntegerType()
    def visitUnExpr(self, ctx, o): pass
    def visitId(self, ctx, o): pass
    def visitArrayCell(self, ctx, o): pass    
    def visitIntegerLit(self, ctx, o):
        reg = o[1].getTempReg()
        o[1].updateValue(reg, 100)
        self.emit.printout(self.emit.emitLI(ctx.val, reg))
        return reg, IntegerType()
    def visitFloatLit(self, ctx, o): 
        # Must find the Float register to store the float literal
        pass
    def visitStringLit(self, ctx, o): pass
    def visitBooleanLit(self, ctx, o): pass
    def visitArrayLit(self, ctx, o): pass
    def visitFuncCall(self, ctx, o):
        if (ctx.name == "putInt"):
            for arg in ctx.args:
                reg, typ = self.visit(arg, o)
                self.emit.printout("\n\t# Call putInt Function\n")
                self.emit.printout(self.emit.emitADD(IntegerType(), '4', reg, 'zero'))
                self.emit.printout(self.emit.emitLI(1,"2"))
                self.emit.printout(self.emit.emitSYS())
                self.emit.printout("\n")

    def visitAssignStmt(self, ctx, o):
        # The visitor of ID should return the reg that hold the value
        var_name = ctx.lhs.name
        # Visit the expression
        reg = self.visit(ctx.rhs, o)
        self.emit.printout(self.emit.emitSW(reg,var_name))
    def visitCallStmt(self, ctx, o):
        self.visitFuncCall(ctx, o)
    def visitBlockStmt(self, ctx, o):
        for decl in ctx.body:
            self.visit(decl, o)
    def visitIfStmt(self, ctx, o): pass
    def visitForStmt(self, ctx, o): pass
    def visitWhileStmt(self, ctx, o): pass
    def visitDoWhileStmt(self, ctx, o): pass
    def visitBreakStmt(self, ctx, o): pass
    def visitContinueStmt(self, ctx, o): pass
    def visitReturnStmt(self, ctx, o): pass

    def visitFuncDecl(self, ctx, o):
        if ctx.name == "main":
            # Set the global function in MIPS
            self.emit.printout(self.emit.emitGLOBAL("main"))
        self.emit.printout(self.emit.emitFUNC(ctx.name))

        # Variable need to be add later
        # ctx.params: Chua lam
        # inherit: Chua lam
        # type: Chua lam
        self.visit(ctx.body, o)

        if ctx.name == "main":
            self.emit.printout(self.emit.emitLI(10,"2"))
            self.emit.printout(self.emit.emitSYS())
    def visitVarDecl(self, ctx, o):
        val = "" 
        self.emit.printoutData(self.emit.emitVAR(ctx.name, val))
        self.emit.printoutData(self.emit.emitDATA())

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        # o: the Reg class for manage address Descriptor and Register Descriptor        
        o = ({}, Reg())
        self.emit.printout(self.emit.emitTEXT())
        for decl in ast.decls:
            self.visit(decl, o)
        self.emit.emitEPILOG()
        



    


