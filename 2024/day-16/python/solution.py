import sys
sys.setrecursionlimit(5000)
inputFile = "2024/day-16/python/" + ("sampleInput" if False else "input") + ".txt"
grid = {i+j*1j: x for i,row in enumerate(open(inputFile)) for j,x in enumerate(row.rstrip("\n"))}
cheapestRouteToNodeCost = {i+j*1j: 999999 for i,row in enumerate(open(inputFile)) for j,x in enumerate(row.rstrip("\n"))}
start = [i for i in grid if grid[i]=="S"][0]
end = [i for i in grid if grid[i]=="E"][0]
dirs = [1,-1,1j,-1j]
minCost = 9999999999
bestPaths = []
print(start,end)
def findShortestPath(node : complex, path : set, cost :int, dir: complex):
    global minCost
    global bestPaths
    if grid[node] == "#" or node in path:
        return False
    if cheapestRouteToNodeCost[node] + 1000 < cost: # This really cool optimization turned an unusable program into a slow program! Which is much better than unusable! Adding the + 1000 part makes the optimization worse but allows us to properly take note of some of the best tiles.
        return False
    else:
        cheapestRouteToNodeCost[node] = cost
    path.add(node)
    #print("hey")
    if node == end:
        print("end",end=" ")
        if cost == minCost:
            bestPaths.append(path)
        if cost < minCost:
            minCost = cost
            bestPaths = [path]
            print(cost)
        return True
    for d in dirs:
        findShortestPath(node+d, path.copy(), cost+(1 if dir == d else 1001), d)
    
findShortestPath(start, set(), 0, 1)
print(minCost)
bestTiles = set()
for path in bestPaths:
    bestTiles = bestTiles.union(path)
print(len(bestTiles))