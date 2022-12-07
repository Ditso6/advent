import re

# read input
file = open("input.txt", "r")

stacks = [
    ['D','B','J','V'],
    ['P','V','B','W','R','D','F'],
    ['R','G','F','L','D','C','W','Q'],
    ['W','J','P','M','L','N','D','B'],
    ['H','N','B','P','C','S','Q'],
    ['R','D','B','S','N','G'],
    ['Z','B','P','M','Q','F','S','H'],
    ['W','L','F'],
    ['S','V','F','M','R']
]
instructions = []
for line in file.readlines():
    instructions.append(list(map(int, re.search("move ([0-9]*) from ([0-9]*) to ([0-9]*)", line).groups())))

for instruction in instructions:
    moving = []
    for i in range(0, instruction[0]):
        moving.insert(0,stacks[instruction[1] - 1].pop())
    stacks[instruction[2]-1] += moving

topRow = ''
for stack in stacks:
    topRow += stack[-1]

print(topRow)