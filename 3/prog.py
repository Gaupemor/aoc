import numpy as np
import sys

"""
Day 3 - Puzzle 1 & 2
https://adventofcode.com/2019/day/3
"""

# assuming the central port is located in position (0, 0)

# Calculate paths and intersections
def calculate():
    with open("input.txt", "r") as f:
        def generate_path_array(delimited_string):
            path = list()

            directional_path = np.array([(p[0], int(p[1:])) for p in np.array(delimited_string.split(","))])
            current_pos = np.array([0, 0])

            def go_left():
                current_pos[1] -= 1
                path.append(np.copy(current_pos))
            def go_right():
                current_pos[1] += 1
                path.append(np.copy(current_pos))
            def go_up():
                current_pos[0] -= 1
                path.append(np.copy(current_pos))
            def go_down():
                current_pos[0] += 1
                path.append(np.copy(current_pos))

            for direction, steps in directional_path:
                go_direction = None

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

            return np.array(path)

        def calculate_intersections(p_1, p_2):
            return np.array(
                [x for x in
                set([tuple(x) for x in p_1])
                & set([tuple(x) for x in p_2])]
                )

        path_1 = generate_path_array(f.readline().strip("\n"))
        path_2 = generate_path_array(f.readline().strip("\n"))
        calculated_intersections = calculate_intersections(path_1, path_2)

        return path_1, path_2, calculated_intersections

path_1, path_2, intersections = calculate()

# 1: Distance to nearest intersection
def manhattan_distance():
    closest_intersection = sys.maxsize
    for i in intersections:
        path_length = abs(i[0]) + abs(i[1])
        if path_length < closest_intersection:
            closest_intersection = path_length
    return closest_intersection

# 2: Shortest joined path to intersections
def shortest_joined_path():
    shortest_joined_path = sys.maxsize
    for i in intersections:
        i_1 = path_1.tolist().index(i.tolist()) + 1
        i_2 = path_2.tolist().index(i.tolist()) + 1

        joined_path = i_1 + i_2
        if joined_path < shortest_joined_path:
            shortest_joined_path = joined_path

    return shortest_joined_path

print(f"1: {manhattan_distance()}") # 466
print(f"2: {shortest_joined_path()}") # 9006
