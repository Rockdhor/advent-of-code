file = (list(map(int, open("2024/day-1/python/input.txt", "r").read().split())))
x,y = sorted(file[::2]), sorted(file[1::2])
print(sum(map(lambda i, j: abs(i-j), x, y)))
print(sum(map(lambda i: abs(i * y.count(i)), x)))

# This is way better. I hate that I didn't go here right away.
# If there's any way to combine the first two lines without being redundant PLEASE LET ME KNOW.
