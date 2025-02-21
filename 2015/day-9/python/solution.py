input = open("2015/day-9/python/input.txt").readlines()
distances = {}
for line in input:
    a, _, b, _, distance = line.strip().split()
    distances[a, b] = distances[b, a] = int(distance)
cities = set()
for a, b in distances:
    cities.add(a)
    cities.add(b)
def visitAllMin(city, remainingCities):
    if not remainingCities:
        return 0
    return min(
        distances[city, nextCity] + visitAllMin(nextCity, remainingCities - {nextCity})
        for nextCity in remainingCities
    )

def visitAllMax(city, remainingCities):
    if not remainingCities:
        return 0
    return max(
        distances[city, nextCity] + visitAllMax(nextCity, remainingCities - {nextCity})
        for nextCity in remainingCities
    )
print(min(visitAllMin(city, cities - {city}) for city in cities))
print(max(visitAllMax(city, cities - {city}) for city in cities))