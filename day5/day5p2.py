# read input
file = open("boardingpasses.txt", "r")


def calculate_binary(row, addLetter, limit):
    pos = 0
    range = limit
    for place in row:
        range = range / 2
        if place == addLetter:
            pos += range + 1

    return pos


def calculate_seat_id(boardingPass):
    row = boardingPass[0:7]
    col = boardingPass[7:10]
    return calculate_binary(row, "B", 126) * 8 + calculate_binary(col, "R", 6)

passes = []
for line in file.readlines():
    passes.append(list(line.rstrip()))

seat_ids = []
for boardingPass in passes:
    seat_ids.append(calculate_seat_id(boardingPass))

seat_ids_range = range(872)
for seat_id in seat_ids_range:
    if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
        print seat_id
        exit(0)


