'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntegerType()), CName(self.libName)),
                    Symbol("putInt", MType([IntegerType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntegerType()], VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        # SubBody(frame, sym)

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        # SubBody is that the body of the program
        # None is the frame of the program: In the initial it is None because the 
        # the program didn't have any frame
        # self.env is the enviroment of the program to store name of the func or var
        e = SubBody(None, self.env)

        # visit all decls in the program
        # During the visit time, put the enviroment e 
        # so that it can store the environment of the program
        # Also in this time, what declare in the program will be
        # visited and write on the MT22.j
        for x in ast.decls:
            e = self.visit(x, e)

        # After it visit all the declare in the program then create the environment of the program
        # it will genrate the init method of the program class (The MT22Class)
        # generate default constructor
        # genMETHOD(self, consdecl, o, frame)
        self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt( list())), c, Frame("<init>", VoidType))
        # for str in self.emit.buff:
        #     print(str)
        self.emit.emitEPILOG()

        # After done visit the program the visit pattern return the c as the 
        # environment after applying some changes
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any -> Symbols
        #frame: Frame

        # True if the return_type is None mean that the init method
        isInit = consdecl.return_type is None

        # True if this program's name is 'main' and have no param and return type is VoidType
        isMain = consdecl.name == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType
        
        # Set the returnType to VoidType if Init else return other's type
        returnType = VoidType() if isInit else consdecl.return_type
        
        # Set the methodName to <init> if init else other's name
        methodName = "<init>" if isInit else consdecl.name
        
        # Set the input params of the program to Array of String if this is Main
        # else just an empty list
        intype = [ArrayPointerType(StringType())] if isMain else list()
        
        # The method type is the combination of the params's type and the return type
        mtype = MType(intype, returnType)

        # emitMETHOD(self, lexem, mtype, isStatic, frame)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        # Enter the body of the method -> Create from start label to end lable
        frame.enterScope(True)

        # Set the global environment equal to o
        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # Get the body of the method
        body = consdecl.body

        # Print the label to buffer for latter write to the file
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements (For init)
        if isInit:
            # emitREADVAR(self, name, inType, index, frame)
            # Read the 'this' variable from the memory for using invokespecial
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            
            # Using invokespecial to call the <init> method of the MT22Class
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # SubBody(frame, sym)
        # Just visit all the body of the funcdecl or vardecl
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))

        # After visit all the declarations of the method then -> print the end_label
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        # if the return_type is void then print return for voidtype
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        # Put some end method line to the buffer
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any -> Sub(frame, environment)
        # SubBody(frame, sym)

        # Get the subbody by assigning o
        subctxt = o

        # Create a frame for this funcdecl 
        # Frame(self, name, return_type)
        frame = Frame(ast.name, ast.return_type)

        # Gen method by the genMETHOD function
        # subctxt.sym is just the environment of this frame
        self.genMETHOD(ast, subctxt.sym, frame)

        # Return the subbody for later assign
        # And add the method to the symbol list of the program
        # Symbol(method_name, Method_type, class_name)
        # Addition with the environment symbol
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.return_type), CName(self.className))] + subctxt.sym)

    def visitFuncCall(self, ast, o):
        #ast: FuncCall
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        # Lookup for the symbol that is the name of the funcall
        sym = self.lookup(ast.name, nenv, lambda x: x.name)

        # Get the value of the sym's value: the class name
        cname = sym.value.value
    
        # The type of the class
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.args:
            # Visit the arg of of the method
            # Access(frame, sym, isLeft, isFirst)
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))

        # Save the push command to the buffer
        self.emit.printout(in_[0])

        # Save the Invokestatic to the buffer
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame))

    def visitIntegerLit(self, ast, o):
        #ast: IntLiteral
        #o: Any: Access(frame, sym, isLeft, isFirst)

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.val, frame), IntegerType()

    def visitFloatLit(self, ast, o):
        #ast: FloatLiteral
        #o: Any: Access(frame, sym, isLeft, isFirst)

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(ast.val, frame), FloatType

    def visitBinExpr(self, ast: BinExpr, o):
        # ast: BinExpr
        # o: any: Access(frame, sym, isLeft, isFirst)

        ctxt = o
        frame = ctxt.frame

        str1, typ1 = self.visit(ast.left, o)
        str2, typ2 = self.visit(ast.right, o)

        self.emit.printout(str1)
        self.emit.printout(str2)

        return self.emit.emitADDOP(ast.op, IntegerType(), frame), IntegerType()
        
               


    
