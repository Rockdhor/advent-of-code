import hashlib
input = open("2015/day-4/python/input.txt").read()

for part in [5,6]:
    out = "really cool placeholder"
    i=-1
    while out[:part] != "0" * part:
        i+=1
        out = hashlib.md5((input + str(i)).encode()).hexdigest()
        
    print(i, out)