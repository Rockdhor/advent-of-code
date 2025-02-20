input = open("2015/day-7/python/input.txt").readlines()
wires = {}
while input:
    line = input.pop(0)
    arg, out = line.strip().split(" -> ")
    arg = arg.split()
    wires[out] = arg
print(wires)
memo = {}
def get_value(wire):
    global memo
    if wire in memo:
        return memo[wire]
    arg = wires[wire]
    if len(arg) == 1:
        memo[wire] = int(arg[0]) if arg[0].isdigit() else get_value(arg[0])
    elif len(arg) == 2:
        memo[wire] = ~(int(arg[1]) if arg[1].isdigit() else get_value(arg[1]))
    else:
        x = int(arg[0]) if arg[0].isdigit() else get_value(arg[0])
        y = int(arg[2]) if arg[2].isdigit() else get_value(arg[2])
        if arg[1] == "AND":
            memo[wire] = (x) & (y)
        elif arg[1] == "OR":
            memo[wire] = (x) | (y)
        elif arg[1] == "LSHIFT":
            memo[wire] = (x) << (y)
        elif arg[1] == "RSHIFT":
            memo[wire] = (x) >> (y)
    return memo[wire]
a = get_value("a")
print(a)
memo = {"b": a}
a = get_value("a")
print(a)
'''
try:
        if len(arg) == 1:
            wires[out] = int(arg[0]) if arg[0].isdigit() else int(wires[arg[0]])
        elif len(arg) == 2:
            wires[out] = ~(int(arg[1]) if arg[1].isdigit() else int(wires[arg[1]]))
        else:
            x = int(arg[0]) if arg[0].isdigit() else int(wires[arg[0]])
            y = int(arg[2]) if arg[2].isdigit() else int(wires[arg[2]])
            match arg[1]:
                case "AND":
                    wires[out] = (x) & (y)
                case "OR":
                    wires[out] = (x) | (y)
                case "LSHIFT":
                    wires[out] = (x) << (y)
                case "RSHIFT":
                    wires[out] = (x) >> (y)
        if wires[out] < 0:
            wires[out] = 65536 + wires[out]
    except KeyError:
        input.append(line)
'''