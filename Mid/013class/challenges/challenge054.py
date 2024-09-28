# Challenge 054
# Script an application that reads the year of birth of seven people and in the end shows how many people still are minor and how many are of legal age.

from time import sleep as s
import color_chart as c
from datetime import date as d

def start_function():
    print(f"""{c.color['blue']}{c.text['itallic']}"First of all, I will need the year of birth of you all. Seven people, right? Good."{c.color['clear']}""")
    
    global minor
    global legal_age
    
    minor = 0
    legal_age = 0
    today = d.today().year
    
    def age_function():
    
        for age in range(0, 7):
            year = int(input(f"{c.text['itallic']}{c.color['lilac']}Input the year of birth: {c.color['green']}"))
            print(f"{c.text['clear']}")
            
            if year < 1900:
                print(f"{c.text['bold']}{c.color['red']}Invalid input, you're definitely not {c.color['cyan']}{today - year}{c.color['red']} years old. Retrying in 5 seconds...{c.text['clear']}")
                s(5)
                age_function()
                
            elif year > today:
                print(f"{c.text['bold']}{c.color['red']}Invalid input, so you're not even born? Haha, very funny... retrying in 5 seconds...{c.text['clear']}")
                s(5)
                age_function()
                
            else:
                if (today - year) < 18:
                    global minor
                    
                    minor += 1
                
                elif (today - year) > 18:
                    global legal_age
                    
                    legal_age += 1
                    
                else:
                    print(f"{c.color['red']}{c.text['clear']}Error... I suggest troubleshooting...{c.text['clear']}")
                    exit()
                    
    
    age_function()
        
    print(f"""{c.color['cyan']}{c.text['itallic']}Good, there are {c.color['lilac']}seven{c.color['cyan']} of you, but only {c.color['yellow']}{legal_age}{c.color['cyan']} are over {c.color['lilac']}eighteen{c.color['cyan']}. Meaning that they're the only ones who can get through, to the other {c.color['yellow']}{minor}{c.color['cyan']} minors, I suggest you just get out of here.{c.text['clear']}""")
    
start_function()

        