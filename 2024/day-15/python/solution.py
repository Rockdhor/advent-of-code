pt = 2 # 1 | 2
inputFile = "2024/day-15/python/" + ("sampleInput" if False else "input") + ".txt"
print(inputFile)
grid, steps = open(inputFile).read().split("\n\n")
if pt != 1:
    nGrid = ""
    for row in grid:
        for col in row:
            match col:
                case "#":
                    nGrid += "##"
                case "O":
                    nGrid += "[]"
                case ".":
                    nGrid += ".."
                case "@":
                    nGrid += "@."
                case "\n":
                    nGrid += "\n"
    grid = nGrid
grid = {i+j*1j: x for i,row in enumerate(grid.split("\n")) for j,x in enumerate(row.rstrip("\n"))}
translate = {"v" : 1, "^" : -1, ">" : 1j, "<":-1j}

def part1():
    def push(body, direction):
        match grid[body+translate[direction]]:
            case "O":
                if push(body+translate[direction], direction):
                    grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                    return True
                return False
            case "#":
                return False
            case _:
                grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                return True
    for step in steps:
        if step == "\n":
            continue
        robot = [i for i in grid if grid[i]=="@"][0]
        push(robot, step)
    total = 0
    for i in grid:
        if grid[i] == "O":
            total+= 100*i.real + i.imag
    print(total)
def part2():
    def safePush(body,direction):
        match grid[body+translate[direction]]:
                case "[":
                    if safePush(body+translate[direction], direction) and safePush(body+translate[direction] + 1j, direction):
                        return True
                    return False
                case "]":
                    if safePush(body+translate[direction], direction) and safePush(body+translate[direction] + - 1j, direction):
                        return True
                    return False
                case "#":
                    return False
                case _:
                    return True
    def push(body, direction, safe = False):
        if direction in ["<", ">"]:
            match grid[body+translate[direction]]:
                case "[":
                    if push(body+translate[direction], direction):
                        grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                        return True
                    return False
                case "]":
                    if push(body+translate[direction], direction):
                        grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                        return True
                    return False
                case "#":
                    return False
                case _:
                    grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                    return True
        else:
            match grid[body+translate[direction]]:
                case "[":
                    if (not safe):
                        if not (safePush(body+translate[direction], direction) and safePush(body+translate[direction] + 1j, direction)):
                            return False
                    if push(body+translate[direction], direction, safe = True) and push(body+translate[direction]+1j, direction, safe = True): 
                        grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                        return True
                    return False
                case "]":
                    if (not safe):
                        if not (safePush(body+translate[direction], direction) and safePush(body+translate[direction] + -1j, direction)):
                            return False
                    if push(body+translate[direction], direction, safe = True) and push(body+translate[direction]+-1j, direction, safe = True):
                        grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                        return True
                    return False
                case "#":
                    return False
                case _:
                    grid[body], grid[body+translate[direction]] = grid[body+translate[direction]], grid[body]
                    return True
    for step in steps:
        if step == "\n":
            continue
        robot = [i for i in grid if grid[i]=="@"][0]
        push(robot, step)
    total = 0
    for i in grid:
        if grid[i] == "[":
            total+= 100*i.real + (i.imag)
    print(int(total))

if pt == 1:
    part1()
else:
    part2()