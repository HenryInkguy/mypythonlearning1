# Challenge 043
# Develop a logic that reads the weight and the height of someone, calculates their BMI and shows his status, according to the data below:
# < 18.5 = Underweight. Between 18.5 and 25 = Normal. Between 25 and 30 = Overweight. Between 30 and 40 = Obesity. Above 40: Morbid Obesity


import color_chart as c

def BMIdef ():
    weight = float(input(f"{c.text['itallic']}Input your weight in kilograms: {c.text['clear']}"))
    height = float(input(f"{c.text['itallic']}Input your height in meters: {c.text['clear']}"))

    if weight >= 650 or height >= 3.00:
        print("INVALID DATA.")
        yesno =  str(input(f"{c.text['bold']}Do you want to try again? (Yes or No): {c.text['clear']}")).strip().lower()

        if yesno == 'yes':
            BMIdef()

        elif yesno == 'no':
            print("Terminating...")
            quit()
    
    else:

        yesno2 = str(input(f"{c.text['itallic']}So {weight:.2f}kg is your weight, and {height:.2f}m your height. {c.text['bold']}Please confirm if this is correct (Yes or No): {c.text['clear']}")).strip().lower()
        if yesno2 ==  'yes':
            BMI = weight / pow(height,2)
            print(f"Your BMI is {BMI:.2f}.")

            if BMI < 18.5:
                print(f"{BMI:.2f} is your Body Mass Index, classified = Underweight.")

            elif BMI >= 18.5 and BMI < 25:
                print(f"{BMI:.2f} is your Body Mass Index, classified = Normal.")

            elif BMI >= 25 and BMI < 30:
                print(f"{BMI:.2f}  is your Body Mass Index, classified = Overweight.")

            elif BMI >= 30 and BMI < 40:
                print(f"{BMI:.2f} is your Body Mass Index, classified = Obesity.")

            elif BMI >= 40:
                print(f"{BMI:.2f} is your Body Mass Index, classified = Morbid Obesity.")

        elif yesno2 == 'no':
            BMIdef()
    
        else:
            print("Terminating...")
            quit()

BMIdef()
