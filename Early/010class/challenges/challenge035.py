# Challenge 035
# Make a script that reads the length of three straight lines and says if it can make a triangle.

print("Tell me random lengths for three straight lines, I will then say if you can make a triangle with them.")
a = float(input("Straight Line A: "))
b = float(input("Straight Line B: "))
c = float (input("Straight Line C: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("You can easily make a triangle with these three. Thank you for collaborating with the research.")

else:
    print("No, you can't make a triangle with these. Thank you for collaborating with the research anyways!")

# A remind that you should always be simple and think a lot before making long straight codes.

'''if (a > b and a > c):
    bnum = a
    lnum = b + c

elif (b > a and b > c):
    bnum = b
    lnum = a + c

elif (c > a and c > b):
    bnum = c
    lnum = b + a 

if lnum >= bnum:
    print("You can easily make a triangle with these three. Thank you for collaborating with the research.")
    
else:
    print("No, you can't make a triangle with these. Thank you for collaborating with the research anyways!")'''
