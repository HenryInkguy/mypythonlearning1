# Challenge 023
# Make a script that reads a number between 0 and 9999 and shows and shows each one of the digits separated.

number = int(input("Oh, hey, another project we are doing. Then, type a number between 0 and 9999, I will show you each digit of it.\n"))


print(f"""The number you chose is {number}, good, now I will show you each digit:
Ones: {number // 1 % 10}
Tens: {number // 10 % 10}
Hundreds: {number // 100 % 10}
Thousands: {number // 1000 % 10}""")
