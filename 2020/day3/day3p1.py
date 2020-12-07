# read input
file = open("map.txt", "r")

locations = []
for line in file.readlines():
    locationLine= []
    for symbol in line.rstrip():
        locationLine.append(symbol)

    locations.append(locationLine)

height = len(locations)
width = len(locations[0])

posX = 0
posY = 0
counter = 0
while posY < height - 1:
    posX = (posX + 3) % width
    posY += 1
    symbol = locations [posY][posX]
    if symbol == "#":
        counter += 1

print counter
