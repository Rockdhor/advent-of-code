import os
import shutil
import cv2
import numpy
isSample = False
size, file = ((11,7), "2024/day-14/python/sampleInput.txt") if isSample else ((101,103), "2024/day-14/python/input.txt")
robotPositions = {}
robotVelocities = {}
midpoint = (size[0]//2, size[1]//2)
def part1():
    steps = 100
    quadrants = [0 for i in range(4)]
    for i,line in enumerate(open(file).readlines()):
        robotPositions[i] = (0,0)
        robotVelocities[i] = (0,0)
        position, velocity = line.split(" ")
        position = position.split(",")
        position[0] = int(position[0][2:])
        position[1] = int(position[1])
        velocity = velocity.split(",")
        velocity[0] = int(velocity[0][2:])
        velocity[1] = int(velocity[1])
        robotPositions[i] = ((position[0] + steps*velocity[0]) % size[0], (position[1] + steps*velocity[1]) % size[1])
        robotVelocities[i] = velocity
        x,y = robotPositions[i][0], robotPositions[i][1]
        if (x == midpoint[0] or y == midpoint[1]):
            continue
        if x < midpoint[0]:
            if y < midpoint[1]:
                quadrants[0]+=1
            else:
                quadrants[1]+=1
        else:
            if y < midpoint[1]:
                quadrants[2]+=1
            else:
                quadrants[3]+=1
        print(robotPositions[i])
    for q in quadrants:
        print(q)
    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

def part2():
    folder = "2024/day-14/python/imgDump"
    if os.path.exists(folder) and os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    for step in range(size[0]*size[1]*2):
        grid = numpy.zeros((size[0],size[1]))
        for i,line in enumerate(open(file).readlines()):
            robotPositions[i] = (0,0)
            robotVelocities[i] = (0,0)
            position, velocity = line.split(" ")
            position = position.split(",")
            position[0] = int(position[0][2:])
            position[1] = int(position[1])
            velocity = velocity.split(",")
            velocity[0] = int(velocity[0][2:])
            velocity[1] = int(velocity[1])
            robotPositions[i] = ((position[0] + step*velocity[0]) % size[0], (position[1] + step*velocity[1]) % size[1])
            robotVelocities[i] = velocity
            x,y = robotPositions[i][0], robotPositions[i][1]
            grid[x,y] = 255
        if (step % 101 == 39 or step % 103 == 99):
            cv2.imwrite(f"{folder}/result{step}.png",grid)
        '''
        if (step % 101 == 39 and step % 103 == 99):
            print(step)
            break
        would end up being enough knowing all that we know after seeing all of the images.
        '''
part1()
part2()