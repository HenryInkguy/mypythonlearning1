# Challenge 019
# Make a script that reads the name of four students and writes the name of a random chosen one.

import random as r
u_input = str(input("Type the names of the four students, separated by commas (,): "))
names = u_input.split(',')
names = [name.strip() for name in names]
ch = r.choice(names)
print(f"The chosen one is: {ch}")

