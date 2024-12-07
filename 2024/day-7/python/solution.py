inputFileString = "2024/day-7/python/input.txt"
inputFile = open(inputFileString).readlines()

def canCalibrate(goal, factors, concat = False):
    if len(factors) == 1:
        return goal == factors[0]
    return canCalibrate(goal, [factors[0] + factors[1]] + factors[2:], concat) or canCalibrate(goal, [factors[0] * factors[1]] + factors[2:], concat) or (concat and canCalibrate(goal, [int(str(factors[0]) + str(factors[1]))] + factors[2:], concat))

total = 0

for line in inputFile:
    goal, factors = line.split(":")
    goal, factors = int(goal), [*map(int,factors.rstrip("").split())]
    total += goal if canCalibrate(goal,factors, True) else 0

print(total) #PT 1 = 1611660863222 | PT 2 = 945341732469724
#This was quite a simple one. I'm surprised? confused?
#At a simple glance I could optimize with memoization and/or multithreading but it's fast enough that I don't care.