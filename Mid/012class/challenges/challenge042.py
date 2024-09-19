# Challenge 042
# Remake the Challenge 035 (Find out if its possible to make a triangle with 3 straight lines of certain length.), adding the feature to show what kind of triangle it is:
# Equilateral / Isosceles / Scalene

import color_chart as c

stline1 = float(input(f"{c.text['itallic']}Input a length for a straight line: "))
stline2 = float(input(f"Another one: "))
stline3 = float(input(f"Last one: {c.text['clear']}"))
istriangle = False

if (stline1 + stline2 > stline3) and (stline2 + stline3 > stline1) and (stline1 + stline1 > stline2):
    istriangle = True

if istriangle == True:
    if stline1 != stline2 != stline3:
        print("Scalene Triangle.")
    elif stline1 == stline2 == stline3:
        print("Equilateral Triangle.")
    elif stline1 == stline2 or stline2 == stline3 or stline1 == stline3:
        print("Isosceles Triangle.")
    
else: 
    print("Not a triangle.")