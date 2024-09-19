# Challenge 040
# Build an application that reads two grades of a student and calculates its mean, showing a message at the end, according to the average achieved:
# Average below 5 = Failed. Average above 7 = Approved. Average between 5 and 6.9 = Summer School.

gradeA = float(input("Tell me your grade of last semester: "))
gradeB = float(input("Now your grade of this semester: "))
average = (gradeA + gradeB) / 2

if average < 5:
    print(f"Uh... really? Only {average:.1f} of average grades? Sorry, but you failed.")

elif average >= 5 and average < 7:
    print(f"Yeah, okay, {average:.1f} of average isn't so bad, but you will have to attend summer school.")

elif average > 7:
    print(f"Oh good, you're totally approved, {average:.1f} of average grades is pretty neat. Good job.")