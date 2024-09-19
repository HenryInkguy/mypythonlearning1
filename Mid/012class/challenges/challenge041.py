# Challenge 041
# The National Swimming Confederation needs an application that reads the year of birth of an athlete and shows his category, according to his age:
# < 9y = Sub-9. til 14y = Sub-14. til 19 = Junior. til 20 = Senior. Above 20 = Master.  

import color_chart as c

age1 = int(input(f"{c.text['itallic']}National Swimming Confederation. Type your year of birth to be set to a swimming category: {c.text['clear']}"))

age = 2024 - age1

if age1 >= 2020:
    print("INVALID YEAR OF BIRTH.")

elif age < 9:
    print("Sub-9 Category.")

elif age > 9 and age <= 14:
    print("Sub-14 Category.")

elif age > 14 and age <= 19:
    print("Junior Category.")

elif age > 19 and age <= 20:
    print("Senior Category.")

elif age > 20:
    print("Master Category.")
