# Challenge 036
# Make a script to approve a bank loan for the purchase of a house. The application will ask the value of the house, the salary of the buyer and how many years he will pay.
# Calculate the monthly installment, knowing that it can't excede 30% of the salary or then the loan will be denied.

from time import sleep as w

print("You're the one wanting a bank loan, hm? Ok, I will need to know your wage, for how many years you're intending to be paying for it, and the value of the house you want.")
w(2)
print("\033[3m...Typing noises...\033[0m")
w(2)

wage = float(input("Good, first your wage: "))
house = float(input("Now the house full value: "))
time = int(input("How many years you're expecting to be paying for it: "))
exceed = wage * 30 / 100
monIn = float(house / (time*12))

print(f"Good, so having your data... a wage of U${wage:.2f}, the value of the house being U${house:.2f} and the time you plan to be paying being {time} years... it will be around U${monIn:.2f} every month.")

if monIn > exceed:
    print(f"I can't accept that deal, sorry. The monthly installments of U${monIn:.2f} can't exceed 30% of your wage, that is U${exceed:.2f}.")

elif monIn < exceed:
    print(f"Good, we have a deal.")
    