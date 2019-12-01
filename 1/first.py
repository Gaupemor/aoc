import numpy as np

"""
Day 1 - Puzzle 1 & 2
https://adventofcode.com/2019/day/1
"""

module_masses = np.loadtxt(fname = "input.txt")
module_total_fuel_req = complete_total_fuel_req = 0


def calc_fuel_req(mass):
    return int(mass / 3) - 2


for module_mass in module_masses:
    module_fuel_req = calc_fuel_req(module_mass)

    # Part 1
    module_total_fuel_req += module_fuel_req

    # Part 2
    while module_fuel_req > 0:
        complete_total_fuel_req += module_fuel_req
        module_fuel_req = calc_fuel_req(module_fuel_req)


print(f"1: Module total fuel requirements: {module_total_fuel_req}") # 3254441
print(f"2: Complete total fuel requirements: {complete_total_fuel_req}") # 4878818
