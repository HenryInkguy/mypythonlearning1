# Challenge 045
# Create an application that plays Rock, Paper and Scissors with you.

import color_chart as c
from time import sleep as t
from random import randint as r

def rps():
    ropasc = int(input(f"{c.text['itallic']}Let's play rock paper and scissors, what choose yours first and we will see who'd win.\n(1) for Rock\n(2) for Paper\n(3) for Scissors\nChoose: {c.text['clear']}"))
    rpsbot = "Rock","Paper","Scissors"
    rpsint = r(1,3)

    print(f"{c.text['bold']}")

    def agg():
        t(5)
        again = str(input(f"{c.text['bold']}Want to play again?\n(Yes) or (No): {c.text['clear']}")).strip().lower()
        if again == 'yes':
            print(f"")
            rps()

        elif again == 'no':
            print(f"{c.text['itallic']}Terminating code...{c.text['clear']}")
            exit()

        else:
            print(f"{c.text['itallic']}Invalid input, starting over... {c.text['clear']}")
            t(5)
            agg()
        
    def rock():
        if ropasc == (1):
            print(f"its a draw.{c.text['clear']}")
            agg()

        elif ropasc == (2):
            print(f"I lost... good game.{c.text['clear']}")
            agg()

        elif ropasc == (3):
            print(f"I won! Yes!{c.text['clear']}")
            agg()

        else:
            print(f"Invalid input, starting over in 5 seconds...{c.text['clear']}")
            t(5)
            rps()

    def paper():
        if ropasc == (1):
            print(f"I won! Yes!{c.text['clear']}")
            agg()

        elif ropasc == (2):
            print(f"its a draw.{c.text['clear']}")
            agg()

        elif ropasc == (3):
            print(f"I lost... good game.{c.text['clear']}")
            agg()

        else:
            print(f"Invalid input, starting over in 5 seconds...{c.text['clear']}")
            t(5)
            rps()

    def scissors():
        if ropasc == (1):
            print(f"You have won!{c.text['clear']}")
            agg()
        
        elif ropasc == (2):
            print(f"Bot has won! Yes!{c.text['clear']}")
            agg()

        elif ropasc == (3):
            print(f"Draw!{c.text['clear']}")
            agg()

        else:
            print(f"Invalid input, starting over in 5 seconds...{c.text['clear']}")
            t(5)
            rps()

    if 3 < ropasc < 1:
        print(f"Invalid input, starting over in 5 seconds...{c.text['clear']}")
        t(5)
        rps()

    else:
        print(f"{c.text['itallic']}Rock...\n{t(1)}Paper...\n{t(1)}Scissors!{c.text['clear']}")

        print(f"""{c.text['bold']}{"=-="*10}
Player chose {rpsbot[ropasc+1]}
Bot chose {rpsbot[rpsint]}
{"=-="*10}\n{c.text['clear']}""")

        if rpsint == 1:
            rock()

        elif rpsint == 2:
            paper()

        else:
            scissors()


        
rps()
   