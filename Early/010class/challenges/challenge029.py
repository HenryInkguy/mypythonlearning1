# Challenge 029
# Makes a script that reads the speed of a car.
# If it is beyond 80km/h, it writes a message saying he was fined
# The fine is around R$ 7,00 per kilometer beyond the limit.

speed = int(input("Well, well, looks like your car is going at some considerable speed, what did it show in the speedometer?\n"))

if speed > 80:
    fine = float((speed - 80) * 7.00)
    print(f"Yeah, sorry buddy but you were overspeeding, I will need to fine you for R${fine:.2f}.")

    print(f"\n\n\033[3mYou lost R${fine:.2f}")

elif speed > 75 and speed < 80:
    print("Driving pretty close to the edge, huh? Be careful, lad, if you ever get to speed up just a little more, someone will need to fine you.")

elif speed <= 30 and speed > 10:
    print("You're going really slow, never thought of speeding up just a bit? Come on, enjoy your ride, lad, have a good one.")
 
elif speed <= 10:
    print("You should speed up just a little more, for safety, at least 30km/h, 40km/h if you want to be like anyone else. Why are you at 10km/h or less in the highway anyways? Freak.")

else:
    print("Great, not overspeeding at all, continue your trip citizen, have a good one.")