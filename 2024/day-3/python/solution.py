# The problem essentially wants us to find a bunch of "mul" statements in this junk file, then perform a multiplication with the values of those statements.
# Find the statements using regex -> Extract the values -> Multiply -> Add everything

import re
def mul(instruction):
    pair = instruction[4:-1].split(",")
    return int(pair[0]) * int(pair[1])
def firstHalf():
    file = open("2024/day-3/python/input.txt", "r")
    content = file.read()
    total = 0
    for i in re.findall("mul\(\d{1,3},\d{1,3}\)", content):
        total += (mul(i))
    print(total) #174960292

# Second half is the same except that it adds the "do" and "don't" instructions. Every mul instruction found between those two, should be ignored. Nothing too crazy.
# This was too easy! Modifying the original regex was very simple, then it's as simple as only adding to the total while the do flag was true.

def secondHalf():
    file = open("2024/day-3/python/input.txt", "r")
    content = file.read()
    total = 0
    do = True
    for i in re.findall("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", content):
        match i:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if (do):
                    total += (mul(i))
        #print(i, total)
    print(total) #56275602
secondHalf()