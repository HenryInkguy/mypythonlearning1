d4c = "Dirty Deeds Done Dirt Cheap 1"

print(d4c)

e_rep = d4c.count('e') # Checks how many times you can find a word or character in the entire str variable.
d4c_len = len(d4c) # Shows the quantity of indexes the str variable have.

print(f"{e_rep}, {d4c_len}")

e_rep_12 = d4c.count('e',0,13) # Checks how many times you can find a word or character between the index you choose, in this case, 0 and 13.
deeds = d4c.find('Deeds') # Checks the index in which the word/character is, returning -1 if not found, or the index in which it starts. Ex: d = deeds, f = d.find('deeds'), f = 0.

print(deeds, e_rep_12)

dirt = ('Dirt' in d4c) # Checks if there's an specific word or character in the string.

print(dirt)

love = d4c.replace('1', 'Love Train') # Replace a character/word with another character/word.
print(love)

scream = love.upper() # All words upper cased.
boring = love.lower() # All words lower cased.

print(scream,"and",boring) 

cap = d4c.capitalize() # Upper case in the first letter.
title = d4c.title() # Upper case in the first letter of every single word.
print(cap)
print(title)

nowadays = "   I wish I could turn back time, to the good old days.      "
strip = nowadays.strip() # Ends useless spaces.
stripl = nowadays.lstrip() # Left
stripr = nowadays.rstrip() # Right
print(strip)
print(stripl)
print(stripr)

split = d4c.split()
print(split)

join = '-'.join(split)
print(join)
