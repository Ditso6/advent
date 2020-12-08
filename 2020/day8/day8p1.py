# imports
import re

# read input
input_file = open("instruction_set.txt", "r")

instruction_set = []
for line in input_file.readlines():
    instruction = re.search("([a-z]*)\s([-+0-9]*)", line).groups()
    instruction_set.append((instruction[0], int(instruction[1])))

accumulator = 0
instruction_position = 0
instruction_positions = []
while True:
    instruction = instruction_set[instruction_position]
    if instruction[0] == "acc":
        accumulator += instruction[1]
        instruction_position += 1
    elif instruction[0] == "jmp":
        instruction_position += instruction[1]
    else:
        instruction_position += 1

    if instruction_position not in instruction_positions:
        instruction_positions.append(instruction_position)
    else:
        print accumulator
        exit(0)













