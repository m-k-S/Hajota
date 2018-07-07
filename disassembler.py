#!/usr/bin/python3.7

# Takes bytecode as input and returns program structure

from opcodes import *

class Instruction:
    def __init__(self, Opcode, Arg, Address):
        self.Opcode = Opcode
        self.Arg = Arg
        self.Address = Address

    def toString(self):
        if self.Arg is not None:
            return ("[{}]: {} {}".format(hex(self.Address), toString(self.Opcode), hex(self.Arg)))
        else:
            return ("[{}]: {}".format(hex(self.Address), toString(self.Opcode)))


class BasicBlock:
    def __init__(self, Instructions, Offset, Next):
        self.Instructions = Instructions
        self.Offset = Offset
        self.Next = Next

    def offsetOf(instruction):
        offset = self.Offset
        for i in self.Instructions:
            if instruction == i:
                return offset

            offset += self.Instructions[i].Opcode.operandSize() + 1

        return -1

class Program:
    def __init__(self, Blocks, JumpDestinations, Functions):
        self.Blocks = Blocks
        self.JumpDestinations = JumpDestinations
        self.Functions = Functions

def newProgram(bytecode):
    bytecodeLength = len(bytecode)

    # Removes trailing hash information
    if (bytecode[bytecodeLength - 1] == 0x29) and (bytecode[bytecodeLength - 2] == 0x00) \
        and (bytecode[bytecodeLength - 43] == 0xa1) and (bytecode[bytecodeLength - 42] == 0x65):
            bytecodeLength -= 43
            bytecode = bytecode[:bytecodeLength]


    program = Program([], {}, {})

    currentBlock = BasicBlock([], 0, None)

    i = 0
    while i < bytecodeLength:
        op = OpCode(bytecode[i])
        size = op.operandSize()
        arg = None
        if size > 0:
            arg = 0
            j = 1
            while j <= size:
                arg = arg << 8
                if i + j < bytecodeLength:
                    arg = arg ^ bytecode[i + j]
                j += 1

        if op.isJumpDest():
            if len(currentBlock.Instructions) > 0:
                program.Blocks.append(currentBlock)
                newBlock = BasicBlock([], i, None)
                currentBlock.Next = newBlock
                currentBlock = newBlock

            currentBlock.Offset += 1
            program.JumpDestinations[i] = currentBlock

        else:
            instruction = Instruction(op, arg, None)
            currentBlock.Instructions.append(instruction)
            address = currentBlock.Offset - 1
            for instr in currentBlock.Instructions:
                address += instr.Opcode.operandSize() + 1
            currentBlock.Instructions[-1].Address = address

            if (op.isJump()) or (op.Ends()):
                program.Blocks.append(currentBlock)
                newBlock = BasicBlock([], i + size + 1, None)
                currentBlock.Next = newBlock
                currentBlock = newBlock

        i += size + 1

    if (len(currentBlock.Instructions) > 0) or (currentBlock.Offset in program.JumpDestinations):
        program.Blocks.append(currentBlock)

    else:
        program.Blocks[len(program.Blocks) - 1].Next = None

    return program

def computeProgramFunctions(program):
    instructions = []
    for block in program.Blocks:
        for instruction in block.Instructions:
            instructions.append(instruction)

    for index in range(len(instructions)):
        if (instructions[index].Opcode.Op == 0x63) and (instructions[index+1].Opcode.Op == 0x14) and (instructions[index+3].Opcode.Op == 0x57):
            destination = instructions[index+2].Arg
            program.Functions[destination] = "_function_{}".format(hex(instructions[index].Arg))

    return program
