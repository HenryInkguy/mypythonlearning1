# Challenge 045
# Create an application that plays Rock, Paper and Scissors with you.

import color_chart as c
from time import sleep as t
from random import randint as r

def rps():
    ropasc = str(input(f"{c.text['itallic']}Let's play rock paper and scissors, what choose yours first and we will see who'd win.\n(R) for Rock\n(P) for Paper\n(S) for Scissors\nChoose: {c.text['clear']}")).strip().lower()
    rpsbot = "Rock","Paper","Scissors"
    rpsint = r(1,3)

    def agg():
        again = str(input("Want to play again?\n(Yes) or (No):")).strip().lower()
        if again == 'yes':
            print(f"")
            rps()

        elif again == 'no':
            print("Terminating code...")
            exit()

        else:
            print("Invalid input, starting over...")
            t(5)
            agg()
        
    def rock():

        if rpsint == 1 and ropasc == ("r"):
            print()

        elif rpsint == 1 and ropasc == ("p"):
            print()

        elif rpsint == 1 and ropasc == ("s"):
            print("")

        else:
            print("Invalid input, starting over in 5 seconds...")
            t(5)
            rps()

    def paper():
        if rpsint == 2 and ropasc == ("r"):
            print()

        elif rpsint == 2 and ropasc == ("p"):
            print()

        


   
'''  if rpsint == 1:
        print(f"You chose ({ropasc.capitalize}), and I chose ({rpsbot[1]}) so... ", end='')
        if ropasc == "rock":
            print(f"its a draw.")
            t(5)
            agg()


        elif ropasc == "scissors":
            print(f"I lost...")
            t(5)
            agg()

        elif ropasc == "paper":
            print(f"I won!")
            t(5)
            agg()


    
    elif rpsint == 2:
        print(f"You chose ({ropasc.capitalize}), and I chose ({rpsbot[2]})so... ", end='')

    
    elif rpsint == 3:
        print(f"You chose ({ropasc.capitalize}), and I chose ({rpsbot[3]})so... ", end='')

rps() '''