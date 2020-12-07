alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"}

# read input
input_file = open("answers.txt", "r")

answers = []
answer_line = alphabet
lines = input_file.read().splitlines()
for idx, line in enumerate(lines, 1):
    if not line.strip() or idx == len(lines):
        answers.append(answer_line)
    answer_line = answer_line.intersection(set(line.rstrip())) if line.strip() else alphabet

counter = 0
for answer in answers:
    counter += len(answer)

# 3103
print counter