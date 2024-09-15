# Challenge 015
# Make a script that reads the Kilometer ran by a rental car and the amount of days it was rented. Calculating the price to pay, considering that the car costs U$ 60 per day and U$ 0,15 per Km traveled.

print("I see here you rented a car... right, let's see, the price you need to pay is... well, I don't have access to the records right now",end='')
print("perhaps you could help me there, buddy? How many kilometers did you travel?")
distance = float(input(''))
print("Cool, now, how many days did you rent the car for?")
duration = int(input(''))

dur_total = duration*60 
dis_total = distance*0.15

total_val = dur_total + dis_total

print(f"Right, staying with it for {duration} days and traveling around {distance}km, you need to pay me U$ {total_val:.2f}. Thank you, sir.")