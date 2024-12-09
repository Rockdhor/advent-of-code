from itertools import combinations
inputFileString = "2024/day-8/python/input.txt"
inputFile = open(inputFileString).readlines()
antennaes,antinodes = {},set()
for y, row in enumerate(inputFile):
    for x, c in enumerate(row.rstrip("\n")):
        if c != ".":
            if c not in antennaes:
                antennaes[c] = [(y,x)]
            else:
                antennaes[c].append((y,x))

# pt1
                
for i in antennaes:
        for j in (list(combinations(antennaes[i],2))):
            dy, dx = j[1][0]- j[0][0], j[1][1] - j[0][1]
            lAntinode , rAntinode = (j[0][0] - dy, j[0][1] - dx), (j[1][0] + dy, j[1][1] + dx)
            if not (lAntinode[0] < 0 or lAntinode[1] < 0 or lAntinode[0] > len(row)-1 or lAntinode[1] > len(row)-1): 
                antinodes.add(lAntinode)
            if not (rAntinode[0] < 0 or rAntinode[1] < 0 or rAntinode[0] > len(row)-1 or rAntinode[1] > len(row)-1): 
                antinodes.add(rAntinode)
print(len(antinodes))

# pt2

for i in antennaes:
        for j in (list(combinations(antennaes[i],2))):
            dy, dx = j[1][0]- j[0][0], j[1][1] - j[0][1]
            lAntinode , rAntinode = (j[0][0] , j[0][1] ), (j[1][0] , j[1][1])
            while not (lAntinode[0] < 0 or lAntinode[1] < 0 or lAntinode[0] > len(row)-1 or lAntinode[1] > len(row)-1): 
                antinodes.add(lAntinode)
                lAntinode = (lAntinode[0] - dy, lAntinode[1] - dx)
            while not (rAntinode[0] < 0 or rAntinode[1] < 0 or rAntinode[0] > len(row)-1 or rAntinode[1] > len(row)-1): 
                antinodes.add(rAntinode)
                rAntinode = (rAntinode[0] + dy, rAntinode[1] + dx)
print(len(antinodes))