# read input
input_file = open("answers.txt", "r")

answers = []
answer_line = set()
lines = input_file.read().splitlines()
for idx, line in enumerate(lines, 1):
    if not line.strip() or idx == len(lines):
        answers.append(answer_line)
    if line.strip():
        answer_line.update(set(line.rstrip()))
    else:
        answer_line = set()


counter = 0
for answer in answers:
    counter += len(answer)

# 6249
print counter
