input = open("2015/day-8/python/input.txt").readlines()
sum = 0
for line in input:
    sum += len(line.strip()) - len(eval(line))
print(sum)
sum = 0
for line in input:
    val = 2 - len(line.strip())
    line = list(line.strip())
    while line:
        c = line.pop(0)
        match c:
            case '"':
                val += 2
            case "\\":
                if line[0] == "x":
                    line.pop(0)
                    line.pop(0)
                    line.pop(0)
                    val += 3
                val += 2
            case _:
                val += 1
    sum += val  
print(sum)
