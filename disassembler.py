#!/usr/bin/python3

# Takes bytecode as input and returns program structure

class Instruction:
    def __init__(self, Opcode, Arg):
        self.Opcode = Opcode
        self.Arg = Arg

    def toString(self):
        if self.Arg:
            # print("{} 0x{}".format(self.Opcode, self.Arg))
            return ("{} 0x{}".format(self.Opcode.toString(), str(self.Arg)))
        else:
            return self.Opcode.toString()

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
    def __init__(self, Blocks, JumpDestinations):
        self.Blocks = Blocks
        self.JumpDestinations = JumpDestinations

def newProgram(bytecode):
    bytecodeLength = len(bytecode)
    program = Program([], {})

    currentBlock = BasicBlock([], 0, None)

    i = 0
    while i < bytecodeLength:
        op = OpCode(bytecode[i])
        size = op.operandSize()
        arg = 0
        if size > 0:
            j = 1
            while j <= size:
                arg = arg << 8
                if i + j < bytecodeLength:
                    arg = arg ^ bytecode[i + j]
                j += 1

        if op == JUMPDEST:
            if len(currentBlock.Instructions) > 0:
                program.Blocks.append(currentBlock)
                newBlock = BasicBlack([], i, None)
                currentBlock.Next = newBlock
                currentBlock = newBlock

            currentBlock.Offset += 1
            program.JumpDestinations[i] = currentBlock

        else:
            instruction = Instruction(op, arg)
            currentBlock.Instructions.append(instruction)

            if (op.isJump()) or (op == RETURN) or (op == SELFDESTRUCT) or (op == STOP) or (op == INVALID) or (op == REVERT):
                program.Blocks.append(currentBlock)
                newBlock = BasicBlock([], i + size + 1, None)
                currentBlock.Next = newBlock
                currentBlock = newBlock

        i += size + 1

    if (len(currentBlock.Instructions) > 0) or (program.JumpDestinations[currentBlock.Offset]):
        program.Blocks.append(currentBlock)

    else:
        program.Blocks[len(program.Blocks) - 1].Next = None

    return program
