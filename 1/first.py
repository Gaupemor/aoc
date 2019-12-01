import numpy as np

"""
Day 1 - Puzzle 1 & 2
https://adventofcode.com/2019/day/1
"""
module_masses = np.loadtxt(fname = "input.txt")

module_total_fuel_req = complete_total_fuel_req = 0

for module_mass in module_masses:
    module_fuel_req = int(module_mass / 3) - 2

    # Part 1
    module_total_fuel_req += module_fuel_req

    # Part 2
    while module_fuel_req > 0:
        complete_total_fuel_req += module_fuel_req
        module_fuel_req = int(module_fuel_req / 3) - 2


print(f"1: Module total fuel requirements: {module_total_fuel_req}")
# 3254441
print(f"2: Complete total fuel requirements: {complete_total_fuel_req}")
# 4878818
