# Generated from e:\STUDY\HK222\PPL_MR\Phase 1\initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u0192\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3h\n\3\3")
        buf.write("\4\3\4\5\4l\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7|\n\7\3\b\3\b\5\b\u0080\n\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u0090\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u009b\n\13\3\f\5\f\u009e\n\f\3\f\5\f\u00a1\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ad\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b8")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00c3\n\17\3\20\3\20\5\20\u00c7\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u00cf\n\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00d6\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00dd\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e5\n\24\f\24")
        buf.write("\16\24\u00e8\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00f0\n\25\f\25\16\25\u00f3\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u00fb\n\26\f\26\16\26\u00fe\13\26\3\27")
        buf.write("\3\27\3\27\5\27\u0103\n\27\3\30\3\30\3\30\5\30\u0108\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0112")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\5\34\u011e\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0135\n\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\5\"\u013e\n\"\3#\3#\3#\3#\3#\3#\3#\5#\u0147\n#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\5*\u016d\n*\3*\3*\3+\3+\3+\3+\3+\5+\u0176\n+\3,\3")
        buf.write(",\3,\5,\u017b\n,\3,\3,\3,\3-\3-\3-\3-\3.\3.\5.\u0186\n")
        buf.write(".\3/\3/\3/\3/\5/\u018c\n/\3\60\3\60\5\60\u0190\n\60\3")
        buf.write("\60\2\5&(*\61\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2\4\6\2\b\b")
        buf.write("\13\13\17\17\21\21\3\2\36\37\2\u0199\2`\3\2\2\2\4g\3\2")
        buf.write("\2\2\6k\3\2\2\2\bm\3\2\2\2\nt\3\2\2\2\f{\3\2\2\2\16\177")
        buf.write("\3\2\2\2\20\u008f\3\2\2\2\22\u0091\3\2\2\2\24\u009a\3")
        buf.write("\2\2\2\26\u009d\3\2\2\2\30\u00ac\3\2\2\2\32\u00ae\3\2")
        buf.write("\2\2\34\u00c2\3\2\2\2\36\u00c6\3\2\2\2 \u00ce\3\2\2\2")
        buf.write("\"\u00d5\3\2\2\2$\u00dc\3\2\2\2&\u00de\3\2\2\2(\u00e9")
        buf.write("\3\2\2\2*\u00f4\3\2\2\2,\u0102\3\2\2\2.\u0107\3\2\2\2")
        buf.write("\60\u0111\3\2\2\2\62\u0113\3\2\2\2\64\u0117\3\2\2\2\66")
        buf.write("\u011d\3\2\2\28\u011f\3\2\2\2:\u0124\3\2\2\2<\u0134\3")
        buf.write("\2\2\2>\u0136\3\2\2\2@\u0138\3\2\2\2B\u013d\3\2\2\2D\u013f")
        buf.write("\3\2\2\2F\u0148\3\2\2\2H\u0152\3\2\2\2J\u0156\3\2\2\2")
        buf.write("L\u015c\3\2\2\2N\u0164\3\2\2\2P\u0167\3\2\2\2R\u016a\3")
        buf.write("\2\2\2T\u0175\3\2\2\2V\u0177\3\2\2\2X\u017f\3\2\2\2Z\u0185")
        buf.write("\3\2\2\2\\\u018b\3\2\2\2^\u018f\3\2\2\2`a\5\4\3\2ab\7")
        buf.write("\2\2\3b\3\3\2\2\2cd\5\6\4\2de\5\4\3\2eh\3\2\2\2fh\5\6")
        buf.write("\4\2gc\3\2\2\2gf\3\2\2\2h\5\3\2\2\2il\5\16\b\2jl\5\32")
        buf.write("\16\2ki\3\2\2\2kj\3\2\2\2l\7\3\2\2\2mn\7\30\2\2no\7*\2")
        buf.write("\2op\5\f\7\2pq\7+\2\2qr\7\26\2\2rs\5\n\6\2s\t\3\2\2\2")
        buf.write("tu\t\2\2\2u\13\3\2\2\2vw\7\63\2\2wx\7/\2\2xy\3\2\2\2y")
        buf.write("|\5\f\7\2z|\7\63\2\2{v\3\2\2\2{z\3\2\2\2|\r\3\2\2\2}\u0080")
        buf.write("\5\20\t\2~\u0080\5\22\n\2\177}\3\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\7\60\2\2\u0082\17\3\2\2\2\u0083")
        buf.write("\u0084\7\67\2\2\u0084\u0085\7/\2\2\u0085\u0086\5\20\t")
        buf.write("\2\u0086\u0087\7/\2\2\u0087\u0088\5\"\22\2\u0088\u0090")
        buf.write("\3\2\2\2\u0089\u008a\7\67\2\2\u008a\u008b\7\61\2\2\u008b")
        buf.write("\u008c\5\30\r\2\u008c\u008d\7\62\2\2\u008d\u008e\5\"\22")
        buf.write("\2\u008e\u0090\3\2\2\2\u008f\u0083\3\2\2\2\u008f\u0089")
        buf.write("\3\2\2\2\u0090\21\3\2\2\2\u0091\u0092\5\24\13\2\u0092")
        buf.write("\u0093\7\61\2\2\u0093\u0094\5\30\r\2\u0094\23\3\2\2\2")
        buf.write("\u0095\u0096\7\67\2\2\u0096\u0097\7/\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\u009b\5\24\13\2\u0099\u009b\7\67\2\2\u009a")
        buf.write("\u0095\3\2\2\2\u009a\u0099\3\2\2\2\u009b\25\3\2\2\2\u009c")
        buf.write("\u009e\7\27\2\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2")
        buf.write("\2\u009e\u00a0\3\2\2\2\u009f\u00a1\7\24\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\7\67\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\5\30")
        buf.write("\r\2\u00a5\27\3\2\2\2\u00a6\u00ad\7\b\2\2\u00a7\u00ad")
        buf.write("\7\17\2\2\u00a8\u00ad\7\13\2\2\u00a9\u00ad\7\21\2\2\u00aa")
        buf.write("\u00ad\5\b\5\2\u00ab\u00ad\7\6\2\2\u00ac\u00a6\3\2\2\2")
        buf.write("\u00ac\u00a7\3\2\2\2\u00ac\u00a8\3\2\2\2\u00ac\u00a9\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\31")
        buf.write("\3\2\2\2\u00ae\u00af\7\67\2\2\u00af\u00b0\7\61\2\2\u00b0")
        buf.write("\u00b1\7\r\2\2\u00b1\u00b2\5\34\17\2\u00b2\u00b3\7(\2")
        buf.write("\2\u00b3\u00b4\5\36\20\2\u00b4\u00b7\7)\2\2\u00b5\u00b6")
        buf.write("\7\27\2\2\u00b6\u00b8\7\67\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\5X-\2\u00ba")
        buf.write("\33\3\2\2\2\u00bb\u00c3\7\b\2\2\u00bc\u00c3\7\17\2\2\u00bd")
        buf.write("\u00c3\7\13\2\2\u00be\u00c3\7\21\2\2\u00bf\u00c3\7\23")
        buf.write("\2\2\u00c0\u00c3\5\b\5\2\u00c1\u00c3\7\6\2\2\u00c2\u00bb")
        buf.write("\3\2\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c1\3\2\2\2\u00c3\35\3\2\2\2\u00c4\u00c7\5 \21")
        buf.write("\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\37\3\2\2\2\u00c8\u00c9\5\26\f\2\u00c9\u00ca")
        buf.write("\7/\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\5 \21\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cf\5\26\f\2\u00ce\u00c8\3\2\2")
        buf.write("\2\u00ce\u00cd\3\2\2\2\u00cf!\3\2\2\2\u00d0\u00d1\5$\23")
        buf.write("\2\u00d1\u00d2\7\'\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d6")
        buf.write("\3\2\2\2\u00d4\u00d6\5$\23\2\u00d5\u00d0\3\2\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6#\3\2\2\2\u00d7\u00d8\5&\24\2\u00d8")
        buf.write("\u00d9\7\3\2\2\u00d9\u00da\5&\24\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00dd\5&\24\2\u00dc\u00d7\3\2\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dd%\3\2\2\2\u00de\u00df\b\24\1\2\u00df\u00e0")
        buf.write("\5(\25\2\u00e0\u00e6\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2")
        buf.write("\u00e3\7\4\2\2\u00e3\u00e5\5(\25\2\u00e4\u00e1\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\'\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\b\25\1\2\u00ea\u00eb\5*\26\2\u00eb\u00f1\3\2\2\2\u00ec")
        buf.write("\u00ed\f\4\2\2\u00ed\u00ee\t\3\2\2\u00ee\u00f0\5*\26\2")
        buf.write("\u00ef\u00ec\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f4\u00f5\b\26\1\2\u00f5\u00f6\5,\27\2\u00f6")
        buf.write("\u00fc\3\2\2\2\u00f7\u00f8\f\4\2\2\u00f8\u00f9\7\5\2\2")
        buf.write("\u00f9\u00fb\5,\27\2\u00fa\u00f7\3\2\2\2\u00fb\u00fe\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd+")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\7\31\2\2\u0100")
        buf.write("\u0103\5,\27\2\u0101\u0103\5.\30\2\u0102\u00ff\3\2\2\2")
        buf.write("\u0102\u0101\3\2\2\2\u0103-\3\2\2\2\u0104\u0105\7\37\2")
        buf.write("\2\u0105\u0108\5.\30\2\u0106\u0108\5\60\31\2\u0107\u0104")
        buf.write("\3\2\2\2\u0107\u0106\3\2\2\2\u0108/\3\2\2\2\u0109\u0112")
        buf.write("\7\63\2\2\u010a\u0112\7\64\2\2\u010b\u0112\7\65\2\2\u010c")
        buf.write("\u0112\7\66\2\2\u010d\u0112\5\64\33\2\u010e\u0112\5B\"")
        buf.write("\2\u010f\u0112\5:\36\2\u0110\u0112\5\62\32\2\u0111\u0109")
        buf.write("\3\2\2\2\u0111\u010a\3\2\2\2\u0111\u010b\3\2\2\2\u0111")
        buf.write("\u010c\3\2\2\2\u0111\u010d\3\2\2\2\u0111\u010e\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112\61\3\2")
        buf.write("\2\2\u0113\u0114\7(\2\2\u0114\u0115\5\"\22\2\u0115\u0116")
        buf.write("\7)\2\2\u0116\63\3\2\2\2\u0117\u0118\7,\2\2\u0118\u0119")
        buf.write("\5\66\34\2\u0119\u011a\7-\2\2\u011a\65\3\2\2\2\u011b\u011e")
        buf.write("\5T+\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e\67\3\2\2\2\u011f\u0120\7\67\2\2\u0120\u0121")
        buf.write("\7*\2\2\u0121\u0122\5T+\2\u0122\u0123\7+\2\2\u01239\3")
        buf.write("\2\2\2\u0124\u0125\7\67\2\2\u0125\u0126\7(\2\2\u0126\u0127")
        buf.write("\5\66\34\2\u0127\u0128\7)\2\2\u0128;\3\2\2\2\u0129\u0135")
        buf.write("\5@!\2\u012a\u0135\5D#\2\u012b\u0135\5F$\2\u012c\u0135")
        buf.write("\5J&\2\u012d\u0135\5L\'\2\u012e\u0135\5V,\2\u012f\u0135")
        buf.write("\5X-\2\u0130\u0135\5R*\2\u0131\u0135\5N(\2\u0132\u0135")
        buf.write("\5P)\2\u0133\u0135\5> \2\u0134\u0129\3\2\2\2\u0134\u012a")
        buf.write("\3\2\2\2\u0134\u012b\3\2\2\2\u0134\u012c\3\2\2\2\u0134")
        buf.write("\u012d\3\2\2\2\u0134\u012e\3\2\2\2\u0134\u012f\3\2\2\2")
        buf.write("\u0134\u0130\3\2\2\2\u0134\u0131\3\2\2\2\u0134\u0132\3")
        buf.write("\2\2\2\u0134\u0133\3\2\2\2\u0135=\3\2\2\2\u0136\u0137")
        buf.write("\7\60\2\2\u0137?\3\2\2\2\u0138\u0139\5H%\2\u0139\u013a")
        buf.write("\7\60\2\2\u013aA\3\2\2\2\u013b\u013e\7\67\2\2\u013c\u013e")
        buf.write("\58\35\2\u013d\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("C\3\2\2\2\u013f\u0140\7\16\2\2\u0140\u0141\7(\2\2\u0141")
        buf.write("\u0142\5\"\22\2\u0142\u0143\7)\2\2\u0143\u0146\5<\37\2")
        buf.write("\u0144\u0145\7\n\2\2\u0145\u0147\5<\37\2\u0146\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147E\3\2\2\2\u0148\u0149")
        buf.write("\7\f\2\2\u0149\u014a\7(\2\2\u014a\u014b\5H%\2\u014b\u014c")
        buf.write("\7/\2\2\u014c\u014d\5\"\22\2\u014d\u014e\7/\2\2\u014e")
        buf.write("\u014f\5\"\22\2\u014f\u0150\7)\2\2\u0150\u0151\5<\37\2")
        buf.write("\u0151G\3\2\2\2\u0152\u0153\5B\"\2\u0153\u0154\7\62\2")
        buf.write("\2\u0154\u0155\5\"\22\2\u0155I\3\2\2\2\u0156\u0157\7\22")
        buf.write("\2\2\u0157\u0158\7(\2\2\u0158\u0159\5\"\22\2\u0159\u015a")
        buf.write("\7)\2\2\u015a\u015b\5<\37\2\u015bK\3\2\2\2\u015c\u015d")
        buf.write("\7\t\2\2\u015d\u015e\5X-\2\u015e\u015f\7\22\2\2\u015f")
        buf.write("\u0160\7(\2\2\u0160\u0161\5\"\22\2\u0161\u0162\7)\2\2")
        buf.write("\u0162\u0163\7\60\2\2\u0163M\3\2\2\2\u0164\u0165\7\7\2")
        buf.write("\2\u0165\u0166\7\60\2\2\u0166O\3\2\2\2\u0167\u0168\7\25")
        buf.write("\2\2\u0168\u0169\7\60\2\2\u0169Q\3\2\2\2\u016a\u016c\7")
        buf.write("\20\2\2\u016b\u016d\5\"\22\2\u016c\u016b\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7\60\2")
        buf.write("\2\u016fS\3\2\2\2\u0170\u0171\5\"\22\2\u0171\u0172\7/")
        buf.write("\2\2\u0172\u0173\5T+\2\u0173\u0176\3\2\2\2\u0174\u0176")
        buf.write("\5\"\22\2\u0175\u0170\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("U\3\2\2\2\u0177\u0178\7\67\2\2\u0178\u017a\7(\2\2\u0179")
        buf.write("\u017b\5T+\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c\u017d\7)\2\2\u017d\u017e\7\60\2\2")
        buf.write("\u017eW\3\2\2\2\u017f\u0180\7,\2\2\u0180\u0181\5Z.\2\u0181")
        buf.write("\u0182\7-\2\2\u0182Y\3\2\2\2\u0183\u0186\5\\/\2\u0184")
        buf.write("\u0186\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2")
        buf.write("\u0186[\3\2\2\2\u0187\u0188\5^\60\2\u0188\u0189\5\\/\2")
        buf.write("\u0189\u018c\3\2\2\2\u018a\u018c\5^\60\2\u018b\u0187\3")
        buf.write("\2\2\2\u018b\u018a\3\2\2\2\u018c]\3\2\2\2\u018d\u0190")
        buf.write("\5<\37\2\u018e\u0190\5\16\b\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190_\3\2\2\2!gk{\177\u008f\u009a\u009d")
        buf.write("\u00a0\u00ac\u00b7\u00c2\u00c6\u00ce\u00d5\u00dc\u00e6")
        buf.write("\u00f1\u00fc\u0102\u0107\u0111\u011d\u0134\u013d\u0146")
        buf.write("\u016c\u0175\u017a\u0185\u018b\u018f")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'float'", "'for'", "'function'", "'if'", "'integer'", 
                     "'return'", "'string'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", 
                     "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "Binary1", "Binary2", "Binary4", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "NEG", "AND", "OR", "EQUAL", "DIF", "PLUS", "SUB", 
                      "MUL", "DIV", "MOD", "LT", "LTE", "GT", "GTE", "CONC", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                      "SEMI", "COLON", "ASSIGN", "INTTYPE", "FLOATTYPE", 
                      "BOOLTYPE", "STRINGTYPE", "IDENTIFIER", "CPPCMT", 
                      "CCMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_arrdcl = 3
    RULE_atom = 4
    RULE_intlist = 5
    RULE_variabledcl = 6
    RULE_vardcl_full = 7
    RULE_vardcl_short = 8
    RULE_idlist = 9
    RULE_paradcl = 10
    RULE_paratype = 11
    RULE_funcdcl = 12
    RULE_functype = 13
    RULE_paralist = 14
    RULE_paraprime = 15
    RULE_expr = 16
    RULE_expr1 = 17
    RULE_expr2 = 18
    RULE_expr3 = 19
    RULE_expr4 = 20
    RULE_expr5 = 21
    RULE_expr6 = 22
    RULE_expr7 = 23
    RULE_sub_expr = 24
    RULE_arraylit = 25
    RULE_nullable_explist = 26
    RULE_idexop = 27
    RULE_func_call = 28
    RULE_stmt = 29
    RULE_null_stmt = 30
    RULE_assignstmt = 31
    RULE_lhs = 32
    RULE_ifstmt = 33
    RULE_forstmt = 34
    RULE_assign = 35
    RULE_whilestmt = 36
    RULE_dwstmt = 37
    RULE_brkstmt = 38
    RULE_constmt = 39
    RULE_rtrnstmt = 40
    RULE_exprlist = 41
    RULE_callstmt = 42
    RULE_blockstmt = 43
    RULE_stmtlist = 44
    RULE_stmtprime = 45
    RULE_stmttype = 46

    ruleNames =  [ "program", "decllist", "decl", "arrdcl", "atom", "intlist", 
                   "variabledcl", "vardcl_full", "vardcl_short", "idlist", 
                   "paradcl", "paratype", "funcdcl", "functype", "paralist", 
                   "paraprime", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "sub_expr", "arraylit", "nullable_explist", 
                   "idexop", "func_call", "stmt", "null_stmt", "assignstmt", 
                   "lhs", "ifstmt", "forstmt", "assign", "whilestmt", "dwstmt", 
                   "brkstmt", "constmt", "rtrnstmt", "exprlist", "callstmt", 
                   "blockstmt", "stmtlist", "stmtprime", "stmttype" ]

    EOF = Token.EOF
    Binary1=1
    Binary2=2
    Binary4=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    WHILE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    INHERIT=21
    ARRAY=22
    NEG=23
    AND=24
    OR=25
    EQUAL=26
    DIF=27
    PLUS=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    LT=33
    LTE=34
    GT=35
    GTE=36
    CONC=37
    LB=38
    RB=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    DOT=44
    COMMA=45
    SEMI=46
    COLON=47
    ASSIGN=48
    INTTYPE=49
    FLOATTYPE=50
    BOOLTYPE=51
    STRINGTYPE=52
    IDENTIFIER=53
    CPPCMT=54
    CCMT=55
    WS=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    ERROR_CHAR=59

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

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.decllist()
            self.state = 95
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.decl()
                self.state = 98
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variabledcl(self):
            return self.getTypedRuleContext(MT22Parser.VariabledclContext,0)


        def funcdcl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.variabledcl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.funcdcl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atom(self):
            return self.getTypedRuleContext(MT22Parser.AtomContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrdcl




    def arrdcl(self):

        localctx = MT22Parser.ArrdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrdcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MT22Parser.ARRAY)
            self.state = 108
            self.match(MT22Parser.LSB)
            self.state = 109
            self.intlist()
            self.state = 110
            self.match(MT22Parser.RSB)
            self.state = 111
            self.match(MT22Parser.OF)
            self.state = 112
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atom




    def atom(self):

        localctx = MT22Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
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


    class IntlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intlist(self):
            return self.getTypedRuleContext(MT22Parser.IntlistContext,0)


        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_intlist




    def intlist(self):

        localctx = MT22Parser.IntlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_intlist)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(MT22Parser.INTTYPE)
                self.state = 117
                self.match(MT22Parser.COMMA)
                self.state = 119
                self.intlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(MT22Parser.INTTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def vardcl_full(self):
            return self.getTypedRuleContext(MT22Parser.Vardcl_fullContext,0)


        def vardcl_short(self):
            return self.getTypedRuleContext(MT22Parser.Vardcl_shortContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledcl




    def variabledcl(self):

        localctx = MT22Parser.VariabledclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variabledcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 123
                self.vardcl_full()
                pass

            elif la_ == 2:
                self.state = 124
                self.vardcl_short()
                pass


            self.state = 127
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardcl_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def vardcl_full(self):
            return self.getTypedRuleContext(MT22Parser.Vardcl_fullContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def paratype(self):
            return self.getTypedRuleContext(MT22Parser.ParatypeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vardcl_full




    def vardcl_full(self):

        localctx = MT22Parser.Vardcl_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vardcl_full)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(MT22Parser.IDENTIFIER)
                self.state = 130
                self.match(MT22Parser.COMMA)
                self.state = 131
                self.vardcl_full()
                self.state = 132
                self.match(MT22Parser.COMMA)
                self.state = 133
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(MT22Parser.IDENTIFIER)
                self.state = 136
                self.match(MT22Parser.COLON)
                self.state = 137
                self.paratype()
                self.state = 138
                self.match(MT22Parser.ASSIGN)
                self.state = 139
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardcl_shortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def paratype(self):
            return self.getTypedRuleContext(MT22Parser.ParatypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardcl_short




    def vardcl_short(self):

        localctx = MT22Parser.Vardcl_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vardcl_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.idlist()
            self.state = 144
            self.match(MT22Parser.COLON)
            self.state = 145
            self.paratype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idlist)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(MT22Parser.IDENTIFIER)
                self.state = 148
                self.match(MT22Parser.COMMA)
                self.state = 150
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def paratype(self):
            return self.getTypedRuleContext(MT22Parser.ParatypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paradcl




    def paradcl(self):

        localctx = MT22Parser.ParadclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paradcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 154
                self.match(MT22Parser.INHERIT)


            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 157
                self.match(MT22Parser.OUT)


            self.state = 160
            self.match(MT22Parser.IDENTIFIER)
            self.state = 161
            self.match(MT22Parser.COLON)
            self.state = 162
            self.paratype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def arrdcl(self):
            return self.getTypedRuleContext(MT22Parser.ArrdclContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paratype




    def paratype(self):

        localctx = MT22Parser.ParatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paratype)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
                self.arrdcl()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 169
                self.match(MT22Parser.AUTO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIER)
            else:
                return self.getToken(MT22Parser.IDENTIFIER, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def functype(self):
            return self.getTypedRuleContext(MT22Parser.FunctypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(MT22Parser.ParalistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdcl




    def funcdcl(self):

        localctx = MT22Parser.FuncdclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcdcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MT22Parser.IDENTIFIER)
            self.state = 173
            self.match(MT22Parser.COLON)
            self.state = 174
            self.match(MT22Parser.FUNCTION)
            self.state = 175
            self.functype()
            self.state = 176
            self.match(MT22Parser.LB)
            self.state = 177
            self.paralist()
            self.state = 178
            self.match(MT22Parser.RB)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 179
                self.match(MT22Parser.INHERIT)
                self.state = 180
                self.match(MT22Parser.IDENTIFIER)


            self.state = 183
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def arrdcl(self):
            return self.getTypedRuleContext(MT22Parser.ArrdclContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functype




    def functype(self):

        localctx = MT22Parser.FunctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functype)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.arrdcl()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 7)
                self.state = 191
                self.match(MT22Parser.AUTO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraprime(self):
            return self.getTypedRuleContext(MT22Parser.ParaprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paralist




    def paralist(self):

        localctx = MT22Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paralist)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.paraprime()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraprime(self):
            return self.getTypedRuleContext(MT22Parser.ParaprimeContext,0)


        def paradcl(self):
            return self.getTypedRuleContext(MT22Parser.ParadclContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paraprime




    def paraprime(self):

        localctx = MT22Parser.ParaprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paraprime)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.paradcl()
                self.state = 199
                self.match(MT22Parser.COMMA)
                self.state = 201
                self.paraprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.paradcl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def CONC(self):
            return self.getToken(MT22Parser.CONC, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expr1()
                self.state = 207
                self.match(MT22Parser.CONC)
                self.state = 208
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def Binary1(self):
            return self.getToken(MT22Parser.Binary1, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr1)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expr2(0)
                self.state = 214
                self.match(MT22Parser.Binary1)
                self.state = 215
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def Binary2(self):
            return self.getToken(MT22Parser.Binary2, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    self.match(MT22Parser.Binary2)
                    self.state = 225
                    self.expr3(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUS or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 236
                    self.expr4(0) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def Binary4(self):
            return self.getToken(MT22Parser.Binary4, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    self.match(MT22Parser.Binary4)
                    self.state = 247
                    self.expr5() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(MT22Parser.NEG, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr5)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(MT22Parser.NEG)
                self.state = 254
                self.expr5()
                pass
            elif token in [MT22Parser.SUB, MT22Parser.LB, MT22Parser.LCB, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.BOOLTYPE, MT22Parser.STRINGTYPE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr6)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(MT22Parser.SUB)
                self.state = 259
                self.expr6()
                pass
            elif token in [MT22Parser.LB, MT22Parser.LCB, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.BOOLTYPE, MT22Parser.STRINGTYPE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MT22Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MT22Parser.FLOATTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MT22Parser.BOOLTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MT22Parser.STRINGTYPE, 0)

        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sub_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr7)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(MT22Parser.INTTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(MT22Parser.FLOATTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(MT22Parser.BOOLTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(MT22Parser.STRINGTYPE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.arraylit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.lhs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sub_expr




    def sub_expr(self):

        localctx = MT22Parser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.LB)
            self.state = 274
            self.expr()
            self.state = 275
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def nullable_explist(self):
            return self.getTypedRuleContext(MT22Parser.Nullable_explistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MT22Parser.LCB)
            self.state = 278
            self.nullable_explist()
            self.state = 279
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_explistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_nullable_explist




    def nullable_explist(self):

        localctx = MT22Parser.Nullable_explistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_nullable_explist)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NEG, MT22Parser.SUB, MT22Parser.LB, MT22Parser.LCB, MT22Parser.INTTYPE, MT22Parser.FLOATTYPE, MT22Parser.BOOLTYPE, MT22Parser.STRINGTYPE, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.exprlist()
                pass
            elif token in [MT22Parser.RB, MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idexop




    def idexop(self):

        localctx = MT22Parser.IdexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_idexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MT22Parser.IDENTIFIER)
            self.state = 286
            self.match(MT22Parser.LSB)
            self.state = 287
            self.exprlist()
            self.state = 288
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def nullable_explist(self):
            return self.getTypedRuleContext(MT22Parser.Nullable_explistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_call




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MT22Parser.IDENTIFIER)
            self.state = 291
            self.match(MT22Parser.LB)
            self.state = 292
            self.nullable_explist()
            self.state = 293
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dwstmt(self):
            return self.getTypedRuleContext(MT22Parser.DwstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def rtrnstmt(self):
            return self.getTypedRuleContext(MT22Parser.RtrnstmtContext,0)


        def brkstmt(self):
            return self.getTypedRuleContext(MT22Parser.BrkstmtContext,0)


        def constmt(self):
            return self.getTypedRuleContext(MT22Parser.ConstmtContext,0)


        def null_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Null_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 299
                self.dwstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 300
                self.callstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 301
                self.blockstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 302
                self.rtrnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 303
                self.brkstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 304
                self.constmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 305
                self.null_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_null_stmt




    def null_stmt(self):

        localctx = MT22Parser.Null_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_null_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MT22Parser.AssignContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.assign()
            self.state = 311
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def idexop(self):
            return self.getTypedRuleContext(MT22Parser.IdexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lhs)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(MT22Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.idexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MT22Parser.IF)
            self.state = 318
            self.match(MT22Parser.LB)
            self.state = 319
            self.expr()
            self.state = 320
            self.match(MT22Parser.RB)
            self.state = 321
            self.stmt()
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 322
                self.match(MT22Parser.ELSE)
                self.state = 323
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def assign(self):
            return self.getTypedRuleContext(MT22Parser.AssignContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MT22Parser.FOR)
            self.state = 327
            self.match(MT22Parser.LB)
            self.state = 328
            self.assign()
            self.state = 329
            self.match(MT22Parser.COMMA)
            self.state = 330
            self.expr()
            self.state = 331
            self.match(MT22Parser.COMMA)
            self.state = 332
            self.expr()
            self.state = 333
            self.match(MT22Parser.RB)
            self.state = 334
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign




    def assign(self):

        localctx = MT22Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.lhs()
            self.state = 337
            self.match(MT22Parser.ASSIGN)
            self.state = 338
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MT22Parser.WHILE)
            self.state = 341
            self.match(MT22Parser.LB)
            self.state = 342
            self.expr()
            self.state = 343
            self.match(MT22Parser.RB)
            self.state = 344
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DwstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dwstmt




    def dwstmt(self):

        localctx = MT22Parser.DwstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_dwstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MT22Parser.DO)
            self.state = 347
            self.blockstmt()
            self.state = 348
            self.match(MT22Parser.WHILE)
            self.state = 349
            self.match(MT22Parser.LB)
            self.state = 350
            self.expr()
            self.state = 351
            self.match(MT22Parser.RB)
            self.state = 352
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BrkstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_brkstmt




    def brkstmt(self):

        localctx = MT22Parser.BrkstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_brkstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MT22Parser.BREAK)
            self.state = 355
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_constmt




    def constmt(self):

        localctx = MT22Parser.ConstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_constmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MT22Parser.CONTINUE)
            self.state = 358
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RtrnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_rtrnstmt




    def rtrnstmt(self):

        localctx = MT22Parser.RtrnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_rtrnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MT22Parser.RETURN)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.NEG) | (1 << MT22Parser.SUB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.INTTYPE) | (1 << MT22Parser.FLOATTYPE) | (1 << MT22Parser.BOOLTYPE) | (1 << MT22Parser.STRINGTYPE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 361
                self.expr()


            self.state = 364
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exprlist)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.expr()
                self.state = 367
                self.match(MT22Parser.COMMA)
                self.state = 368
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_callstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(MT22Parser.IDENTIFIER)
            self.state = 374
            self.match(MT22Parser.LB)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.NEG) | (1 << MT22Parser.SUB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.INTTYPE) | (1 << MT22Parser.FLOATTYPE) | (1 << MT22Parser.BOOLTYPE) | (1 << MT22Parser.STRINGTYPE) | (1 << MT22Parser.IDENTIFIER))) != 0):
                self.state = 375
                self.exprlist()


            self.state = 378
            self.match(MT22Parser.RB)
            self.state = 379
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MT22Parser.LCB)
            self.state = 382
            self.stmtlist()
            self.state = 383
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(MT22Parser.StmtprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmtlist)
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LCB, MT22Parser.SEMI, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.stmtprime()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmttype(self):
            return self.getTypedRuleContext(MT22Parser.StmttypeContext,0)


        def stmtprime(self):
            return self.getTypedRuleContext(MT22Parser.StmtprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtprime




    def stmtprime(self):

        localctx = MT22Parser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtprime)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.stmttype()
                self.state = 390
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.stmttype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmttypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def variabledcl(self):
            return self.getTypedRuleContext(MT22Parser.VariabledclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmttype




    def stmttype(self):

        localctx = MT22Parser.StmttypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmttype)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.variabledcl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr2_sempred
        self._predicates[19] = self.expr3_sempred
        self._predicates[20] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




