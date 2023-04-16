# from Utils import *
class Reg():
    def __init__(self):
        # This field will hold information about register and it usage
        # then the Emitter can calculate and find good one for use
        self.registers_descriptor = {'2':("$v0", []), '3':("$v1", []), 
                          '4':("$a0", []), '5':("$a1", []), '6':("$a2", []), '7':("$a3", []),
                          '8':("$t0", []), '9':("$t1", []), '10':("$t2", []), '11':("$t3", []),
                          '12':("$t4", []), '13':("$t5", []), '14':("$t6", []), '15':("$t7", []),
                          '16':("$s0", []), '17':("$s1", []), '18':("$s2", []), '19':("$s3", []),
                          '20':("$s4", []), '21':("$s5", []), '22':("$s6", []), '23':("$s7", []),
                          '24':("$t8", []), '25':("$t9", []),
                        }
        self.address_descriptor = {}

    def resetRegs(self, regs):
        for reg in regs:
            self.registers_descriptor[reg][1].clear()

    def updateValue(self, reg, value):
        self.registers_descriptor[reg][1].append(value)

    def add_AD(self, var, value):
        if not var in self.address_descriptor:
            self.address_descriptor[var] = [value]
        else:
            self.address_descriptor[var].append(value)

    # params is the suitable paramter for the type 
    def update_AD_RD(self, params, type):
        # Load
        if type == 1:
            # params = (var, reg) 
            # var is the variable name
            # reg is the register's number
            self.registers_descriptor[params[1]] = [params[0]]
            if not params[0] in self.address_descriptor:   
                self.address_descriptor[params[0]] = [params[1]]
            else:
                self.address_descriptor[params[0]] += [params[1]]

        # Store
        if type == 2:
            # params = (var, reg)
            # var is the variable name
            # reg is the register's number
            if not params[0] in self.address_descriptor:   
                self.address_descriptor[params[0]] = [params[0]]
            elif not params[0] in self.address_descriptor[params[0]][1]:
                self.address_descriptor[params[0]] += [params[0]]

        # Operations
        if type == 3:
            # params = (var1, var2, var3, reg1, reg2, reg3)
            self.registers_descriptor[params[3]][1] = [params[0]]
            self.address_descriptor[params[0]] = [params[3]]
            for reg_num in self.registers_descriptor.keys():
                if params[3] in self.registers_descriptor[reg_num][1]:
                    self.registers_descriptor[reg_num][1].remove(params[3])

    def getReg_complex(self, var1=None, var2=None, var3=None):
        if (var1 is None and var2 is None and var3 is None):
            reg1 = None
            reg2 = None
            reg3 = None
            # Case 1
            for reg_num in self.registers_descriptor.keys():
                if var2 in self.registers_descriptor[reg_num][1]:
                    reg2 = self.registers_descriptor[reg_num][0]
                    # Update the AD and RD
                if var3 in self.registers_descriptor[reg_num][1]:
                    reg3 = self.registers_descriptor[reg_num][0]
                    # Update the AD and RD
            # Case 2
            for reg_num in self.registers_descriptor.keys():
                if len(self.registers_descriptor[reg_num][1]) == 0:
                    if reg2 is None:
                        reg2 = self.registers_descriptor[reg_num][0]
                        # Update the AD and RD
                    if reg3 is None:
                        reg3 = self.registers_descriptor[reg_num][0]
                        # Update the AD and RD

            # Case 3
            r_score = {}
            for reg_num in self.registers_descriptor.keys():
                for v in self.registers_descriptor[reg_num][1]:
                    # Situation a
                    if len(self.address_descriptor[v]) > 1:
                        if not reg_num in r_score:
                            r_score[reg_num] = 1
                        else:
                            r_score[reg_num] += 1
                    # Situation b
                    if v == var1 and v != var2 and v != var3:
                        if not reg_num in r_score:
                            r_score[reg_num] = 0
                    # Situation c: We need to know the scope of the variable v
                    # to check that do we need it in the future

                    # Situation d: Then we need to generate the store instruction ST v, R to
                    # to place a copy of v in its own memory location (SPILL)

                    
            r_score = sorted(r_score.items(), key=lambda x:x[1])
            if reg2 is None:
                reg = r_score.keys()[0]
                reg2 = self.registers_descriptor[reg][0]
                # Update AD and RD
                r_score.pop(reg)
            if reg3 is None:
                reg = r_score.keys()[0]
                reg3 = self.registers_descriptor[reg][0]
                # Update AD and RD
                r_score.pop(reg)

            # The code for finding var1:
            # var2 and var3 is found when the code come here
            
            # If var1 is var2 or var3:
            if var1 == var2:
                reg1 = reg2
            elif var1 == var3:
                reg1 = reg3
            else:
                for reg_num in self.registers_descriptor.keys():
                    if var1 in self.registers_descriptor[reg_num][1]:
                        reg1 = self.registers_descriptor[reg_num][0]
                        # Update the AD and RD
                if reg1 is None:
                    reg = r_score.keys()[0]
                    reg1 = self.registers_descriptor[reg][0]
                    # Update AD and RD
                    r_score.pop(reg)

            # if var2 or var3 is not used later -> Use them for var1
            ## Add code here

            return reg1, reg2, reg3

    def getReg(self):
        reg = None
        for reg_num in self.registers_descriptor.keys():
            if len(self.registers_descriptor[reg_num][1]) == 0:
                if reg is None:
                    reg = reg_num
                    break
        return reg

    def getTempReg(self):
        reg = None
        temp_reg = ['8','9','10','11','24','25']
        for reg_num in temp_reg:
            if len(self.registers_descriptor[reg_num][1]) == 0:
                if reg is None:
                    reg = reg_num
                    break
        return reg
    
    def getFuncResReg(self):
        reg = None
        func_res_reg = ['2','3']
        for reg_num in func_res_reg:
            if len(self.registers_descriptor[reg_num][1]) == 0:
                if reg is None:
                    reg = reg_num
                    break
        return reg
    
    def getArgReg(self):
        reg = None
        arg_reg = ['4','5','6','7']
        for reg_num in arg_reg:
            if len(self.registers_descriptor[reg_num][1]) == 0:
                if reg is None:
                    reg = reg_num
                    break
        return reg

    def getSaveReg(self):
        reg = None
        save_reg = ['16','17','18','19','20','21','22','23']
        for reg_num in save_reg:
            if len(self.registers_descriptor[reg_num][1]) == 0:
                if reg is None:
                    reg = reg_num
                    break
        return reg