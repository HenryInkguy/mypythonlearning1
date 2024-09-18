# Challenge 034
# Make a script that reads the salary of a worker and calculates their raise.
# For salaries above R$1250,00, calculate a raise of 10%.
# For lower, the raise is 15%

wage = float(input("Hmm, we are making a research to know what percentage you'll get for a raise, and the final price of course. So we need to know, what's your salary in reais?\n"))

if wage <= 1250.00:
    print(f"Good, supposedly you'll get a 15% percent raise, so your new salary will be around R${(wage + (wage * 15 / 100)):.2f}")

elif wage > 1250.00:
    print(f"Good, supposedly you'll get a 10% percent raise, so your new salary will be around R${(wage + (wage * 10 / 100)):.2f}")
