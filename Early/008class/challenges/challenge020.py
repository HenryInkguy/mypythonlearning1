# Challenge 020
# The same person as before required this script, now he wants to randomize the sequence in which his students will present their works.
# So make the script read the name of these four students and choose the random sequence.

import random as r

names = str(input("Type the names of the students that are going to make a presentation, remember to separate the names by a comma (,): "))
sequence = names.split(',')
sequence = [name.strip() for name in sequence]
r.shuffle(sequence)

print(f"Here is the sequence in which they will present their work: {sequence}.")