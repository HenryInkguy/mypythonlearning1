# Challenge 025
# Make a script that reads the name of somebody and says if they have "Silva" in it.

name = str(input("Tell me your name so we can finally continue with our little software development: ")).strip()
uppy = name.upper()

if "SILVA" not in uppy:
    print("Okay, looks like you're not who I thought you was. Could swear you had Silva in your name.")
else:
    print("Perfect, let's continue our job then, Mr.Silva.")
    