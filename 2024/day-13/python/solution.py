f = open("2024/day-13/python/input.txt").read().split("\n\n")
def solve(part):
    tokens = 0
    for machine in f:
        machine = machine.split("\n")
        a1, b1 = machine[0].split(",")
        a1, b1 = int(a1[12:]), int(b1[3:])
        a2, b2 = machine[1].split(",")
        a2, b2 = int(a2[12:]), int(b2[3:])
        p1, p2 = machine[2].split(",")
        p1, p2 = int(p1[9:]) + (10000000000000 if part == 2 else 0), int(p2[3:]) + (10000000000000 if part == 2 else 0)
        d = a1*b2 - a2*b1
        dx, dy = (p1 * b2 - a2 * p2), (p1 * b1 - a1 * p2)
        x,y = (abs(dx/d),abs(dy/d))
        if not x.is_integer() or not y.is_integer():
            continue
        tokens += 3*x + y
    print(int(tokens))

for part in [1,2]:
    solve(part)