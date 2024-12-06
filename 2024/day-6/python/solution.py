grid = open("2024/day-6/python/input.txt", "r").read().splitlines()
start = (list(map(lambda x: "^" in x, grid)).index(True), grid[list(map(lambda x: "^" in x, grid)).index(True)].index("^"))
dir, dirs = (-1, 0), [(0, 1), (1,0), (0,-1), (-1, 0)]
traversed = []
def turn(dirs):
    dirs.append(dirs.pop(0))
    return dirs[-1], dirs

while (True):
    try:
        traversed.append(start)
        check = grid[start[0] + dir[0]][start[1] + dir[1]]
        
        if (check == "#"):
            dir, dirs = turn(dirs)
        start = start[0] + dir[0], start[1] + dir[1]
    except IndexError:
        break

print(len(set(traversed))) #5067