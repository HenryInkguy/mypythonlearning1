# Challenge 037
# Make an application that reads any integer number and asks for the user to chose which will be the base of conversion.
# 1- For binary. 2- For octal. 3- For hexadecimal.

print("-=-"*20)
num = int(input("Type any integer number: "))
dec = int(input(f"Good, now tell me if you want to convert {num} into 1- Binary, 2- Octal or 3- Hexadecimal.\n\033[3mType 1, 2 or 3: \033[0m"))
print("-=-"*20)

if dec == 1:
    print(f"The number you typed: {num}. Converting to Binary, it is: {bin(num)}.")

elif dec == 2:
    print(f"The number you typed: {num}. Converting to Octal, it is: {oct(num)}.")

elif dec == 3:
    print(f"The number you typed: {num}. Converting to Hexadecimal, it is: {hex(num)}")

else:
    print("Invalid choice.")
    