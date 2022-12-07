# read input
file = open("stream.txt", "r")

stream = file.readline().rstrip()

position = 0
for i in range(0, len(stream)-4, 1):
    marker = set(stream[i:i+4])
    if len(marker) == 4:
        position = i+4
        break
    else:
        None

print(position)
