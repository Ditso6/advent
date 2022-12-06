# read input

file = open("pairs.txt", "r")

class Section:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlap(self, other):
        for i in range(self.start, self.end+1, 1):
            if range(other.start, other.end+1, 1).__contains__(i):
                return True
            else:
                None
        return False

    def __str__(self):
        return str(self.start) + "-" + str(self.end)


sections = []
for line in file.readlines():
    pairs = line.rstrip().split(',')
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    sections.append((Section(int(pair1[0]), int(pair1[1])), Section(int(pair2[0]), int(pair2[1]))))

overlaps = 0
for section in sections:
    if section[0].overlap(section[1]):
        overlaps += 1
    else:
        None

print(overlaps)
