# Challenge 038
# Make an application that reads two integer numbers and compare them, showing in the screen a message:
# The first value is bigger. The second value is bigger. There is no bigger value, they're the same.

a = int(input("Type any integer number: "))
b = int(input("Another one: "))

if a > b:
    print(f"{a} is bigger than {b}.")

elif b > a:
    print(f"{b} is bigger than {a}.")

else:
    print("They're the same.")