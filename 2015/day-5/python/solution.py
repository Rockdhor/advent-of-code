import re
input = open("2015/day-5/python/input.txt").readlines()

def checkVowels(str):
    return len((re.findall("[aeiou]", str))) >= 3
def checkDouble(str):
    for c in range(len(str)-1):
        if str[c] == str[c+1]:
            return True
    return False
def checkBlacklist(str):
    for b in ["ab", "cd", "pq", "xy"]:
        if str.find(b) != -1:
            return False
    return True
def checkRepeatingPair(str):
    for i in range(len(str)-2):
        for j in range(len(str)-2):
            if str[i:i+2] == str[j:j+2]:
                if abs(i-j) > 1:
                    return True
    return False
def checkRepeatingLetterWithSpace(str):
    for i in range(len(str)-2):
        if str[i] == str[i+2]:
            return True
    return False

print([checkVowels(i) and checkDouble(i) and checkBlacklist(i) for i in input].count(True))
print([checkRepeatingPair(i) and checkRepeatingLetterWithSpace(i) for i in input].count(True))