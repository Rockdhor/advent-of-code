### First Half
# Puzzle wants you to find how many reports are safe.
# A report is essentially an array of integers called levels.
# A report is safe when both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

def firstHalf():
    unsafeTotal = 0
    total = 0
    file = open("2024/day-2/python/input.txt", "r")
    for line in file:
        total += 1
        report = list(map(int,line.split()))
        print(report)
        diff = report[0] - report[1]
        if (abs(diff) < 1 or abs(diff) > 3):
                unsafeTotal += 1
                print("US")
                continue
        for level in range(2, len(report)):
            newDiff = report[level-1] - report[level]
            if (abs(newDiff) < 1 or abs(newDiff) > 3 or newDiff*diff < 0):
                unsafeTotal += 1
                print("US")
                break
    print(total, unsafeTotal, total-unsafeTotal) #369 was the answer!

# Second half is essentially the same but it adds the idea of a problem dampener.
# If an unsafe report can be made safe by removing a single level, then it will be safe.
# After analyzing a few reports, I came to the following conclusion:
# - When the problem is caused by differing parities or equal levels -> remove left number.
# - When the problem is caused by a high difference -> remove right number.
# I haven't bothered to try and understand why this is the case. This is purely pattern recognition here.
# After removing a level if needed, we should be able to determine if the report is really unsafe.
    
"""
This was an attempt to be efficient about it but I'm running into issues so it is brute forcing time!

def isSafe(report, problem = False):
    if (not problem):
         print(report)
    diff = report[0] - report[1]
    if (abs(diff) < 1 or abs(diff) > 3):
        #print("Branch" if problem + "US")
        return False if problem else isSafe(report[1:], True) or isSafe([report[0]] + report[2:], True)
    for level in range(2, len(report)):
            newDiff = report[level-1] - report[level]
            if (abs(newDiff) < 1 or abs(newDiff) > 3 or newDiff*diff < 0):
                negL = report[:]
                negL.pop(level-1)
                negR = report[:]
                negR.pop(level)
                if (not problem):
                    print(negL, negR)
                return False if problem else isSafe(negL, True) or isSafe(negR, True)
    print("Safe")
    return True # The answer I was geting was 342? I believe?
"""
# Yeah... Just checking for safety on each subset of the report of length n-1 will do the trick. Just check if at least 1 is safe and call it a day.

def isSafe(report, problem = False):
    print(report)
    if (not problem):
        for level in range(len(report)):
            temp = report[:level] + report[level+1:]
            if isSafe(temp, True):
               return True
        return False
    diff = report[0] - report[1]
    if (abs(diff) < 1 or abs(diff) > 3):
        return False
    for level in range(2, len(report)):
            newDiff = report[level-1] - report[level]
            if (abs(newDiff) < 1 or abs(newDiff) > 3 or newDiff*diff < 0):
                return False
    print("Safe")
    return True

def secondHalf():
    safeTotal = 0
    file = open("2024/day-2/python/input.txt", "r")
    for line in file:
        report = list(map(int,line.split()))
        safeTotal += isSafe(report)
    print(safeTotal)

secondHalf()