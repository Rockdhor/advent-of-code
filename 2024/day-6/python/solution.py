import threading
import time

inputFile = "2024/day-6/python/input.txt"
g = [list(line.rstrip("\n")) for line in open(inputFile, "r").readlines()]
grid = g[:]
dict = {
    (0, 1): "U", (1,0) : "R", (0,-1) : "D", (-1, 0) : "L"
}
s = start = (list(map(lambda x: "^" in x, grid)).index(True), grid[list(map(lambda x: "^" in x, grid)).index(True)].index("^"))
dir, dirs = (-1, 0), [(0, 1), (1,0), (0,-1), (-1, 0)]
traversed = []
def turn(dirs):
    newDirs = dirs[:]
    newDirs.append(newDirs.pop(0))
    return newDirs[-1], newDirs

while (True):
    try:
        if start not in traversed:
            traversed.append(start)
        check = grid[start[0] + dir[0]][start[1] + dir[1]]
        if (check == "#"):
            dir, dirs = turn(dirs)
            continue
        start = start[0] + dir[0], start[1] + dir[1]
    except IndexError:
        break

traversed = (traversed)
print(len(traversed)) #pt 1 5067
traversed.pop(0)
def loopCheck(total, i):
    grid = [list(line.rstrip("\n")) for line in open(inputFile, "r").readlines()]
    grid[i[0]][i[1]] = "#"
    start = s
    gridHistory = {}
    dir, dirs = (-1, 0), [(0, 1), (1,0), (0,-1), (-1, 0)]
    while (True):
        try:
            if (start[0] < 0 or start[1] < 0):
                raise IndexError
            if start in gridHistory:
                if dict[dir] in gridHistory[start]:
                        total[i] = 1
                        break
            check = grid[start[0] + dir[0]][start[1] + dir[1]]
            if (check == "#"):
                if start in gridHistory:
                    gridHistory[start].append(dict[dir])
                else:
                    gridHistory[start] = [dict[dir]]
                dir, dirs = turn(dirs)
                continue
            start = start[0] + dir[0], start[1] + dir[1]
        except IndexError:
            total[i] = 0
            break
    
total = {}
for i in traversed:
    threading.Thread(target=loopCheck, args=(total, i)).start()
while (len(total) < len(traversed)):
    time.sleep(.5)
print(sum([total[i] for i in total]))
