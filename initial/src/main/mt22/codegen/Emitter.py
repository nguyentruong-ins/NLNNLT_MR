# from Utils import *
# from StaticCheck import *
# from StaticError import *
# import CodeGenerator as cgen
from MachineCode import MIPSCode
from CodeGenError import *
from Reg import *
from AST import *

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = MIPSCode()
    
    def emitVAR(self, name, val):
        return name +":" + self.jvm.emitWORD(val) 

    def emitFUNC(self, name):
        return self.jvm.emitLABEL(name)

    def emitSYS(self):
        return self.jvm.emitSYSCALL()

    def emitTEXT(self):
        return self.jvm.emitTEXT()  
    
    def emitDATA(self):
        return self.jvm.emitDATA()

    def emitLI(self, in_, reg):
        if type(in_) is int:
            return self.jvm.emitLI('$' + reg, in_)
        else:
            raise IllegalOperandException(str(in_))
        
    def emitADD(self, typ, reg1, reg2, reg3):
        if type(typ) is IntegerType:
            return self.jvm.emitADD('$' + reg1, '$' + reg2,'$' + reg3)

    def emitSUB(self, typ, reg1, reg2, reg3):
        if type(typ) is IntegerType:
            return self.jvm.emitSUB('$' + reg1, '$' + reg2,'$' + reg3)

    def emitSW(self, reg, label):
        return self.jvm.emitSWLabel('$' + reg, label)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    def emitGLOBAL(self, name):
        return self.jvm.emitGLOBAL(name)

    def printout(self, in_):
        self.buff.append(in_)

    def printoutData(self, in_):
        self.buff.insert(0, in_)
    
    def clearBuff(self):
        self.buff.clear()
