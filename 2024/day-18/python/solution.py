sample = False
inputFile = "2024/day-18/python/" + ("sampleInput" if sample else "input") + ".txt"
grid = {i+j*1j: "." for i in range(7 if sample else 71) for j in range(7 if sample else 71)}
obstacleMap = []
for line in open(inputFile).readlines():
    line = line.split(",")
    obstacleMap.append(int(line[1]) + int(line[0] )* 1j)
    grid[int(line[1]) + int(line[0] )* 1j] = "#"

print(grid)
for i in range(7):
    for j in range(7):
        print(grid[i+j*1j], end=" ")
    print()

minCost = {}

def pt1(obstacleMap):
    nodes = [(0+0j, 0)]
    seen = set()
    steps = 0
    while nodes:
        node, steps = nodes.pop(0)
        if node == (6+6j if sample else 70+70j):
            return steps
        for d in [1,-1,1j,-1j]:
            peek = node+d
            if peek in grid and peek not in obstacleMap and peek not in seen:
                nodes.append((peek, steps+1))
                seen.add(peek)
def pt2():
    i = 15 if sample else 2990
    blocked = pt1(obstacleMap[:i])
    while blocked != None:
        i+=1
        blocked = pt1(obstacleMap[:i])
        print(i, blocked)
    
        
    return f"{int(obstacleMap[i-1].imag)},{int(obstacleMap[i-1].real)}"

print(pt1(obstacleMap[:12 if sample else 1024]))
print(pt2())