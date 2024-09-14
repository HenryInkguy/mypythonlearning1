# Challenge 008
# Make a script that reads a value in meters and shows it converted in centimeters and milimeters.

print("Our deal tonight is to deal with area, so type me a value in meters and I will show you how much it is converted in centimeters and milimeters. Here you go:", end=' ')
met = int(input(''))
cent = met * 100
mili = met * 1000

print(f"Let's check if it's alright, you typed {met} m, the result in centimeters is about {cent} cm, and in milimeters it is about {mili} mm. Quite easy, right?")