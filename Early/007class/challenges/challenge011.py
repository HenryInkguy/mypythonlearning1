# Challenge 011
# Make a script that reads the height and width of a wall in meters, calculate its area and the necessary amount of ink to paint it, considerating that each liter of ink paints an area of 2m².

print("Straight to the point here. Let's paint a wall, so I need you to tell me the its height in meters: ", end='')
height = float(input(''))
width = float(input('Now the width, in meters: '))
area = height * width
paintL= area / 2
print(f'The area of that wall is about {area:.1f}m². Considering that each liter of paint covers an area of 2m² of wall, then we will need approximately {paintL}L of paint to cover this entire side of the wall.')