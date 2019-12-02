import numpy as np

"""
Day 2 - Puzzle 1 & 2
https://adventofcode.com/2019/day/2
"""

intcode = np.array([int(n) for n in np.loadtxt(fname = "input.txt", delimiter=',')])

def code_99(program):
    return program[0]

def code_1(program, i):
    sum = program[program[i + 1]] + program[program[i + 2]]
    pos = program[i + 3]

    program[pos] = sum

def code_2(program, i):
    product = program[program[i + 1]] * program[program[i + 2]]
    pos = program[i + 3]

    program[pos] = product

def run_intcode_program(noun, verb):
    i = 0
    program = np.copy(intcode)
    program[1] = noun
    program[2] = verb

    while True:
        if program[i] == 1:
            code_1(program, i)
        elif program[i] == 2:
            code_2(program, i)
        else:
            return code_99(program)
        i += 4

# Puzzle 1: gravity
print(f"1: {run_intcode_program(12, 2)}") # 3931283

# Puzzle 2: find input yielding given result
for i in range(100):
    for j in range(100):
        if run_intcode_program(i, j) == 19690720:
            print(f"2: {100 * i + j}") # 6979
