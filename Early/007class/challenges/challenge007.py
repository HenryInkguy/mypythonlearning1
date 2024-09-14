# Challenge 007
# Develop a script where it reads two grades of one student and calculates its mean.

print("Okay, I checked here and I need to know your grades from the last two semesters, so input them here and I will show how much is your grade point average. Here:", end=' ')
sem1 = int(input(''),)
sem2 = int(input('Okay, now another one: '))
mean = float((sem1 + sem2) / 2)
meanr = round(mean, 1)

print(f"Okay okay, here's your average: {meanr}, just from the last two semesters though.")
