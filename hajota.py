#!/usr/bin/python3

import disassembler
from opcodes import *
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bytecode", help="specify bytecode file")
    parser.add_argument("-d", "--dict", help="return output in dictionary (Mythril) format", action="store_true")
    args = parser.parse_args()

    with open(args.bytecode) as f:
        bytecode = f.read()
        bytecode = [bytecode[i:i+2] for i in range(0, len(bytecode), 2)]
        for j in range(len(bytecode)):
            bytecode[j] = int("0x" + bytecode[j], 0)

        Disassembled = disassembler.newProgram(bytecode)

        if args.dict:
            instruction_list = []
            for block in Disassembled.Blocks:
                offset = block.Offset

                for instruction in block.Instructions:
                    instruction_list.append({"address": instruction.Address, "opcode": toString(instruction.Opcode), "argument": instruction.Arg})

            print instruction_list

        else:
            for block in Disassembled.Blocks:
                offset = block.Offset

                for instruction in block.Instructions:
                    print instruction.toString()
