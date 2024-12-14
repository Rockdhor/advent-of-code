garden = {i+j*1j: x for i,row in enumerate(open("2024/day-12/python/input.txt")) for j,x in enumerate(row.rstrip("\n"))}
regionMap = {}
regionMembers = {}
regionSides = {}
regionID = 0
total1 = total2 = 0
def assignRegion(plant, plot, regionID):
    if plot in regionMembers[regionID]:
        return 0
    if plot not in garden or plot in regionMap or garden[plot] != plant:
        return "wall"
    regionMap[plot] = regionID
    regionMembers[regionID].add(plot)
    perimeter = 0
    for d in [1,-1,1j,-1j]:
        p = assignRegion(garden[plot], plot + d, regionID)
        if p == "wall":
            regionSides[d][plot] = plant
            perimeter+=1
            continue
        perimeter += p
    return perimeter

def assignSides(plot, dir, sideId):
    if plot not in regionSides[dir] or plot in sidesMap or plot not in regionSides[dir]:
        return
    sidesMembers[sideId].add(plot)
    sidesMap[plot] = sideId
    for d in [1,-1,1j,-1j]:
        assignSides(plot + d, dir, sideId)
    return
for plot in garden:
    perimeter = 0
    if plot in regionMap:
        continue
    regionMembers[regionID] = set([plot])
    regionSides = {1 : {},  
                             -1: {}, 
                             1j:{}, 
                             -1j:{}}
    regionMap[plot] = regionID
    for d in [1,-1,1j,-1j]:
        p = assignRegion(garden[plot], plot + d, regionID)
        if p == "wall":
            regionSides[d][plot] = garden[plot]
            perimeter+=1
            continue
        perimeter += p
    
    totalSides = 0
    for dir in [1,-1,1j,-1j]:
        sidesMembers = {}
        sidesMap = {}
        sideId = 0
        for plot in regionSides[dir]:
            if plot in sidesMap or plot not in regionSides[dir]:
                continue
            sidesMembers[sideId] = set([plot])
            sidesMap[plot] = sideId
            for d in [1,-1,1j,-1j]:
                assignSides(plot + d, dir, sideId)
            sideId += 1
        totalSides+=len(sidesMembers)
    total1 += len(regionMembers[regionID]) * perimeter
    total2 += len(regionMembers[regionID]) * totalSides 
    regionID+=1

print(total1)
print(total2)