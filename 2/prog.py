import numpy as np
import sys
sys.setrecursionlimit(1000)

"""
Day 2 - Puzzle 1 & 2
https://adventofcode.com/2019/day/2

Modifications added for day 5.
"""

def generate_computer(input_file_name="input.txt"):
     return np.array([int(n) for n in np.loadtxt(fname = input_file_name, delimiter=',')])

def compute(computer):
    program = np.copy(computer)

    def run_instruction(i):
        instruction = str(program[i])
        optcode = int(instruction[len(instruction) - 1])
        parameter_modes = ''.join([instruction[x]
                                for x in range(0, len(instruction) - 1)
                                if (x != len(instruction) - 1
                                and x != len(instruction) - 2)])


        def generate_parameter_string(num_of_params):
            p_str = str(parameter_modes)
            while len(p_str) < num_of_params:
                p_str = "0" + p_str
            return p_str

        def code_1():
            nonlocal i
            p = generate_parameter_string(3)

            a = program[i + 1]
            if p[2] == '0':
                a = program[a]
            b = program[i + 2]
            if p[1] == '0':
                b = program[b]

            sum = a + b

            pos = program[i + 3]
            if p[0] != '0':
                raise Exception(f"The store parameter was set to mode 1. {instruction}")

            program[pos] = sum

            i += 4

        def code_2():
            nonlocal i
            p = generate_parameter_string(3)

            a = program[i + 1]
            if p[2] == '0':
                a = program[a]
            b = program[i + 2]
            if p[1] == '0':
                b = program[b]

            product = a * b

            pos = program[i + 3]
            if p[0] != '0':
                raise Exception(f"The store parameter was set to mode 1. {instruction}")

            program[pos] = product

            i += 4

        def code_3():
            nonlocal i
            p = generate_parameter_string(1)

            val = int(input(">>> "))
            program[program[i + 1]] = val
            if p[0] != '0':
                raise Exception(f"The store parameter was set to mode 1. {instruction}")

            i += 2

        def code_4():
            nonlocal i
            p = generate_parameter_string(1)

            val = program[i + 1]
            if p[0] == '0':
                val = program[val]

            print(val)

            i += 2

        def code_5():
            nonlocal i
            p = generate_parameter_string(2)

            indicator = program[i + 1]
            if p[1] == '0':
                indicator = program[indicator]

            if indicator != 0:
                i = program[i + 2]
                if p[0] == '0':
                    i = program[i]
            else:
                i += 3

        def code_6():
            nonlocal i
            p = generate_parameter_string(2)

            indicator = program[i + 1]
            if p[1] == '0':
                indicator = program[indicator]

            if indicator == 0:
                i = program[i + 2]
                if p[0] == '0':
                    i = program[i]
            else:
                i += 3

        def code_7():
            nonlocal i
            p = generate_parameter_string(3)

            a = program[i + 1]
            if p[2] == '0':
                a = program[a]
            b = program[i + 2]
            if p[1] == '0':
                b = program[b]

            store_val = 1 if a < b else 0

            pos = program[i + 3]
            if p[0] != '0':
                raise Exception(f"The store parameter was set to mode 1. {instruction}")

            program[pos] = store_val

            i += 4

        def code_8():
            nonlocal i
            p = generate_parameter_string(3)

            a = program[i + 1]
            if p[2] == '0':
                a = program[a]
            b = program[i + 2]
            if p[1] == '0':
                b = program[b]

            store_val = 1 if a == b else 0

            pos = program[i + 3]
            if p[0] != '0':
                raise Exception(f"The store parameter was set to mode 1. {instruction}")

            program[pos] = store_val

            i += 4


        def code_99():
            return program[0]


        if optcode in range(1, 9):
            if optcode == 1:
                code_1()
            elif optcode == 2:
                code_2()
            elif optcode == 3:
                code_3()
            elif optcode == 4:
                code_4()
            elif optcode == 5:
                code_5()
            elif optcode == 6:
                code_6()
            elif optcode == 7:
                code_7()
            elif optcode == 8:
                code_8()
            return run_instruction(i)
        else:
            return code_99()

    return run_instruction(0)

if __name__ == "__main__":
    intcode = generate_computer()

    def run_intcode_program(computer, noun, verb):
        program = np.copy(computer)
        program[1] = noun
        program[2] = verb

        return compute(program)

    # Puzzle 1: gravity
    print(f"1: {run_intcode_program(intcode, 12, 2)}") # 3931283

    # Puzzle 2: find input yielding given result
    for i in range(100):
        for j in range(100):
            if run_intcode_program(intcode, i, j) == 19690720:
                print(f"2: {100 * i + j}") # 6979
