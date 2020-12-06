# import
import re

# read input
file = open("answers.txt", "r")

answers = []
answerLine = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
for line in file.readlines():
    if len(line.lstrip()) > 0:
        answerLine = answerLine.intersection(set(line.rstrip()))
    else:
        answers.append(answerLine)
        answerLine = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
answers.append(answerLine)

counter = 0
for answer in answers:
    counter += len(answer)

print counter