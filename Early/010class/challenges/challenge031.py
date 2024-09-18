# Challenge 031
# Make a script that reads the distance of a trip in Km, calculate the price of the ticket, charging R$ 0,50 for each km for trips up to 200km and R$ 0,45 for longer.

dist = int(input("""Oh, yeah, here we are, I don't know exactly how long your trip will take, but I need to know the distance in km to check the value of the tickets.\n
\033[3mInsert the distance in km: \033[0m"""))

if dist >= 200:
    price = 0.45

else:
    price = 0.50

fullp = dist * price

print(f"The amount you'll need to pay in the end is: R${fullp:.2f}")