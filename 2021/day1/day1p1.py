# read input
file = open("depths.txt", "r")

depths = []
for line in file.readlines():
    depths.append(int(line))

i = 0

previous = 0
increases = 0

while i < len(depths):
    if previous < depths[i]:
        increases += 1

    previous = depths[i]
    i += 1

print increases - 1
