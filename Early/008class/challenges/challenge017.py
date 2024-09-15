# Challenge 017
# Make a script that reads the length of a right triangle's legs and calculates the hypotenuse's lenght.

from math import hypot

print("So here we have a right triangle, can you type for me please, the length of the opposite leg? ", end='')
leg1 = int(input(''))
leg2 = int(input('Now type the length of the adjacent one: '))

hypot = hypot(leg1,leg2)

print(f"The hypotenuse of this right triangle, with one leg being {leg1}cm and the other being {leg2}cm, is {hypot:.2f}cm")
