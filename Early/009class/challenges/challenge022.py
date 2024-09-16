# Challenge 022
# Make a script that reads the full name of someone and shows:
# Full name with all characters in uppercase.
# Full name with all characters in lowercase.
# How many letters it have, not considering whitespaces.
# How many letters does only the first name have.

arctic = str(input("Tell me your full name, please: ")).strip()
uptic = arctic.upper()
lowtic = arctic.lower()
nospace = arctic.replace(" ","")
split = arctic.split()
quant = len(nospace)
quantf = len(split[0])

print(f"""Then your full name is {arctic}, right?
Good, your full name in uppercase is {uptic};
And in lower case is {lowtic};
Your name have a total of {quant} letters;
Your first name have a total of {quantf} letters.""")
