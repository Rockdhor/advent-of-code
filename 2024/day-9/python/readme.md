My first implementation for pt-1 was done SO quick and it worked perfectly with the sample input.
With the regular input... completely different story.
This lead me to believe the error was with the input somehow, a quick diff check made me realize that was not the case.
After who knows how long I realize that the problem happens with numbers with more than 1 digit being iterpreted as n-numbers of 1 digit.
I quickly tought of using chr() and ord() to fix it. Amazing! Felt so clever even tho it wasn't a big deal.
Still getting the wrong result tho... It took me SO long to realize that "." was not a proper character to use to represent empty blocks since it'll get mistaken as 48 or some low number like that.
Just had to use some character with a huge unicode representation... took me so long to realize this. That's why you have to pay good attention to each step of your program!

Leavint the comments in the solution to serve as battle scars.