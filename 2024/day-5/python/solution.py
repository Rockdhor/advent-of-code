# Ok so after reading up reddit for a bit I decided that I wanted to go for a cleaner approach, so: (my approach was nasty and was overcomplicating the second half, or maybe I couldn't think of a proper way to brute force it)
from functools import cmp_to_key

file = open("2024/day-5/python/input.txt", "r").read().split("\n\n")
rules = set(file[0].split("\n"))
orders = [line.split(",") for line in file[1].split("\n")]

def comp(x, y):
    return -1 if f"{x}|{y}" in rules else 0

def sortedPages(orders):
    return sorted(orders, key = cmp_to_key(comp))

def middlePage(pages):
    return int(pages[len(pages) // 2])

print(sum(middlePage(p) for p in orders if sortedPages(p) == p)) #PT 1 - 7198 again, good
print(sum(middlePage(sortedPages(p)) for p in orders if sortedPages(p) != p)) #PT 2 - 4230 checks out

# I've been liking taking the most braindead approach possible for each puzzle however it seems like it takes the same amount of time if I just think of a better approach
# I was stuck as to how to tweak my second half for a bit so I think from this point forward I'll go for cleaner solutions.