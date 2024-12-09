decompressed = ""
empty = chr(ord("ア") + ord("レ") + ord("ン")) #アレン - Aren
for i,x  in enumerate(open("2024/day-9/python/input.txt").read()):
    decompressed += (chr(i//2)  if i%2==0 else empty) * int(x)
id = chr(i//2)

def part1(d):
    decompressed = d[:]
    total = 0
    while decompressed[-1] == empty:
            decompressed = decompressed[:-1]
    while empty in decompressed:
        i = decompressed.index(empty)
        decompressed = decompressed[0:i] + decompressed[-1] + decompressed[i+1:-1]
        while decompressed[-1] == empty:
            decompressed = decompressed[:-1]

    for i in range(len(decompressed)):
        total += ord(decompressed[i]) * i
    return total
print(part1(decompressed))

def part2(d):
    decompressed = d[:]
    total = 0
    i = len(decompressed)-1
    for _ in range(ord(id),0,-1):
        i, c = decompressed.find(chr(_)), decompressed.count(chr(_)) 
        e = decompressed.find(empty * c, 0 , i)
        if e != -1:
            decompressed = decompressed[0:e] + chr(_)*c + decompressed[e+c:i] + empty * c + decompressed[i+c:]

    for i in range(len(decompressed)):
        if decompressed[i] == empty:
             continue
        total += (ord(decompressed[i])) * i
    return total


print(part2(decompressed))     
