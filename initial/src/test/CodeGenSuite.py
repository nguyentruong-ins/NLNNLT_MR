import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int1(self):
        """Simple program: int main() {} """
        input = """main: function void(){putInt(1 - 2);}"""
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,500))
        
    # def test_int2(self):
    #     """ """
    #     input = """main: function void(){putInt(100 + 1000);}"""
    #     expect = "1100"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_int3(self):
    #     """ """
    #     input = """main: function void(){putInt(50 + 11);}"""
    #     expect = "61"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
        
    # def test_int4(self):
    #     """ """
    #     input = """main: function void(){putInt(503 + 1);}"""
    #     expect = "504"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
        
    # def test_int5(self):
    #     """ """
    #     input = """main: function void(){putInt(20 + 1);}"""
    #     expect = "21"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
        