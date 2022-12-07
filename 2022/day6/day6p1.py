# read input
file = open("stream.txt", "r")

stream = file.readline().rstrip()

position = 0
for i in range(0, len(stream)-4, 1):
    if len(set(stream[i:i+4])) == 4:
        position = i+4
        break
    else:
        None

print(position)
