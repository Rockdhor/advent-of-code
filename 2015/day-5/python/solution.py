import re
input = open("2015/day-5/python/sampleInput.txt").readlines()

def checkVowels(str):
    return len(set(re.findall("[aeiou]", str))) >= 3
    
def checkDouble(str):
    pass
def checkBlacklist(str):
    pass

for i in input:
    print(i.strip(), checkVowels(i))