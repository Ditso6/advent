# imports
import re


# functions
def find_child(tree, children, color):
    if color in children:
        return True
    else:
        found_in_children = False
        for child in children:
            found_in_children |= find_child(tree, tree[child],color)
        return found_in_children


# read input
input_file = open("bags.txt", "r")

lines = {}
for line in input_file.readlines():
    split = line.split("contain")

    parent = split[0][:-6]
    children = map(lambda x: x.strip(), re.findall("([a-z\s]*)bag", split[1]))
    children = filter(lambda x: x != "no other", children)
    lines.update({parent: children})

# 370
counter = 0
for parent, children in lines.items():
    if find_child(lines, children, "shiny gold"):
        counter += 1

print counter











