# imports
import re

# read input
input_file = open("numbers.txt", "r")


def calculate_sums(numbers):
    sums = set()
    i = 0
    while i < len(numbers) - 1:
        j = i + 1
        while j < len(numbers):
            sums.add(numbers[i] + numbers[j])
            j += 1
        i += 1
    return sums


numbers = []
for line in input_file.readlines():
    number = int(re.search("([0-9]*)", line).group())
    if number:
        numbers.append(number)

position = 25
while numbers[position] in calculate_sums(numbers[position - 25: position]):
    position += 1

print numbers[position]
















