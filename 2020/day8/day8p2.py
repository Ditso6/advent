# imports
import re

# read input
input_file = open("instruction_set.txt", "r")


def instruction_set_has_end(instruction_set):
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

        if instruction_position == len(instruction_set) - 1:
            return True, accumulator
        if instruction_position >= len(instruction_set) or instruction_position in instruction_positions:
            return False, accumulator

        instruction_positions.append(instruction_position)

instruction_set = []
for line in input_file.readlines():
    instruction = re.search("([a-z]*)\s([-+0-9]*)", line).groups()
    instruction_set.append((instruction[0], int(instruction[1])))

position = 0
previous_instruction_change = ""
previous_instruction_change_position = 0
while not instruction_set_has_end(instruction_set)[0]:
    # restore previous change
    if previous_instruction_change:
        changed_instruction = instruction_set[previous_instruction_change_position]
        instruction_set[previous_instruction_change_position] = (previous_instruction_change, changed_instruction[1])

    instruction = instruction_set[position]
    if instruction[0] == "jmp":
        previous_instruction_change = "jmp"
        previous_instruction_change_position = position
        instruction_set[position] = ("nop", instruction[1])
    elif instruction[0] == "nop":
        previous_instruction_change = "nop"
        previous_instruction_change_position = position
        instruction_set[position] = ("jmp", instruction[1])
    else:
        previous_instruction_change_position = 0
        previous_instruction_change = ""

    position += 1

print instruction_set_has_end(instruction_set)[1]














