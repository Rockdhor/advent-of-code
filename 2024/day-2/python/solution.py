def safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return not (0 in diffs or max(diffs)/min(diffs) < 0 or len(list(filter(lambda x: abs(x) > 3, diffs))) > 0)

reports = list(map(lambda i : list(map(int, i.split())), open("2024/day-2/python/input.txt", "r").readlines()))
print(list(map(safe, reports)).count(True))
print(list(map(lambda r: any([safe(r[:l] + r[l+1:]) for l in range(len(r))]), reports)).count(True))

# This approach is WAY cleaner, makes my previous attempt embarassing.