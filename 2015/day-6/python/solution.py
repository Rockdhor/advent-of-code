input = open("2015/day-6/python/input.txt").readlines()
part = 2 # 1 for part 1, 2 for part 2
grid = [[False for i in range(1000)] for j in range(1000)] if part == 1 else [[0 for i in range(1000)] for j in range(1000)]
for line in input:
    line=line.split()
    if line[0] == "turn":
        line.pop(0)
    x1, y1 = map(int, line[1].split(","))
    x2, y2 = map(int, line[3].split(","))
    if part == 1:
        if line[0] == "on":
            func = lambda i, j: True
        elif line[0] == "off":
            func = lambda i, j: False
        else:
            func = lambda i, j: not grid[i][j]
    else:
        if line[0] == "on":
            func = lambda i, j: grid[i][j] + 1
        elif line[0] == "off":
            func = lambda i, j: max(grid[i][j] - 1,0)
        else:
            func = lambda i, j: grid[i][j] + 2 
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = func(i, j)
    #print(line)
print(sum([sum(row) for row in grid]))