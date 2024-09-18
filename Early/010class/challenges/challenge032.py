# Challenge 032
# Make a program that reads any year and shows if the year is leap year

acyear = int(input("\033[3mInput a year: \033[0m"))

# Talk to me while we code together. Maybe in suggestions while I am writing a print or input code.

if acyear % 4 == 0 and acyear % 100 != 0 or acyear % 400 == 0:
    leapy = True

else:
    leapy = False

if leapy == True:
    print("The your you chose is a leap year.")

else:
    print("The year you chose isn't a leap year.")