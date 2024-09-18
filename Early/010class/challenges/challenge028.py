# Challenge 028
# Make a script that thinks in a number between 0 and 5 and asks to the user to try finding out what number it really was.
# The software needs to show in the terminal if the user won or lost.

from random import randint as r

num = r(0,5)

print("Hello, RNG Guesser, want to play today?\n")
maybe = str(input("\033[3mYES OR NO?\033[0m\n")).strip().lower()

if maybe == "yes":
    print("Great, you need to guess the number I am thinking, between 0 and 5, I will tell you if you've won or lost after that.\n")
    guess = int(input("\033[3mCome on, remember, it needs to be an integer, between 0 and 5: \033[0m"))

    if guess == num:
        print(f"\033[3mCongratulations!\033[0m You guessed it right on the spot! It's {num}! Never thought you'd guess, despite the odds being very clear.\n")
    
    elif guess > 5 or guess < 0:
        print(f"\033[3mThat's... not what I asked for, anyways, it was supposed to be a number between 0 and 5, you chose {guess}, clearly, it was different from mine, {num}.\033[0m")


    else:
        print(f"\033[3mAw... sorry buddy...\033[0m the number you chose was {guess}, while the one I chose was {num}, but don't worry, it was close, well, see you later, have a good one!")


else:
    print("Okay I guess, talk to you later then.")