# read input
file = open("strategy.txt", "r")

i = 1
maxCalories = 0
calories = {}
for line in file.readlines():
    if line.strip():
        calories[i] = calories.setdefault(i, 0) + int(line)
    else:
        i += 1

sortedCalories = dict(sorted(calories.items(), key=lambda x: x[1], reverse=True))

maxCalories = sum(list(sortedCalories.values())[0:3])

print(maxCalories)