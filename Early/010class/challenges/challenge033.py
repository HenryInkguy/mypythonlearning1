# Challenge 033
# Make a script that reads 3 numbers and shows which is the biggest and the smallest.

a = int(input("Write a random integer number: "))
b = int(input("Another one: "))
c = int(input("Last one: "))

if a > b and a > c:
    print(f"{a} is a bigger number than {b} and {c}. So it's the biggest one.")
    
    if b < c:
        print(f"{b} is the smallest number.")

    elif c < b:
        print(f"{c} is the smallest number.")


elif b > a and b > c:
    print(f"{b} is a bigger number than {a} and {c}. So it's the biggest one.")

    if a < c:
        print(f"{a} is the smallest number.")

    elif c < a:
        print(f"{c} is the smallest number.")


elif c > a and c > b:
    print(f"{c} is a bigger number than {a} and {b}. So it's the biggest one.")

    if a < b:
        print(f"{a} is the smallest number.")

    elif b < a:
        print(f"{b} is the smallest number.")

else:
    print("Well... they're all the same.")
