def calculate_binary_position(row):
    pos = 0
    binary_range = 2 ** (len(row)) - 2

    for place in row:
        binary_range = binary_range / 2
        if place:
            pos += binary_range + 1

    return pos


def calculate_seat_id(boarding_pass):
    row = map(lambda x: x == "B", boarding_pass[0:7])
    col = map(lambda x: x == "R", boarding_pass[7:10])
    return calculate_binary_position(row) * 8 + calculate_binary_position(col)


# read input
input_file = open("boardingpasses.txt", "r")

passes = []
for line in input_file.readlines():
    passes.append(list(line.rstrip()))

seat_ids = []
for boardingPass in passes:
    seat_ids.append(calculate_seat_id(boardingPass))

seat_ids_range = range(872)
for seat_id in seat_ids_range:
    if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
        print seat_id
        exit(0)

