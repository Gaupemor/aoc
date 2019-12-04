import numpy as np
import sys

"""
Day 4 - Puzzle 1 & 2
https://adventofcode.com/2019/day/4
"""

puzzle_input = "146810-612564"

# 1
first_passwords = list()

for num in range(int(puzzle_input.split("-")[0]), int(puzzle_input.split("-")[1])):
    num_string = str(num)

    all_increasing = True
    for i in range(1, 6):
        if num_string[i] < num_string[i-1]:
            all_increasing = False

    if not all_increasing:
        continue

    for i in range(1, 6):
        if num_string[i] == num_string[i-1]:
            first_passwords.append(num)
            break

# 2
second_passwords = list()

for num in first_passwords:
    num_string_array = list(str(num))

    unique, counts = np.unique(num_string_array, return_counts=True)
    if 2 in counts:
        second_passwords.append(num)

print(f"1: {len(first_passwords)}") # 1748
print(f"2: {len(second_passwords)}") # 1180
