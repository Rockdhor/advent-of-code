input = open("2016/day-1/python/input.txt").read()
print(input)
dir = [0+1j, 1+0j, 0-1j, -1+0j]
d = 0+0j
visited = set([0+0j])
for i in input.split(", "):
    #print(i)
    if i[0] == "R":
        dir = dir[1:] + [dir[0]]
    else:
        dir = [dir[-1]] + dir[:-1]
        #print(dir)
    for j in range(int(i[1:])):
        d += dir[0] * 1
        if d in visited:
            print("found", d, abs(d.real) + abs(d.imag))
        visited.add(d)
    print(i, d, abs(d.real) + abs(d.imag))
print("end",d, abs(d.real) + abs(d.imag))