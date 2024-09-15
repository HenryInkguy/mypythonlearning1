# Challenge 018
# Make a script that reads an angle and shows in the terminal the sine, cosine and tangent values of that angle.

from math import sin, cos, tan, radians

print('Oh hello, this math problems really suck, right? Do not worry there is only two more left, let us just finish this already.')
angle = int(input("First of all, tell me the angle you need to know the sine, cossine and tangent of, I will just make the math calculations: "))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))


print(f"Here you go, since the angle you chose is {angle}°.\nThe sine of it is about {sin:.2f}°.\nThe cossine of it is about {cos:.2f}°.\nThe tangent of it is about {tan:.2f}°.\n\nEasy stuff.")
