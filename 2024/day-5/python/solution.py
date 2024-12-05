# So. This problem's input has two parts.
# The first part is a set of "page ordering rules" which basically says that if both of these page numbers are present in an "update" one MUST be before the other.
# The second part is a set of "updates" which we'll actually iterate thru to find if it complies with the aforementioend "page ordering rules"
# The answer of the puzzle is the sum of the middle page numbers of all complying updates.

import random


def firstHalf():
    total = 0
    rules = {}
    file = open("2024/day-5/python/input.txt", "r")
    readingRules = True
    for line in file:
        if (readingRules):
            tmp = line.split("|")
            if len(tmp) == 1:
                readingRules = False
                print(rules)
                continue
            if int(tmp[1]) in rules:
                rules[int(tmp[1])].append(int(tmp[0]))
            else:
                rules[int(tmp[1])] = [int(tmp[0])]
            continue
        update = list(map(int, line.split(",")))
        abides = True
        
        print(update)
        for i in range(len(update)-1):
            if update[i] not in rules:
                rules[update[i]] = []
            if (len([(e) for e in update[i+1:] if (e) in rules[update[i]]]) > 0 ):
                abides = False
                break
        if (abides):
            total += int(update[len(update) // 2])
    print(total) #7198 let's gooo
            
# ok part two is just evil...
# i refuse to comply and will just get silly now
# ok nvm shuffling the list is insane and i thought it wouldn't take that long. wrong.
# i'll take a break to work on some other stuff and come back to this    

def getMiddleFromForcedAbide(update, rules):
    abides = False
    while (not abides):
        random.shuffle(update)
        for i in range(len(update)-1):
            if update[i] not in rules:
                rules[update[i]] = []
            if (len([(e) for e in update[i+1:] if (e) in rules[update[i]]]) > 0 ):
                abides = False
                break
    return int(update[len(update) // 2])
    
  
def secondHalf():
    total = 0
    rules = {}
    file = open("2024/day-5/python/input.txt", "r")
    readingRules = True
    for line in file:
        if (readingRules):
            tmp = line.split("|")
            if len(tmp) == 1:
                readingRules = False
                #print(rules)
                continue
            if int(tmp[1]) in rules:
                rules[int(tmp[1])].append(int(tmp[0]))
            else:
                rules[int(tmp[1])] = [int(tmp[0])]
            continue
        update = list(map(int, line.split(",")))
        abides = True
        
        #print(update)
        for i in range(len(update)-1):
            if update[i] not in rules:
                rules[update[i]] = []
            if (len([(e) for e in update[i+1:] if (e) in rules[update[i]]]) > 0 ):
                abides = False
                break
        if (abides):
            continue    
        else:
            total += getMiddleFromForcedAbide(update, rules)
            print("ding!")
    print(total)
    
secondHalf()