# read input
import string

file = open("rucksacks.txt", "r")

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

compartments = []
for line in file.readlines():
    compartments.append((line.rstrip()[:len(line)//2], line.rstrip()[len(line)//2:]))

print(compartments)
def calcPriority(char):
    if alphabet_lower.find(char) > 0:
        return alphabet_lower.find(char) + 1
    else:
        return alphabet_upper.find(char) + 27

priority = 0
for compartment in compartments:
    for char in compartment[0]:
        if compartment[1].find(char) > -1:
            priority += calcPriority(char)
            break
        else:
            None


print(priority)