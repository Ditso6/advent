# import
import re


class Point:
    x = 0
    y = 0
    steps = 0

    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# read input
input_file = open("paths.txt", "r")

first_path = re.findall("([UDLR])([0-9]*)", input_file.readline())
second_path = re.findall("([UDLR])([0-9]*)", input_file.readline())


def calculate_coordinates(path):
    coordinates = set()

    pos_x = 0
    pos_y = 0
    steps = 0
    for instruction in path:
        direction = instruction[0]
        distance = int(instruction[1]) + 1
        if direction == "U":
            for i in range(1, distance):
                pos_y += 1
                steps += 1
                coordinates.add(Point(pos_x, pos_y, steps))
        elif direction == "D":
            for i in range(1, distance):
                pos_y -= 1
                steps += 1
                coordinates.add(Point(pos_x, pos_y, steps))
        elif direction == "R":
            for i in range(1, distance):
                pos_x += 1
                steps += 1
                coordinates.add(Point(pos_x, pos_y, steps))
        elif direction == "L":
            for i in range(1, distance):
                pos_x -= 1
                steps += 1
                coordinates.add(Point(pos_x, pos_y, steps))
    return coordinates


first_path_coordinates = calculate_coordinates(first_path)
second_path_coordinates = calculate_coordinates(second_path)

cross_section_coordinates = first_path_coordinates.intersection(second_path_coordinates)

distances = []
for point in cross_section_coordinates:
    first_path_point = None
    first_steps = 0
    for fpoint in first_path_coordinates:
        if fpoint == point:
            first_steps = fpoint.steps
            continue

    second_steps = 0
    for spoint in second_path_coordinates:
        if spoint == point:
            second_steps = spoint.steps
            continue

    distances.append(first_steps + second_steps)

print min(distances)
