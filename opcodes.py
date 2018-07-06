

STOP = OpCode(0x0)
ADD = OpCode(0x1)
MUL = OpCode(0x2)
SUB = OpCode(0x3)
DIV = OpCode(0x4)
SDIV = OpCode(0x5)
MOD = OpCode(0x6)
SMOD = OpCode(0x7)
ADDMOD = OpCode(0x8)
MULMOD = OpCode(0x9)
EXP = OpCode(0xa)
SIGNEXTEND = OpCode(0xb)

LT = OpCode(0x10)
GT = OpCode(0x11)
SLT = OpCode(0x12)
SGT = OpCode(0x13)
EQ = OpCode(0x14)
ISZERO = OpCode(0x15)
AND = OpCode(0x16)
OR = OpCode(0x17)
XOR = OpCode(0x18)
NOT = OpCode(0x19)
BYTE = OpCode(0x1a)
SHA3 = OpCode(0x20)

ADDRESS = OpCode(0x30)
BALANCE = OpCode(0x31)
ORIGIN = OpCode(0x32)
CALLER = OpCode(0x33)
CALLVALUE = OpCode(0x34)
CALLDATALOAD = OpCode(0x35)
CALLDATASIZE = OpCode(0x36)
CALLDATACOPY = OpCode(0x37)
CODESIZE = OpCode(0x38)
CODECOPY = OpCode(0x39)
GASPRICE = OpCode(0x3a)
EXTCODESIZE = OpCode(0x3b)
EXTCODECOPY = OpCode(0x3c)


class OpCode:
    def __init__(self, op):
        self.Op = op

    def isPush():
        if Op.startswith("PUSH"):
            return True
        else:
            return False

    def hasSideEffects():
        if p.startswith("CALL"):
            return True
        else:
            return False

    def isDup():
        if op.startswith("DUP"):
            return True
        else:
            return False

    def isSwap():
        if op.startswith("SWAP"):
            return True
        else:
            return False

    def operandSize():
        if not op.isPush():
            return 0
        else:
            return int(Op - PUSH1 + 1)

    def IsJump():
        if (Op == JUMP) or (Op == JUMPI):
            return True
        else:
            return False
