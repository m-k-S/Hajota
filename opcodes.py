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
            return int(self.Op - 0x60 + 1)

    def isJump(self):
        if (self.Op == 0x56) or (self.Op == 0x57):
            return True
        else:
            return False

    def isJumpDest(self):
        if (self.Op == 0x61):
            return True
        else:
            return False

    def Ends(self):
        if (self.Op == 0x00) or (self.Op == 0xf3) or (self.Op == 0xfd) or (self.Op == 0xfe) or (self.Op == 0xff):
            return True
        else:
            return False

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
    0x5a: "GAS",
    0x5b: "JUMPDEST",
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
    opString = OpcodeString[Opcode.Op]
    if len(opString) == 0:
        print("Missing opcode 0x{}".format(str(opString)))
        return 0
    return opString

def stringToOp(opString):
    return (list(OpcodeString.keys())[list(OpcodeString.values()).index(opString)])
