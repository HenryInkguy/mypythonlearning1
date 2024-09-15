# Challenge 016 
# Make a script that reads a float number and shows in the terminal only its integer portion.

from math import trunc



fnum = float(input("Type a random float number: "))
inum = trunc(fnum)

print(f"Here you go, as an integer: {inum}")