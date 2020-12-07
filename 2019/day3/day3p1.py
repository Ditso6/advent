# import
import re

# read input
input_file = open("paths.txt", "r")

first_path = re.findall("([UDLR])([0-9]*)", input_file.readline())
second_path = re.findall("([UDLR])([0-9]*)", input_file.readline())


def calculate_coordinates(path):
    coordinates = set()

    pos_x = 0
    pos_y = 0
    for instruction in path:
        direction = instruction[0]
        distance = int(instruction[1]) + 1
        if direction == "U":
            for i in range(1, distance):
                pos_y += 1
                coordinates.add((pos_x, pos_y))
        elif direction == "D":
            for i in range(1, distance):
                pos_y -= 1
                coordinates.add((pos_x, pos_y))
        elif direction == "R":
            for i in range(1, distance):
                pos_x += 1
                coordinates.add((pos_x, pos_y))
        elif direction == "L":
            for i in range(1, distance):
                pos_x -= 1
                coordinates.add((pos_x, pos_y))
    return coordinates


first_path_coordinates = calculate_coordinates(first_path)
second_path_coordinates = calculate_coordinates(second_path)

cross_section_coordinates = first_path_coordinates.intersection(second_path_coordinates)

cross_section_distances = map(lambda x: abs(x[0]) + abs(x[1]), cross_section_coordinates)
print min(cross_section_distances)

