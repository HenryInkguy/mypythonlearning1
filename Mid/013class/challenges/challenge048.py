# Challenge 048
# Make a script that shows the sum of all the odd numbers that are multiples of 3 and that are between 1 and 500.

import color_chart as c
from time import sleep as s

global odd_function
global start_function

global odd_quantity
odd_quantity = 0
            
def start_function():
    print(f"{c.color['cyan']}{c.text['itallic']}I will show you all the odd numbers that are multiples of {c.color['yellow']}3{c.color['cyan']}, between {c.color['green']}1{c.color['cyan']} and {c.color['green']}100{c.color['cyan']}, and also the sum of them all.\n")
    s(3)
    
    global odd_lace

    def odd_function():
        global odd_quantity
        global odd_sum
        odd_sum = 0

        for odd_lace in range(1,501):
            if odd_lace % 2 != 0:
                    if (odd_lace % 3) == 0:
                        odd_quantity += 1
                        
                        odd_sum += odd_lace

    odd_function()

    print(f"{c.color['yellow']}{c.text['itallic']}The quantity of odd numbers that are multiples of {c.color['blue']}3{c.color['yellow']} is: {c.color['cyan']}{c.text['bold']}{odd_quantity}{c.color['yellow']}. And the sum of all these numbers is: {c.color['lilac']}{odd_sum}{c.color['yellow']}.{c.text['clear']}")

start_function()

s(20)
    
# Guanabara's solution:

'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1'''
