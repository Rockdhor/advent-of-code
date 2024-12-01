### First Half
# Problem asks for the sum of the distances between the values of two ordered lists.

# The most straightforward approach for this problem is to simply order the lists then find distance for each pair and add them to a total as we go.

def firstHalf():
    total = 0
    left = []
    right = []
    file = open("2024/day-1/python/input.txt", "r")
    for line in file:
        valuePair = line.split()
        left.append(int(valuePair[0]))
        right.append(int(valuePair[1]))
    left = sorted(left)
    right = sorted(right)
    for i in range(len(left)):
        total += abs(right[i] - left[i])
    print(total) #2344935 is the answer for the given input. We get a gold star!

### Second Half
# This half asks for the similarity score of the two lists.
# I think the quickest way to go about this is to use a dictionary where each ID serves as they and the value is composed of a list with the frequency for the left and the right lists.

def secondHalf():
    total = 0
    dic = {}
    file = open("2024/day-1/python/input.txt", "r")
    for line in file:
        valuePair = line.split()
        if valuePair[0] not in dic:
            dic[valuePair[0]] = [1,0]
        else:
            dic[valuePair[0]][0] += 1
        if valuePair[1] not in dic:
            dic[valuePair[1]] = [0,1]
        else:
            dic[valuePair[1]][1] += 1
    for i in dic:
        total += int(i) * dic[i][0] * dic[i][1]
    print(total) #27647262 is the answer for this input! 
secondHalf()