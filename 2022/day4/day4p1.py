# read input

file = open("pairs.txt", "r")

class Section:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def superSetOf(self, other):
        if self.start <= other.start and self.end >= other.end:
            return True
        else:
            return False

    def __str__(self):
        return str(self.start) + "-" + str(self.end)


sections = []
for line in file.readlines():
    pairs = line.rstrip().split(',')
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    sections.append((Section(int(pair1[0]), int(pair1[1])), Section(int(pair2[0]), int(pair2[1]))))

supersets = 0
for section in sections:
    if section[0].superSetOf(section[1]) or section[1].superSetOf(section[0]):
        supersets += 1
    else:
        None

print(supersets)
