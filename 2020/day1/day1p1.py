# read input
file = open("numbers.txt", "r")

numbers = []
for line in file.readlines():
    numbers.append(int(line))

i = 0

while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])
            exit(0)
        else:
            j += 1
    else:
        i += 1