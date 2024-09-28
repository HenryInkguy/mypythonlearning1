# Challenge 049
# Remake the Challenge 009, showing a number's multiplication table that the user shows, but now using function for()

import color_chart as c

number = int(input(f"{c.color['cyan']}{c.text['itallic']}Input the number you want to see the multiplication table of: {c.text['bold']}{c.color['yellow']}"))

def multiplication_table():
    print("\n")
    print(f"{c.color['green']}=-= {c.text['clear']}"*5)
    print("\n")
    for multiplication in range(1,11):
        print(f"{c.color['yellow']}{c.text['bold']}{number} {c.color['cyan']}x {c.color['red']}{multiplication} {c.color['cyan']}= {c.color['lilac']}{number * multiplication}{c.text['clear']}\n")
    
    print(f"{c.color['green']}=-= {c.text['clear']}"*5)

multiplication_table()