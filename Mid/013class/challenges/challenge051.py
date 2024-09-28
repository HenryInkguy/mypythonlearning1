# Challenge 051
# Make a progression arithmetic where the script reads the first term and the reason/common difference.

import color_chart as c
from time import sleep as s

def start_code():
    global first_term
    global common_difference
    
    first_term = int(input(f"{c.color['red']}{c.text['itallic']}Input the first term: {c.color['lilac']}"))
    common_difference = int(input(f"\n{c.color['cyan']}{c.text['itallic']}Input the common difference: {c.color['lilac']}"))
    print(f"{c.text['clear']}")
    
    def arithmetic():
            term = first_term + (n - 1) * common_difference
            print(f"{c.color['green']}{c.text['bold']}Term {c.color['yellow']}{n}{c.color['green']}: {c.color['blue']}{term}{c.color['green']}.{c.text['clear']}")
    
    def returnal():
        yesno1 = int(input(f"{c.text['bold']}{c.color['yellow']}Do you want to try again?\n{c.color['cyan']}(1) Yes (2) No\n{c.color['lilac']}"))
        
        if yesno1 == 1:
            print(f"{c.text['itallic']}{c.color['green']}Good, retrying code in 3 seconds...{c.text['clear']}")
            s(3)
            start_code()
            
        elif yesno1 == 2:
            print(f"{c.color['red']}{c.text['itallic']}Terminating code...{c.color['lilac']}")
            exit()
            
        else:
            print(f"{c.color['red']}{c.text['itallic']}Wrong input, retrying in 3 seconds...")
            s(3)
            returnal()
            
    global n
    
    print(f"{c.color['blue']}{c.text['bold']}Considering the First Term {c.color['red']}{c.text['itallic']}{first_term}{c.color['blue']}{c.text['bold']} and the Common Difference {c.color['yellow']}{c.text['itallic']}{common_difference}{c.color['blue']}{c.text['bold']}...{c.text['clear']}\n")
    
    for n in range(1,21):
        arithmetic()
    
    s(3)
    print(f"\n{c.color['lilac']}{c.text['itallic']}And so it goes...{c.text['clear']}\n")
    s(5)
        
    returnal()
            
start_code()