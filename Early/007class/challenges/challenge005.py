# Challenge 005
# Make a script that reads an int number and shows its successor and predecessor

print('First of all, this challenge is quite simple, I will read a number and show you its sucessor and predecessor, fine? Okay here we go:', end='')
number = int(input(' '))
# print("Great, now here we go, the number you typed is {}, its sucessor is {} and its predecessor is {}. Easy peasy, don't you think?".format(number,number+1,number-1))

# Modern way to solve it, using 'F': 
# print(f"Great, now here we go, the number you typed is {number}, its sucessor is {number+1} and its predecessor is {number-1}. Easy peasy, don't you think?")


# Another way to go with two more variables.

pred = number - 1
suc = number + 1

#print("Great, now here we go, the number you typed is {}, its sucessor is {} and its predecessor is {}. Easy peasy, don't you think?".format(number,suc,pred))

# Modern way to solve it, using 'F': 
print(f"Great, now here we go, the number you typed is {number}, its sucessor is {suc} and its predecessor is {pred}. Easy peasy, don't you think?")
