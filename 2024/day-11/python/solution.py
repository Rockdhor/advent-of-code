from collections import defaultdict
memory = defaultdict(int)
for stone in map(int,list(open("2024/day-11/python/input.txt").read().split())):
    memory[stone] += 1

def change(stones):
    tempMemory = defaultdict(int)
    for stone, val in stones.items():
        strStone = str(stone)
        if stone == 0:
            tempMemory[1] += val
            continue
        if len(strStone) % 2 == 0:
            tempMemory[int(strStone[0:(len(strStone)//2)])] += val
            tempMemory[int(strStone[len(strStone)//2:])] += val
            continue
        tempMemory[stone*2024] += val
    return tempMemory

for i in range(75):
    memory = change(memory)
print(sum(memory.values()))