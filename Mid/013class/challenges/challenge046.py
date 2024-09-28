# Challenge 046
# Script a program that shows in the terminal a countdown for the fireworks, from 10 to 0, with an interval of 1 second.

from time import sleep as w
import color_chart as c


def fireworks():
    print(f"{c.color['red']}{c.text['itallic']}We are going to launch some fireworks right now! Countdown starting in 3 seconds...{c.color['clear']}{c.text['clear']}")
    w(3)
    
    for countdown in range(0,10):
        print(f"{c.text['bold']}{c.color['yellow']}Launching fireworks in: ", end='') 
        print(f"{c.color['cyan']}{(10 - countdown)}{c.color['clear']}{c.text['clear']}")
        w(1)
    
    print(f"\n{c.color['yellow']}{c.text['itallic']}Woooosh!{c.text['clear']}{c.color['clear']}\n")
    print(f"{c.text['itallic']}{c.color['red']}Geez, that was awesome!")
    
    
fireworks()
