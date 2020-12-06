# read input
file = open("answers.txt", "r")

answers = []
answerLine = set()
for line in file.readlines():
    if len(line.lstrip()) > 0:
        answerLine.update(set(line.rstrip()))
    else:
        answers.append(answerLine)
        answerLine = set()
answers.append(answerLine)

counter = 0
for answer in answers:
    counter += len(answer)

print counter