Part 2 was probably the hardest puzzle up to this point.

I understand how to reverse engineer the input program but I don't know how to find the A value with that.
I also can't seem to pick up patterns good enough.

What I could do however was:
1st - Understand that output length would always be equal or greater as the values for A grew bigger. Meaning we could start our search after the first integer that gives us the appropriate length.
2nd - Understand that the numbers on the left end of the output would complete a cycle before the numbers to their right would move a step. Something like that.

This meant that I could just jump around with really big intervals like let's say 1M, then once I get the right number on the rightmost spot, I can tone the interval down to 100K then get the 2nd rightmost spot right and so on. Do this enough times and you'll be close enough to a point where you can simply check for A values within an interval of 1 and get the answer in no time.

Crazy puzzle.