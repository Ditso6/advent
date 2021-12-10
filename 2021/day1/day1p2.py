# read input
file = open("depths.txt", "r")

depths = []
for line in file.readlines():
    depths.append(int(line))

i = 0

increases = 0
previous_window = 0
next_window = 0

while i < len(depths)-2:
    next_window = depths[i] + depths[i+1] + depths[i+2]
    if previous_window < next_window:
        increases += 1

    previous_window = next_window
    i += 1

print increases - 1
