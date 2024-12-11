topoMap = {i+j*1j: int(x) for i,row in enumerate(open("2024/day-10/python/input.txt")) for j,x in enumerate(row.rstrip("\n"))}

def getTrailheadScore(pos, peaks, val=0):
    if pos in topoMap and topoMap[pos] == val:
        if val < 9:
            return (sum(getTrailheadScore(pos+dir, peaks, val+1) for dir in [1,-1,1j,-1j]))
        if pos not in peaks:
            peaks.add(pos)
            return 1
    return 0

def getTrailheadRating(pos, val=0):
    if pos in topoMap and topoMap[pos] == val:
        if val < 9:
            return (sum(getTrailheadRating(pos+dir, val+1) for dir in [1,-1,1j,-1j]))
        return 1
    return 0

print(sum([getTrailheadScore(pos, set()) for pos in topoMap if topoMap[pos] == 0]))
print(sum([getTrailheadRating(pos) for pos in topoMap if topoMap[pos] == 0]))
