# Challenge 056
# Develop an application that reads, name, age and sex of 4 people, and in the end shows: Average Age of the group | The name of the oldest man. | How many women have less than 20 years.

from time import sleep as s
import color_chart as c

def start_function():
    print(f"{c.color['cyan']}{c.text['itallic']}The application will read the name of 4 people and will in the end show the average age of the group, name of the oldest man, and how many women have less than 20 years.{c.text['clear']}")

    def multi():
        total_age = 0
        oldest = 0

        global women_lower

        women_lower = 0

        global average_age

        average_age = total_age // 4

        for n in range(0,4):

            print(f"{c.color['red']}{c.text['bold']}Subject {c.color['lilac']}{n+1}{c.text['clear']}")

            name = str(input(f"\n{c.color['cyan']}{c.text['itallic']}Input your first name only: {c.color['yellow']}")).strip()

            if name.find(' ') != -1:
                print(f"{c.color['red']}{c.text['itallic']}Invalid output, only the first name without whitespaces please, trying again in 5 seconds...{c.text['clear']}")
                s(5)
                multi()

            age = int(input(f"\n{c.color['cyan']}{c.text['itallic']}Input your age: {c.color['yellow']}"))
            
            total_age += age 

            sex = str(input(f"\n{c.color['cyan']}{c.text['itallic']}Input your sex, (F) or (M): {c.color['yellow']}")).strip().upper()

            if sex == "F" and age < 20:
                
                women_lower += 1

            elif sex == "M" and age > oldest:
                if age > oldest:
                    global oldest_man

                    oldest_man = name

            elif sex != "M" and sex != "F":
                print(f"{c.color['red']}{c.text['itallic']}Invalid output, choose M or F for sex, retrying in 5 minutes... {c.text['clear']}")
                s(5)
                multi()

    multi()

    print(f"""\n{c.color['yellow']}{c.text['bold']}Average Age of the Group: {c.color['cyan']}{average_age}{c.color['yellow']}.\n
Oldest Man in the Group: {c.color['cyan']}{oldest_man}{c.color['yellow']}.
Quantity of Women With Age Below 20: {c.color['cyan']}{women_lower}{c.color['yellow']}.{c.text['clear']}""")
    



start_function()
