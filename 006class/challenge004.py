# Challenge (03)
# Make a script that reads any input and show in the terminal its primitive data structure and all the possible information about it.

b1 = input('Say to me, anything you want, and I will say the primitive data structure it fits, okay? Here we go: ')
print(f"Let's see if what you typed is numeric: {b1.isnumeric()}, right... in case it is, I will check if it's also digits: {b1.isdigit()}, or if it is decimal: {b1.isdecimal()};")
print(f"Cool, now let's check if it is alphabetic: {b1.isalpha()}, if it is written in lower case: {b1.islower()}, or then if it is written in upper case: {b1.isupper()}, or perhaps title case: {b1.istitle()};")
print(f"It only gets even more exciting, not actually, but learning to code is kind of cool, even if you're slow, isn't it? Anyways... I will check if it is alphanumeric: {b1.isalnum()}. I don't know if any got TRUE by now, but anyways, let's check the last thing, if you just... well, typed a blank space: {b1.isspace()}.")

# Second attempt, using conditionals. (dolater)