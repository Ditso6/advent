import re

# read input
file = open("passwords.txt", "r")

tuples = []
for line in file.readlines():
    tuples.append(re.search("([0-9]*)-([0-9]*)\s([a-z]):\s([a-z]*)", line).groups())

firstOccurence = 0
secondOccurence = 1
letter = 2
password = 3

correctPasswords = 0
for tuple in tuples:
    if bool(tuple[password][int(tuple[firstOccurence]) - 1] == tuple[letter]) ^ bool(tuple[password][int(tuple[secondOccurence]) - 1] == tuple[letter]) :
        correctPasswords += 1

print(correctPasswords)
