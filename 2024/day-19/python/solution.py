from functools import cache
sample = False
inputFile = "2024/day-19/python/" + ("sampleInput" if sample else "input") + ".txt"
patterns, designs = (open(inputFile).read().split("\n\n"))
patterns = list(map(str.strip,patterns.split(",")))
designs = designs.split("\n")
print(patterns,designs,"\n")

@cache
def canDesign(design, towel=""):
    if not design.startswith(towel):
        return False
    if towel == design:
        return True
    return any([canDesign(design, towel + next) for next in patterns])

@cache
def howDesign(design, towel=""):
    if not design.startswith(towel):
        return 0
    if towel == design:
        return 1
    return sum([howDesign(design, towel + next) for next in patterns])

'''
for design in designs:
    print(f"The {design} {'can' if canDesign(design) else 'cant'} be made ({howDesign(design)}).")
'''
print(f"{list(map(canDesign, designs)).count(True)} designs were made.")
print(f"{sum(list(map(howDesign, designs)))} possible designs")