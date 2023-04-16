from MachineCode import MIPSCode

jvm = MIPSCode()
print(jvm.emitADD('$s0', '$t0', '$t1'))