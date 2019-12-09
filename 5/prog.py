import numpy as np
import importlib.util

"""
Day 5 - Puzzle 1 & 2
https://adventofcode.com/2019/day/5
"""

# Updated prog.py in day 2 - containing the intcode computer
# Day 2 puzzles still solvable after changes

# setting up the intcode computer
spec = importlib.util.spec_from_file_location("prog", "../2/prog.py")
intcode = importlib.util.module_from_spec(spec)
spec.loader.exec_module(intcode)

computer = intcode.generate_computer()

intcode.compute(computer)

# 1: give input '1'
# All output except final == '0' indicate success
# Output: 16225258

# 2: give input '5'
# Output: 2808771
