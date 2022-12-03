# read input
file = open("strategy.txt", "r")

options = ['A','B','C']
mapping = {
    'X' : 'A',
    'Y' : 'B',
    'Z' : 'C'
}
scores = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

score = 0
strategies = []

def mapToStrategy(stratTuple):
    if stratTuple[1] == 'X':
        return options[(options.index(stratTuple[0]) + 2) % 3]
    elif stratTuple[1] == 'Y':
        return options[(options.index(stratTuple[0]))]
    else:
        return options[(options.index(stratTuple[0]) + 1) % 3]


for line in file.readlines():
    strat = tuple(line.split())
    strategies.append((strat[0], mapToStrategy(strat)))

def calculateResult(strategy):
    if strategy[0] == strategy[1]:
        return 3
    elif (options.index(strategy[0]) + 1) % 3 == options.index(strategy[1]):
        return 6
    else:
        return 0

for strategy in strategies:
    score += calculateResult(strategy) + scores[strategy[1]]

print(score)