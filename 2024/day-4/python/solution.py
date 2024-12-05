# This puzzle is essentially a crosswords I suppose?
# I suppose the simple way to go about this is to treat the input as a 2D-Array and then check for a bunch of adjacency.

def firstHalf():
    total = 0
    file = open("2024/day-4/python/input.txt", "r")
    crosswords = [line.rstrip('\n') for line in file]
    for i in range(len(crosswords)):
        for j in range(len(crosswords[i])):
            if (crosswords[i][j]) == "X":
                for k in [
                    [(1,0), (2,0), (3,0)],
                    [(-1,0), (-2,0), (-3,0)],
                    [(0,1), (0,2), (0,3)],
                    [(0,-1), (0,-2), (0,-3)],
                    [(1,1), (2,2), (3,3)],
                    [(-1,-1), (-2,-2), (-3,-3)],
                    [(1,-1), (2,-2), (3,-3)],
                    [(-1,1), (-2,2), (-3,3)]
                    ]:
                        try:
                            
                            if (crosswords[i+k[0][0]][j+k[0][1]] == "M" and
                        crosswords[i+k[1][0]][j+k[1][1]] == "A" and
                        crosswords[i+k[2][0]][j+k[2][1]] == "S"
                        ):
                                if (i+k[0][0] < 0 or i+k[1][0] < 0 or i+k[2][0] < 0 or j+k[0][1] < 0 or j+k[1][1] < 0 or j+k[2][1] < 0):
                                 continue
                                total+=1
                                #print(crosswords[i+k[0][0]][j+k[0][1]]+crosswords[i+k[1][0]][j+k[1][1]]+crosswords[i+k[2][0]][j+k[2][1]], (i+k[0][0],j+k[0][1]), (i+k[1][0],j+k[1][1]), (i+k[2][0],j+k[2][1]))
                                #print(total, i,j,k)
                        except:
                            continue
    print(total) #2447! Nice!

# This was pretty easy but this feels like such a dirty solution? (which gets the job done) I'll be embarassed if I find out there's some much cleaner way to go about this. Which there must be I'm sure.

# Now this second half is essentially the same problem with some really minor tweaks. Actually nvm a few annoying tweaks sounds more accurate.
    
def secondHalf():
    total = 0
    file = open("2024/day-4/python/input.txt", "r")
    crosswords = [line.rstrip('\n') for line in file]
    for i in range(len(crosswords)):
        for j in range(len(crosswords[i])):
            if (crosswords[i][j]) == "A":
                        try:
                            if (
                        [crosswords[i-1][j-1] + crosswords[i+1][j+1], crosswords[i+1][j+1] + crosswords[i-1][j-1], crosswords[i-1][j+1] + crosswords[i+1][j-1], crosswords[i+1][j-1] + crosswords[i-1][j+1]].count("MS") == 2
                        ):
                                if (i+-1 < 0 or j-1 < 0):
                                 continue
                                total+=1
                                #print(crosswords[i+k[0][0]][j+k[0][1]]+crosswords[i+k[1][0]][j+k[1][1]]+crosswords[i+k[2][0]][j+k[2][1]], (i+k[0][0],j+k[0][1]), (i+k[1][0],j+k[1][1]), (i+k[2][0],j+k[2][1]))
                                #print(total, i,j,k)
                        except:
                            continue
    print(total) #1868! Good.

# Both halves were easy but a little bit annoying to write. The fact that when dealing with verticality + goes down and - goes up messes up with my brain a little.

# After booting up Reddit I'm seeing fancier solutions where I can't help but ask why did I not think of em. But hey. Good enough out here.