import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """int main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Statement: FuncCall(putIntLn, [])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: FuncCall(getInt, [IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl("main",IntegerType(),[],None,BlockStmt([
            FuncCall("foo",[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl("main",IntegerType(),[],None,BlockStmt([
                    FuncCall("putIntLn",[
                        FuncCall("getInt",[IntegerLit(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: FuncCall(getInt, [IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl("main",IntegerType(),[],None,BlockStmt([
                    FuncCall("putIntLn",[])]))])
        expect = "Type Mismatch In Statement: FuncCall(putIntLn, [])"
        self.assertTrue(TestChecker.test(input,expect,405))
    