# read input
file = open("numbers.txt", "r")

numbers = []
for line in file.readlines():
    numbers.append(int(line))

i = 0

while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        k = i + 2
        while k < len(numbers):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                exit(0)
            else:
                k += 1
        else:
            j += 1
    else:
        i += 1