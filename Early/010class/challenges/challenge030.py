# Challenge 030
# Make a script that reads an integer and shows if the number is even or odd.

num = int(input("""Right, here we are again, Wright, scripting simple stuff and well, boring usually, but we need to practice, right?
Right, now tell me a number, integer, but any number, you decide.
Then I will say if the number is even or odd.
                \n\n\033[3mType any number: \033[0m"""))


if (num % 2) == 0:
    print("Your number is even.")

else:
    print("Your number is odd.")


