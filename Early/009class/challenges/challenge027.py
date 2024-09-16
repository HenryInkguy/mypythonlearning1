# Challenge 027
# Make a script that reads the full name of somebody, showing then the first and last name of them, separately.

name = str(input("Once again, here we are, tell me your full name so we can end it all quickly: ")).strip()
titnm = name.title()
split = titnm.split(' ')
fname = split[0]
lname = split[-1]



print(f"Good, here we go, so your first name is {fname}, cool, well, anyways, we will only call you by your last name.\n")
print(f"It's nice to have you around, Mr.{lname}.")
