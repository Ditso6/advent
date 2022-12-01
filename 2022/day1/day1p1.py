# read input
file = open("calories.txt", "r")

i = 1
maxCalories = 0
calories = {}
for line in file.readlines():
    if line.strip():
        calories[i] = calories.setdefault(i, 0) + int(line)
    else:
        if calories[i] > maxCalories:
            maxCalories = calories[i]
        i += 1


print(maxCalories)