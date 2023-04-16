from abc import ABC, abstractmethod, ABCMeta

class MachineCode(ABC):
    # Arithmetic Instructions
    @abstractmethod
    def emitADD(self, store, res1, res2):
        pass
    @abstractmethod
    def emitSUB(self, store, res1, res2):
        pass
    @abstractmethod
    def emitADDI(self, store, res, num):pass
    @abstractmethod
    def emitADDU(self, store, res1, res2):pass
    @abstractmethod
    def emitSUBU(self, store, res1, res2):pass
    @abstractmethod
    def emitADDIU(self, store, res, num):pass
    @abstractmethod
    def emitSMUL(self, store, res1, res2):pass
    @abstractmethod
    def emitLMUL(self, res1, res2):pass
    @abstractmethod
    def emitDIV(self, res1, res2):pass

    # Arithmetic Instruction for FP
    # @abstractmethod
    # def emitADDS(self, store, res1, res2):pass
    # @abstractmethod
    # def emitSUBS(self, store, res1, res2):pass
    # @abstractmethod
    # def emitMULS(self, store, res1, res2):pass
    # @abstractmethod
    # def emitDIVS(self, store, res1, res2):pass
    # @abstractmethod
    # def emitABSS(self, store, res):pass
    # @abstractmethod
    # def emitNEGS(self, store, res):pass

    # Logic Instructions
    @abstractmethod
    def emitAND(self, store, res1, res2):pass
    @abstractmethod
    def emitOR(self, store, res1, res2):pass
    @abstractmethod
    def emitANDI(self, store, res, num):pass
    @abstractmethod
    def emitORI(self, store, res, num):pass
    @abstractmethod
    def emitSHIFTL(self, store, res, num):pass
    @abstractmethod
    def emitSHIFTR(self, store, res, num):pass
    @abstractmethod
    def emitADDI(self, store, res, num):pass

    # Data Transfer
    @abstractmethod
    def emitLW(self, store, index, res):pass
    @abstractmethod
    def emitSW(self, store, index, res):pass
    @abstractmethod
    def emitLUI(self, store, num):pass
    @abstractmethod
    def emitLA(self, store, label):pass
    @abstractmethod
    def emitLI(self, store, num):pass
    @abstractmethod
    def emitMFHI(self, store):pass
    @abstractmethod
    def emitMFLO(self, store):pass
    @abstractmethod
    def emitMOVE(self, store, res):pass
    # @abstractmethod
    # def emitLS(self, store, index, res):pass
    # @abstractmethod
    # def emitSS(self, store, index, res):pass
    # @abstractmethod
    # def emitMOVS(self, store, res):pass
    # @abstractmethod
    # def emitMFC1(self, store, res):pass
    # @abstractmethod
    # def emitMTC1(self, store, res):pass
    # @abstractmethod
    # def emitCVTWS(self, store, res):pass
    # @abstractmethod
    # def emitCVTSW(self, store, res):pass

    # Conditional Branch
    @abstractmethod
    def emitBEQ(self, store, res, num):pass
    @abstractmethod
    def emitBNE(self, store, res, num):pass
    @abstractmethod
    def emitBGT(self, store, res, num):pass
    @abstractmethod
    def emitBGE(self, store, res, num):pass
    @abstractmethod
    def emitBLT(self, store, res, num):pass
    @abstractmethod
    def emitBLE(self, store, res, num):pass

    # Comparison
    @abstractmethod
    def emitSLT(self, store, res1, res2):pass
    @abstractmethod
    def emitSLTI(self, store, res, num):pass

    # Unconditional Jump
    @abstractmethod
    def emitJUMP(self, address):pass
    @abstractmethod
    def emitJUMPR(self, res):pass
    @abstractmethod
    def emitJUMPAL(self, address):pass

    # System Calls
    @abstractmethod
    def emitSYSCALL(self):pass

    # Assembler Directives
    @abstractmethod
    def emitWORD(self, value):pass
    @abstractmethod
    def emitHALF(self, value):pass
    @abstractmethod
    def emitBYTE(self, value):pass
    @abstractmethod
    def emitASCII(self, str):pass
    @abstractmethod
    def emitASCIIZ(self, str):pass
    @abstractmethod
    def emitSPACE(self, value):pass
    @abstractmethod
    def emitALIGN(self, value):pass

    @abstractmethod
    def emitGLOBAL(self, name):pass
    @abstractmethod
    def emitTEXT(self):pass
    @abstractmethod
    def emitLABEL(self, label):pass
    @abstractmethod
    def emitDATA(self):pass


class MIPSCode(MachineCode):
    END = '\n'
    INDENT = '\t'

    # Arithmetics
    def emitADD(self, store, res1, res2):
        return MIPSCode.INDENT + 'add ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitSUB(self, store, res1, res2):
        return MIPSCode.INDENT + 'sub ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitADDI(self, store, res, num):
        return MIPSCode.INDENT + 'addi ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitADDU(self, store, res1, res2):
        return MIPSCode.INDENT + 'addu ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitSUBU(self, store, res1, res2):
        return MIPSCode.INDENT + 'subu ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitADDIU(self, store, res, num):
        return MIPSCode.INDENT + 'addiu ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitSMUL(self, store, res1, res2):
        return MIPSCode.INDENT + 'mul ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitLMUL(self, res1, res2):
        return MIPSCode.INDENT + 'mult ' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitDIV(self, res1, res2):
        return MIPSCode.INDENT + 'div ' + str(res1) + ',' + str(res2) + MIPSCode.END
    
    # Logical
    def emitAND(self, store, res1, res2):
        return MIPSCode.INDENT + 'and ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitOR(self, store, res1, res2):
        return MIPSCode.INDENT + 'or ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitANDI(self, store, res, num):
        return MIPSCode.INDENT + 'andi ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitORI(self, store, res, num):
        return MIPSCode.INDENT + 'ori ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitSHIFTL(self, store, res, num):
        return MIPSCode.INDENT + 'sll ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitSHIFTR(self, store, res, num):
        return MIPSCode.INDENT + 'srl ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    
    # Data transfer
    def emitLW(self, store, index, res):
        return MIPSCode.INDENT + 'lw ' + str(store) + ',' + str(index) + '(' + str(res) + ')' + MIPSCode.END
    def emitSW(self, store, index, res):
        return MIPSCode.INDENT + 'sw ' + str(store) + ',' + str(index) + '(' + str(res) + ')' + MIPSCode.END
    def emitSWLabel(self, store, label):
        return MIPSCode.INDENT + 'sw ' + str(store) + ',' + str(label) + MIPSCode.END
    def emitLUI(self, store, num):
        return MIPSCode.INDENT + 'lui ' + str(store) + ',' + str(num) + MIPSCode.END
    def emitLA(self, store, label):
        return MIPSCode.INDENT + 'la ' + str(store) + ',' + str(label) + MIPSCode.END
    def emitLI(self, store, num):
        return MIPSCode.INDENT + 'li ' + str(store) + ',' + str(num) + MIPSCode.END
    def emitMFHI(self, store):
        return MIPSCode.INDENT + 'mfhi ' + str(store) + MIPSCode.END
    def emitMFLO(self, store):
        return MIPSCode.INDENT + 'mflo ' + str(store) + MIPSCode.END
    def emitMOVE(self, store, res):
        return MIPSCode.INDENT + 'move ' + str(store) + ',' + str(res) + MIPSCode.END
    
    # Conditional Branch
    def emitBEQ(self, store, res, num):
        return MIPSCode.INDENT + 'beq ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitBNE(self, store, res, num):
        return MIPSCode.INDENT + 'bne ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitBGT(self, store, res, num):
        return MIPSCode.INDENT + 'bgt ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitBGE(self, store, res, num):
        return MIPSCode.INDENT + 'bge ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitBLT(self, store, res, num):
        return MIPSCode.INDENT + 'blt ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    def emitBLE(self, store, res, num):
        return MIPSCode.INDENT + 'ble ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    
    # Comparison
    def emitSLT(self, store, res1, res2):
        return MIPSCode.INDENT + 'slt ' + str(store) + ',' + str(res1) + ',' + str(res2) + MIPSCode.END
    def emitSLTI(self, store, res, num):
        return MIPSCode.INDENT + 'slti ' + str(store) + ',' + str(res) + ',' + str(num) + MIPSCode.END
    
    # Unconditional Jump
    def emitJUMP(self, address):
        return MIPSCode.INDENT + 'j ' + str(address) + MIPSCode.END
    def emitJUMPR(self, res):
        return MIPSCode.INDENT + 'jr ' + str(res) + MIPSCode.END
    def emitJUMPAL(self, address):
        return MIPSCode.INDENT + 'jal ' + str(address) + MIPSCode.END
    
    # System Calls
    def emitSYSCALL(self):
        return MIPSCode.INDENT + 'syscall' + MIPSCode.END

    # Assembler Directives
    def emitWORD(self, value):
        return MIPSCode.INDENT + '.word ' + str(value) + MIPSCode.END
    def emitHALF(self, value):
        return MIPSCode.INDENT + '.half ' + str(value) + MIPSCode.END
    def emitBYTE(self, value):
        return MIPSCode.INDENT + '.byte ' + str(value) + MIPSCode.END
    def emitASCII(self, str):
        return MIPSCode.INDENT + '.ascii ' + str + MIPSCode.END
    def emitASCIIZ(self, str):
        return MIPSCode.INDENT + '.asciiz ' + str + MIPSCode.END
    def emitSPACE(self, value):
        return MIPSCode.INDENT + '.ascii ' + str(value) + MIPSCode.END
    def emitALIGN(self, value):
        return MIPSCode.INDENT + '.align ' + str(value) + MIPSCode.END
    
    ####
    def emitGLOBAL(self, name):
        return ".globl " + name + MIPSCode.END
    def emitTEXT(self):
        return ".text" + MIPSCode.END
    def emitLABEL(self, label):
        return label + ":" + MIPSCode.END 
    def emitDATA(self):
        return ".data" + MIPSCode.END