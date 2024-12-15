First half? Cool exercise.
Knowing that whenever you're simulating movement you can simulate the two ends of a surface meeting by simply doing:
looped around position = position after moving % length of surface
And then position after moving is simply position + (speed * steps)

That's all we really need to figure out the solution to part 1. Checking who's in which quadrant and then multiplying is trivial.

NOW PART 2 WAS ANNOYING... for no reason.
The fact that you don't know how a tree is supposed to look makes it so you cant pull some trick to get there.
So I tried to simply print every step out and look at it.
Too slow, doesn't fit in the console properly.
So let's make it into png files instead.
You could look at all of them and that's good enough after around 10k images.
But you could also realized that starting at some number there's a vertical or horizontal pattern happening every n times where n is the height or width of the grid.
Assuming that at some point those converge is correct. That's where the correct answer is.
A little modulo operation or two will make it so you have to see less images.
The right modulo operations will make it so you only have to see the correct answer.

Also a clever way to approach this is to get all of the images and look at the ones with the smallest sizes.
Since the tree has some coherent shape it will get compressed better leading to a smaller file size.