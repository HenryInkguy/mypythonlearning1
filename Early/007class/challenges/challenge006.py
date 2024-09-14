# Challenge 006
# Make a script that reads a number and shows the double, the triple and the square root of that number.

print("Here we go again, so this challenge includes three new calculations, perfect, so, as the previous one, you say to me a number and I will show the double, the triple, and the square root of it. Here we go:", end=' ')
num = float(input(''))
doub = int(num*2)
trip = int(num*3)
sqrt = num**0.5
sqrt1 = round(sqrt, 2)

# I am a bit lazy so I will only use the modern way to do this stuff. - Ink

print(f"Fine, so you typed the number {num}, the double of it is {doub}, the triple of it is {trip}, and finally, the square root of it is about {sqrt:.2f}. Hope you enjoyed writing this code and... this little line, just talking to myself though.")
