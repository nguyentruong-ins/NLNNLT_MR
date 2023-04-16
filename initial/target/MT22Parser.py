# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5$\n\5\3\6\3\6\3\6")
        buf.write("\5\6)\n\6\3\7\3\7\3\7\5\7.\n\7\3\7\3\7\3\7\2\2\b\2\4\6")
        buf.write("\b\n\f\2\3\3\2\5\6\2\60\2\16\3\2\2\2\4\31\3\2\2\2\6\33")
        buf.write("\3\2\2\2\b#\3\2\2\2\n(\3\2\2\2\f*\3\2\2\2\16\17\5\4\3")
        buf.write("\2\17\20\7\3\2\2\20\21\7\t\2\2\21\22\7\n\2\2\22\24\7\13")
        buf.write("\2\2\23\25\5\6\4\2\24\23\3\2\2\2\24\25\3\2\2\2\25\26\3")
        buf.write("\2\2\2\26\27\7\f\2\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32")
        buf.write("\t\2\2\2\32\5\3\2\2\2\33\34\5\f\7\2\34\35\7\r\2\2\35\7")
        buf.write("\3\2\2\2\36\37\5\n\6\2\37 \7\4\2\2 !\5\n\6\2!$\3\2\2\2")
        buf.write("\"$\5\n\6\2#\36\3\2\2\2#\"\3\2\2\2$\t\3\2\2\2%)\5\f\7")
        buf.write("\2&)\7\7\2\2\')\7\b\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2")
        buf.write(")\13\3\2\2\2*+\7\7\2\2+-\7\t\2\2,.\5\b\5\2-,\3\2\2\2-")
        buf.write(".\3\2\2\2./\3\2\2\2/\60\7\n\2\2\60\r\3\2\2\2\6\24#(-")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'+'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PLUS", "INTTYPE", "VOIDTYPE", 
                      "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_exp1 = 4
    RULE_funcall = 5

    ruleNames =  [ "program", "mptype", "body", "exp", "exp1", "funcall" ]

    EOF = Token.EOF
    T__0=1
    PLUS=2
    INTTYPE=3
    VOIDTYPE=4
    ID=5
    INTLIT=6
    LB=7
    RB=8
    LP=9
    RP=10
    SEMI=11
    WS=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MT22Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def LP(self):
            return self.getToken(MT22Parser.LP, 0)

        def RP(self):
            return self.getToken(MT22Parser.RP, 0)

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.mptype()
            self.state = 13
            self.match(MT22Parser.T__0)
            self.state = 14
            self.match(MT22Parser.LB)
            self.state = 15
            self.match(MT22Parser.RB)
            self.state = 16
            self.match(MT22Parser.LP)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ID:
                self.state = 17
                self.body()


            self.state = 20
            self.match(MT22Parser.RP)
            self.state = 21
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MT22Parser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = MT22Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==MT22Parser.INTTYPE or _la==MT22Parser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.funcall()
            self.state = 26
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Exp1Context,i)


        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MT22Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.exp1()
                self.state = 29
                self.match(MT22Parser.PLUS)
                self.state = 30
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MT22Parser.FuncallContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = MT22Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp1)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.funcall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(MT22Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MT22Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MT22Parser.ID)
            self.state = 41
            self.match(MT22Parser.LB)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ID or _la==MT22Parser.INTLIT:
                self.state = 42
                self.exp()


            self.state = 45
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





