# Challenge 055
# Make an application that reads the weight of five people and shows which was the biggest and smallest weight read.

from time import sleep as s
import color_chart as c

def start_function():
    print(f"{c.text['bold']}{c.color['yellow']}So you're in five, I need you to input your weight so I could check and tell the biggest and smallest number...{c.text['clear']}")
    
    def weight_function():
        biggest_weight = float(0)
        smallest_weight = float(699.99)
    
        for n in range(0,5):
            weight = float(input(f"\n{c.color['yellow']}{c.text['itallic']}Input your weight in kg: "))

            if weight > 700:
                print(f"{c.color['red']}{c.text['itallic']}Invalid input, keep yourself honest. Retrying in 5 seconds...{c.text['clear']}")
                s(5)
                weight_function()

            else:

                if weight > biggest_weight:

                    biggest_weight = weight
                
                if weight < smallest_weight:

                    smallest_weight = weight

        print(f"{c.color['yellow']}{c.text['bold']}Okay, the biggest weight of you five is {c.color['cyan']}{biggest_weight:.2f} kg {c.color['yellow']}.\n\nAnd the smallest weight of you five is {c.color['cyan']}{smallest_weight:.2f} kg{c.color['yellow']}.\n\nNot so bad, hm?{c.text['clear']}")

    weight_function()

start_function()

        