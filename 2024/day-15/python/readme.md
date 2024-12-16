Not the cleanest lines of code but they work and I don't really feel like tidying them up right now.

Part 1 goes like this:
For every step
Is there an empty space in front of robot? Then move there.
Is there a wall in front of robot? Then don't do anything
Is there a box in front of robot? Then ask this and other consecutive boxes the same questions until a wall or empty space is met. The robot and all boxes will share the same behavior, either move in step in a direction or don't move at all.

Part 2 is very similar:
For every step
Is movement horizontal? Act exactly as part 1 dictates.
Is movement vertical not a box in front? Act exactly as part 1 dictates.
Else, check if movement can be performed on both the part of the box right in front of body AND the other part of the box. If everything's good to go then perform the push.

Part 1 was a very straightforward implementation but part 2 took a little bit of playing around and hoping the logic made sense and isn't redundant or something.
