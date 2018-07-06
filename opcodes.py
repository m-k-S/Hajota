#!/usr/bin/python3

# Opcode structure for bytecode processing

class OpCode:
    def __init__(self, op):
        self.Op = op

    def isPush(self):
        if 0x60 <= self.Op <= 0x7f:
            return True
        else:
            return False

    def hasSideEffects(self):
        if self.Op == 0xf1:
            return True
        else:
            return False

    def isDup(self):
        if 0x80 <= self.Op <= 0x8f:
            return True
        else:
            return False

    def isSwap(self):
        if 0x90 <= self.Op <= 0x9f:
            return True
        else:
            return False

    def operandSize(self):
        if not self.isPush():
            return 0
        else:
            return int(Op - 0x60 + 1)

    def isJump(self):
        if (self.Op == 0x56) or (self.Op == 0x57):
            return True
        else:
            return False

# Arithmetic
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

# Comparisons and Bitwise Operators
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

# Environment
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

BLOCKHASH = OpCode(0x40)
COINBASE = OpCode(0x41)
TIMESTAMP = OpCode(0x42)
NUMBER = OpCode(0x43)
DIFFICULTY = OpCode(0x44)
GASLIMIT = OpCode(0x45)

POP = OpCode(0x50)
MLOAD = OpCode(0x51)
MSTORE = OpCode(0x52)
MSTORE8 = OpCode(0x53)
SLOAD = OpCode(0x54)
SSTORE = OpCode(0x55)
JUMP = OpCode(0x56)
JUMPI = OpCode(0x57)
PC = OpCode(0x58)
MSIZE = OpCode(0x59)
GAS = OpCode(0x60)
JUMPDEST = OpCode(0x61)

PUSH1 = OpCode(0x60)
PUSH2 = OpCode(0x61)
PUSH3 = OpCode(0x62)
PUSH4 = OpCode(0x63)
PUSH5 = OpCode(0x64)
PUSH6 = OpCode(0x65)
PUSH7 = OpCode(0x66)
PUSH8 = OpCode(0x67)
PUSH9 = OpCode(0x68)
PUSH10 = OpCode(0x69)
PUSH11 = OpCode(0x6a)
PUSH12 = OpCode(0x6b)
PUSH13 = OpCode(0x6c)
PUSH14 = OpCode(0x6d)
PUSH15 = OpCode(0x6e)
PUSH16 = OpCode(0x6f)
PUSH17 = OpCode(0x70)
PUSH18 = OpCode(0x71)
PUSH19 = OpCode(0x72)
PUSH20 = OpCode(0x73)
PUSH21 = OpCode(0x74)
PUSH22 = OpCode(0x75)
PUSH23 = OpCode(0x76)
PUSH24 = OpCode(0x77)
PUSH25 = OpCode(0x78)
PUSH26 = OpCode(0x79)
PUSH27 = OpCode(0x7a)
PUSH28 = OpCode(0x7b)
PUSH29 = OpCode(0x7c)
PUSH30 = OpCode(0x7d)
PUSH31 = OpCode(0x7e)
PUSH32 = OpCode(0x7f)

DUP1 = OpCode(0x80)
DUP2 = OpCode(0x81)
DUP3 = OpCode(0x82)
DUP4 = OpCode(0x83)
DUP5 = OpCode(0x84)
DUP6 = OpCode(0x85)
DUP7 = OpCode(0x86)
DUP8 = OpCode(0x87)
DUP9 = OpCode(0x88)
DUP10 = OpCode(0x89)
DUP11 = OpCode(0x8a)
DUP12 = OpCode(0x8b)
DUP13 = OpCode(0x8c)
DUP14 = OpCode(0x8d)
DUP15 = OpCode(0x8e)
DUP16 = OpCode(0x8f)

SWAP1 = OpCode(0x90)
SWAP2 = OpCode(0x91)
SWAP3 = OpCode(0x92)
SWAP4 = OpCode(0x93)
SWAP5 = OpCode(0x94)
SWAP6 = OpCode(0x95)
SWAP7 = OpCode(0x96)
SWAP8 = OpCode(0x97)
SWAP9 = OpCode(0x98)
SWAP10 = OpCode(0x99)
SWAP11 = OpCode(0x9a)
SWAP12 = OpCode(0x9b)
SWAP13 = OpCode(0x9c)
SWAP14 = OpCode(0x9d)
SWAP15 = OpCode(0x9e)
SWAP16 = OpCode(0x9f)

LOG0 = OpCode(0xa0)
LOG1 = OpCode(0xa1)
LOG2 = OpCode(0xa2)
LOG3 = OpCode(0xa3)
LOG4 = OpCode(0xa4)

CREATE = OpCode(0xf0)
CALL = OpCode(0xf1)
CALLCODE = OpCode(0xf2)
RETURN = OpCode(0xf3)
DELEGATECALL = OpCode(0xf4)
INVALID = OpCode(0xfe)
REVERT = OpCode(0xfd)
SELFDESTRUCT = OpCode(0xff)

OpcodeString = {
    0x0: "STOP",
    0x1: "ADD",
    0x2: "MUL",
    0x3: "SUB",
    0x4: "DIV",
    0x5: "SDIV",
    0x6: "MOD",
    0x7: "SMOD",
    0x8: "ADDMOD",
    0x9: "MULMOD",
    0xa: "EXP",
    0xb: "SIGNEXTEND",
    0x10: "LT",
    0x11: "GT",
    0x12: "SLT",
    0x13: "SGT",
    0x14: "EQ",
    0x15: "ISZERO",
    0x16: "AND",
    0x17: "OR",
    0x18: "XOR",
    0x19: "NOT",
    0x1a: "BYTE",
    0x20: "SHA3",
    0x30: "ADDRESS",
    0x31: "BALANCE",
    0x32: "ORIGIN",
    0x33: "CALLER",
    0x34: "CALLVALUE",
    0x35: "CALLDATALOAD",
    0x36: "CALLDATASIZE",
    0x37: "CALLDATACOPY",
    0x38: "CODESIZE",
    0x39: "CODECOPY",
    0x3a: "GASPRICE",
    0x3b: "EXTCODESIZE",
    0x3c: "EXTCODECOPY",
    0x40: "BLOCKHASH",
    0x41: "COINBASE",
    0x42: "TIMESTAMP",
    0x43: "NUMBER",
    0x44: "DIFFICULTY",
    0x45: "GASLIMIT",
    0x50: "POP",
    0x51: "MLOAD",
    0x52: "MSTORE",
    0x53: "MSTORE8",
    0x54: "SLOAD",
    0x55: "SSTORE",
    0x56: "JUMP",
    0x57: "JUMPI",
    0x58: "PC",
    0x59: "MSIZE",
    0x60: "GAS",
    0x61: "JUMPDEST",
    0x60: "PUSH1",
    0x61: "PUSH2",
    0x62: "PUSH3",
    0x63: "PUSH4",
    0x64: "PUSH5",
    0x65: "PUSH6",
    0x66: "PUSH7",
    0x67: "PUSH8",
    0x68: "PUSH9",
    0x69: "PUSH10",
    0x6a: "PUSH11",
    0x6b: "PUSH12",
    0x6c: "PUSH13",
    0x6d: "PUSH14",
    0x6e: "PUSH15",
    0x6f: "PUSH16",
    0x70: "PUSH17",
    0x71: "PUSH18",
    0x72: "PUSH19",
    0x73: "PUSH20",
    0x74: "PUSH21",
    0x75: "PUSH22",
    0x76: "PUSH23",
    0x77: "PUSH24",
    0x78: "PUSH25",
    0x79: "PUSH26",
    0x7a: "PUSH27",
    0x7b: "PUSH28",
    0x7c: "PUSH29",
    0x7d: "PUSH30",
    0x7e: "PUSH31",
    0x7f: "PUSH32",
    0x80: "DUP1",
    0x81: "DUP2",
    0x82: "DUP3",
    0x83: "DUP4",
    0x84: "DUP5",
    0x85: "DUP6",
    0x86: "DUP7",
    0x87: "DUP8",
    0x88: "DUP9",
    0x89: "DUP10",
    0x8a: "DUP11",
    0x8b: "DUP12",
    0x8c: "DUP13",
    0x8d: "DUP14",
    0x8e: "DUP15",
    0x8f: "DUP16",
    0x90: "SWAP1",
    0x91: "SWAP2",
    0x92: "SWAP3",
    0x93: "SWAP4",
    0x94: "SWAP5",
    0x95: "SWAP6",
    0x96: "SWAP7",
    0x97: "SWAP8",
    0x98: "SWAP9",
    0x99: "SWAP10",
    0x9a: "SWAP11",
    0x9b: "SWAP12",
    0x9c: "SWAP13",
    0x9d: "SWAP14",
    0x9e: "SWAP15",
    0x9f: "SWAP16",
    0xa0: "LOG0",
    0xa1: "LOG1",
    0xa2: "LOG2",
    0xa3: "LOG3",
    0xa4: "LOG4",
    0xf0: "CREATE",
    0xf1: "CALL",
    0xf2: "CALLCODE",
    0xf3: "RETURN",
    0xf4: "DELEGATECALL",
    0xfe: "INVALID",
    0xfd: "REVERT",
    0xff: "SELFDESTRUCT"
}

def toString(Opcode):
    opString = OpcodeString[int(Opcode.Op, 16)]
    if len(opString) == 0:
        print("Missing opcode 0x{}".format(str(opString)))
        return 0
    return opString

def stringToOp(opString):
    return (list(OpcodeString.keys())[list(OpcodeString.values()).index(opString)])

OpcodeStackReads = {
    STOP:       0,
	ADD:        2,
	MUL:        2,
	SUB:        2,
	DIV:        2,
	SDIV:       2,
	MOD:        2,
	SMOD:       2,
	EXP:        2,
	NOT:        1,
	LT:         2,
	GT:         2,
	SLT:        2,
	SGT:        2,
	EQ:         2,
	ISZERO:     1,
	SIGNEXTEND: 1,

	AND:    2,
	OR:     2,
	XOR:    2,
	BYTE:   2,
	ADDMOD: 3,
	MULMOD: 3,
	SHA3: 2,

	ADDRESS:      0,
	BALANCE:      1,
	ORIGIN:       0,
	CALLER:       0,
	CALLVALUE:    0,
	CALLDATALOAD: 1,
	CALLDATASIZE: 0,
	CALLDATACOPY: 3,
	CODESIZE:     0,
	CODECOPY:     3,
	GASPRICE:     0,

	BLOCKHASH:   1,
	COINBASE:    0,
	TIMESTAMP:   0,
	NUMBER:      0,
	DIFFICULTY:  0,
	GASLIMIT:    0,
	EXTCODESIZE: 1,
	EXTCODECOPY: 4,

	POP: 1,
	MLOAD:    1,
	MSTORE:   2,
	MSTORE8:  2,
	SLOAD:    1,
	SSTORE:   2,
	JUMP:     1,
	JUMPI:    2,
	PC:       0,
	MSIZE:    0,
	GAS:      0,
	JUMPDEST: 0,

	PUSH1:  0,
	PUSH2:  0,
	PUSH3:  0,
	PUSH4:  0,
	PUSH5:  0,
	PUSH6:  0,
	PUSH7:  0,
	PUSH8:  0,
	PUSH9:  0,
	PUSH10: 0,
	PUSH11: 0,
	PUSH12: 0,
	PUSH13: 0,
	PUSH14: 0,
	PUSH15: 0,
	PUSH16: 0,
	PUSH17: 0,
	PUSH18: 0,
	PUSH19: 0,
	PUSH20: 0,
	PUSH21: 0,
	PUSH22: 0,
	PUSH23: 0,
	PUSH24: 0,
	PUSH25: 0,
	PUSH26: 0,
	PUSH27: 0,
	PUSH28: 0,
	PUSH29: 0,
	PUSH30: 0,
	PUSH31: 0,
	PUSH32: 0,

	DUP1:  1,
	DUP2:  2,
	DUP3:  3,
	DUP4:  4,
	DUP5:  5,
	DUP6:  6,
	DUP7:  7,
	DUP8:  8,
	DUP9:  9,
	DUP10: 10,
	DUP11: 11,
	DUP12: 12,
	DUP13: 13,
	DUP14: 14,
	DUP15: 15,
	DUP16: 16,

	SWAP1:  2,
	SWAP2:  3,
	SWAP3:  4,
	SWAP4:  5,
	SWAP5:  6,
	SWAP6:  7,
	SWAP7:  8,
	SWAP8:  9,
	SWAP9:  10,
	SWAP10: 11,
	SWAP11: 12,
	SWAP12: 13,
	SWAP13: 14,
	SWAP14: 15,
	SWAP15: 16,
	SWAP16: 17,
	LOG0:   2,
	LOG1:   3,
	LOG2:   4,
	LOG3:   5,
	LOG4:   6,

	CREATE:       3,
	CALL:         7,
	RETURN:       2,
	CALLCODE:     7,
	DELEGATECALL: 6,
	INVALID:      0,
	REVERT:       0,
	SELFDESTRUCT: 1,
}

def StackReads(Op):
    return OpcodeStackReads[Op]

OpcodeStackWrites = {
    STOP:       0,
    ADD:        1,
    MUL:        1,
    SUB:        1,
    DIV:        1,
    SDIV:       1,
    MOD:        1,
    SMOD:       1,
    EXP:        1,
    NOT:        1,
    LT:         1,
    GT:         1,
    SLT:        1,
    SGT:        1,
    EQ:         1,
    ISZERO:     1,
    SIGNEXTEND: 1,

    AND:    1,
    OR:     1,
    XOR:    1,
    BYTE:   1,
    ADDMOD: 1,
    MULMOD: 1,
    SHA3: 1,

    ADDRESS:      1,
    BALANCE:      1,
    ORIGIN:       1,
    CALLER:       1,
    CALLVALUE:    1,
    CALLDATALOAD: 1,
    CALLDATASIZE: 1,
    CALLDATACOPY: 0,
    CODESIZE:     1,
    CODECOPY:     0,
    GASPRICE:     1,

    BLOCKHASH:   1,
    COINBASE:    1,
    TIMESTAMP:   1,
    NUMBER:      1,
    DIFFICULTY:  1,
    GASLIMIT:    1,
    EXTCODESIZE: 1,
    EXTCODECOPY: 0,

    POP: 0,
    MLOAD:    1,
    MSTORE:   0,
    MSTORE8:  0,
    SLOAD:    1,
    SSTORE:   0,
    JUMP:     0,
    JUMPI:    0,
    PC:       1,
    MSIZE:    1,
    GAS:      1,
    JUMPDEST: 0,

    PUSH1:  1,
    PUSH2:  1,
    PUSH3:  1,
    PUSH4:  1,
    PUSH5:  1,
    PUSH6:  1,
    PUSH7:  1,
    PUSH8:  1,
    PUSH9:  1,
    PUSH10: 1,
    PUSH11: 1,
    PUSH12: 1,
    PUSH13: 1,
    PUSH14: 1,
    PUSH15: 1,
    PUSH16: 1,
    PUSH17: 1,
    PUSH18: 1,
    PUSH19: 1,
    PUSH20: 1,
    PUSH21: 1,
    PUSH22: 1,
    PUSH23: 1,
    PUSH24: 1,
    PUSH25: 1,
    PUSH26: 1,
    PUSH27: 1,
    PUSH28: 1,
    PUSH29: 1,
    PUSH30: 1,
    PUSH31: 1,
    PUSH32: 1,

    DUP1:  2,
    DUP2:  3,
    DUP3:  4,
    DUP4:  5,
    DUP5:  6,
    DUP6:  7,
    DUP7:  8,
    DUP8:  9,
    DUP9:  10,
    DUP10: 11,
    DUP11: 12,
    DUP12: 13,
    DUP13: 14,
    DUP14: 15,
    DUP15: 16,
    DUP16: 17,

    SWAP1:  2,
    SWAP2:  3,
    SWAP3:  4,
    SWAP4:  5,
    SWAP5:  6,
    SWAP6:  7,
    SWAP7:  8,
    SWAP8:  9,
    SWAP9:  10,
    SWAP10: 11,
    SWAP11: 12,
    SWAP12: 13,
    SWAP13: 14,
    SWAP14: 15,
    SWAP15: 16,
    SWAP16: 17,
    LOG0:   0,
    LOG1:   0,
    LOG2:   0,
    LOG3:   0,
    LOG4:   0,

    CREATE:       1,
    CALL:         1,
    RETURN:       0,
    CALLCODE:     1,
    DELEGATECALL: 1,
    INVALID:      0,
    REVERT:       0,
    SELFDESTRUCT: 0,
}

def StackWrites(Op):
    return OpcodeStackWrites[Op]
