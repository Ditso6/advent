# functions
def countTrees(slopeLocations, slopeX, slopeY):
    posX = 0
    posY = 0
    counter = 0
    height = len(slopeLocations)
    width = len(slopeLocations[0])
    while posY < height - 1:
        posX = (posX + slopeX) % width
        posY += slopeY
        symbol = slopeLocations [posY][posX]
        if symbol == "#":
            counter += 1
    return counter

# read input
file = open("map.txt", "r")

locations= []
for line in file.readlines():
    locationLine= []
    for symbol in line.rstrip():
        locationLine.append(symbol)

    locations.append(locationLine)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


counter = 1
for slope in slopes:
    counter = counter * countTrees(locations, slope[0], slope[1])

print counter
