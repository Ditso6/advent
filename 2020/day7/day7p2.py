# imports
import re


# functions
def calculate_bags_child(tree, children):
    counter = 0
    for key, value in children.items():
        counter += int(value) + int(value) * calculate_bags_child(tree, tree[key])
    return counter

# read input
input_file = open("bags.txt", "r")

lines = {}
for line in input_file.readlines():
    split = line.split("contain")

    parent = split[0][:-6]
    number_and_color = re.findall("([?0-9]*)\s([a-z\s]*)bag", split[1])
    children = {}
    for number, color in number_and_color:
        if color.strip() != "no other":
            children.update({color.strip():number})
    lines.update({parent: children})

# 29547
count = calculate_bags_child(lines, lines["shiny gold"])
print count










