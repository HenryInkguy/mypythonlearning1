# Challenge 052
# Make a script that reads a number and tells if it is a prime number or not.

import color_chart as c
from time import sleep as s
from math import sqrt


def is_prime():
    
    number = int(input(f"{c.color['cyan']}{c.text['itallic']}Type a number that you want to check if its prime or not: {c.color['lilac']}"))
    
    prime_number = True
    
    for n in range(2,number-1):
        if (number % n) == 0:
            
            prime_number = False
            break
    
    
    if prime_number == False:
    
        print(f"{c.color['yellow']}{c.text['bold']}The number you typed, {c.color['cyan']}{number}{c.color['red']}, is not a prime number.{c.text['clear']}")
    
    elif prime_number == True:
        print(f"{c.color['yellow']}{c.text['bold']}The number you typed, {c.color['cyan']}{number}{c.color['green']}, is a prime number.{c.text['clear']}")


is_prime()
    