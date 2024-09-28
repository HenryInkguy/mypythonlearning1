# Challenge 053
# Make a script that reads a sentence and says if its a palindrome, disconsidering the whitespaces.

import color_chart as c
from time import sleep as s

def start_function():
    paltest = str(input(f"{c.color['yellow']}{c.text['itallic']}Input the word you want to check if its a palindrome: {c.text['bold']}{c.color['lilac']}")).strip().lower()
    print(f"{c.text['clear']}")
    
    def palindrome_test():
        for n in range(0, (len(paltest) // 2)):
            check1 = str(paltest[n])
            check2 = str(paltest[-(n+1)])
            
            if check1 != check2:
                print(f"{c.color['red']}{c.text['bold']}Not a palindrome.{c.text['clear']}")
                s(5)
                exit()
            
        print(f"{c.color['green']}It's a palindrome!{c.text['clear']}")
        
    palindrome_test()
    
    
    
start_function()