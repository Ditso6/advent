import re

# read input
file = open("passwords.txt", "r")

tuples = []
for line in file.readlines():
    tuples.append(re.search("([0-9]*)-([0-9]*)\s([a-z]):\s([a-z]*)", line).groups())

minOccurence = 0
maxOccurence = 1
letter = 2
password = 3

correctPasswords = 0
for tuple in tuples:
    if int(tuple[minOccurence]) <= tuple[password].count(tuple[letter]) <= int(tuple[maxOccurence]):
        correctPasswords += 1

print(correctPasswords)
