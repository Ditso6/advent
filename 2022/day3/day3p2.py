# read input
import string

file = open("rucksacks.txt", "r")

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

contents = []
for line in file.readlines():
    contents.append(line.rstrip())

def calcPriority(char):
    if alphabet_lower.find(char) > 0:
        return alphabet_lower.find(char) + 1
    else:
        return alphabet_upper.find(char) + 27

priority = 0
for i in range(0, len(contents)-2,3):
    for char in contents[i]:
        if contents[i+1].find(char) > -1 and contents[i+2].find(char) > -1:
            priority += calcPriority(char)
            break
        else:
            None

print(priority)