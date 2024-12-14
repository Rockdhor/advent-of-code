This one kicked my butt. Hard.
Part 1 was a reasonable challenge but I got there after a bit.
Just perform a BFS, every time you hit can't navigate in a direction, add 1 to the total for the perimeter. It's that simple.

NOW PART 2 WAS A DIFFERENT BEAST.
I'm victim to the same ailment that has been following me since Dec. 1. Sometimes you need to realize you might want to change your solution for part 1 in order to make it easier to work on part 2.

I don't do that.

I simply work with what I already have which isn't necessarily a bad thing but might lead into more work on the long run.

After deciding to tackle part 2 the next day with some proper sleep I was trying to piece my thoughts together and while browsing the aoc subreddit I saw u/Derailed_Dash's explanation of how they tackled it and realized his implementation went on the same direction I was heading towards. So instead of doing a bunch of crazy line checks or whatever I was thinking of I realized that every time I found a wall for the perimeter, I could simply record the position and direction of the wall so I can map them all out then I can do a second BFS to see if these edges are all connected (thus being part of the same singular side).

Very simple to implement yet I ran into a single error which I found very interesting. To sum it up, the way I was getting the total perimeter worked like this:

On first node, check 4 sides.
If side is a wall (this we know if it's out of bounds or a different plant) return 1.
If side is a proper node, then also check the 4 sides of that node, if it's an already navigated node return 0.
Simple! The total number of walls should just map itself out.
Every time a return value of 1 happened we assume it's a wall which will then be used to calculate the total number of sides.
However, if for whatever reason a side returns 1 not because it's a wall but because the sum of checking all 4 of its sides returned 1, it will get falsely marked as a wall. A few regions ended up with a few false positives.
After finding what happened out all I had to do was change the comparison to make sure it's actually a wall. Dirty fix but it worked out.