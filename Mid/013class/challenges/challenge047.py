# Challenge 047
# Make a script that shows in the terminal all the even numbers between 1 and 50.

import color_chart as c


global even_function
global start_function

even_quantity = 0

def even_function():
    global even_var 
    even_var = (even_lace % 2)
    global even_quantity
    if even_var == 0:
        even_quantity += 1
        print(f"{c.color['red']}{c.text['bold']}{c.text['itallic']}{even_lace} ", end='')
    
def start_function():
    global even_lace
    for even_lace in range(1,51):
        even_function()
            
    
    print(f"\n{c.color['green']}{c.text['itallic']}Amount of Even numbers between 1 and 50: {c.color['clear']}{c.text['clear']}{c.color['cyan']}{c.text['bold']}{even_quantity}{c.text['clear']}")
    
start_function()

# Or, Gustavo Guanabara's solution:

'''
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou.')
    '''

