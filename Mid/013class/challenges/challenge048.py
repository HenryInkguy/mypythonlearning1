# Challenge 048
# Make a script that shows the sum of all the odd numbers that are multiples of 3 and that are between 1 and 100.

import color_chart as c
from time import sleep as s

global odd_function
global start_function

global odd_quantity
odd_quantity = 0

def odd_function():
    global odd_quantity
    
    if odd_lace % 2 != 0:
        if (odd_lace % 3) == 0:
            odd_quantity += 1
            
def start_function():
    global odd_lace
    for odd_lace in range(1,100):
        odd_function()
    
    print(f"{c.color['yellow']}{c.text['itallic']}The quantity of odd numbers that are multiples of {c.color['blue']}3{c.color['yellow']} is: {c.color['cyan']}{c.text['bold']}{odd_quantity}{c.text['clear']}")

start_function()

s(20)
    