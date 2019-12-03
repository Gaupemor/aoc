import numpy as np
import sys

"""
Day 3 - Puzzle 1 & 2
https://adventofcode.com/2019/day/3
"""

def path_directions():
    with open("input.txt", "r") as f:
        def wire_path_array(delimited_string):
            str_path = np.array(delimited_string.split(","))
            return np.array([(path[0], int(path[1:])) for path in str_path])

        return wire_path_array(f.readline().strip("\n")), wire_path_array(f.readline().strip("\n"))

# assuming the central port is located in position (0, 0)
def path_coordinates(path):
    complete_path = list()
    current_pos = np.array([0, 0])
    go_direction = None

    def go_left():
        current_pos[1] -= 1
        complete_path.append(np.copy(current_pos))
    def go_right():
        current_pos[1] += 1
        complete_path.append(np.copy(current_pos))
    def go_up():
        current_pos[0] -= 1
        complete_path.append(np.copy(current_pos))
    def go_down():
        current_pos[0] += 1
        complete_path.append(np.copy(current_pos))

    for direction, steps in path:
        if direction == 'R':
            go_direction = go_right
        if direction == 'L':
            go_direction = go_left
        if direction == 'U':
            go_direction = go_up
        if direction == 'D':
            go_direction = go_down

        for i in range(int(steps)):
            go_direction()

    return np.array(complete_path)

wire_1, wire_2 = path_directions()
complete_path_1 = path_coordinates(wire_1)
complete_path_2 = path_coordinates(wire_2)

intersections = np.array(
    [x for x in
    set([tuple(x) for x in complete_path_1])
    & set([tuple(x) for x in complete_path_2])]
    )

def manhattan_distance():
    closest_intersection = sys.maxsize
    for i in intersections:
        path_length = abs(i[0]) + abs(i[1])
        #print(path_length)
        if path_length < closest_intersection:
            closest_intersection = path_length
    return closest_intersection

def shortest_joined_path():
    shortest_joined_path = sys.maxsize
    for i in intersections:
        
        # make nicer? vvvvvvv
        a = b = 0
        index = 1
        for c_1 in complete_path_1:
            if np.array_equal(i, c_1):
                a = index
                break
            index += 1
        index = 1
        for c_2 in complete_path_2:
            if np.array_equal(i, c_2):
                b = index
                break
            index += 1
        # ^^^^^^^^^^^^

        if a == b == 0:
            raise Exception("Could not located a listed intersection.")
        joined_path = a + b
        #print(f"{i}: {a} + {b} = {joined_path}")
        if joined_path < shortest_joined_path:
            shortest_joined_path = joined_path

    return shortest_joined_path

print(f"1: {manhattan_distance()}") # 466
print(f"2: {shortest_joined_path()}") # 9006
