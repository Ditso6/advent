# imports
import re

# read input
input_file = open("numbers.txt", "r")

numbers = []
for line in input_file.readlines():
    number = int(re.search("([0-9]*)", line).group())
    if number:
        numbers.append(number)

i = 0
while i < len(numbers) - 1:
    j = i + 1
    sum = numbers[i]
    while j < len(numbers):
        sum += numbers[j]
        if sum == 2089807806:
            print min(numbers[i:j]) + max(numbers[i:j])
            exit(0)
        elif sum > 2089807806:
            break
        j += 1
    i += 1















