# Challenge 050
# Make a script that reads six integer numbers and shows the sum of only the even numbers, if the value is odd, disconsider it.

import color_chart as c

def every():
    
    def entire_numbers():
        global total
        total = 0
        for count in range(1,7):
            number = int(input(f"{c.color['yellow']}{c.text['itallic']}Input an integer number: {c.color['cyan']}"))
            if number % 2 == 0:
                total += number

    def returnal():
        yesno = int(input(f"{c.color['yellow']}Do you want to try again?\n{c.color['green']}(1) Yes\n{c.color['red']}(2) No\n"))
        if yesno == 1:
            print(f"{c.text['clear']}")
            every()
        
        elif yesno == 2:
            print(f"\n{c.color['lilac']}{c.text['itallic']}Have a nice one!{c.text['clear']}")
            exit()
        
        else:
            print("Invalid input, returning...")
            returnal()
        
    entire_numbers()

    print("\n")
    print(f"{c.color['cyan']}{c.text['bold']}Sum of all even numbers amongst those you typed: {c.color['lilac']}{total}{c.text['clear']}")
    
    returnal()
    
every()
