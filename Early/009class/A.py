d4c = "Dirty Deeds Done Dirt Cheap 1"

print(d4c)

e_rep = d4c.count('e')
d4c_len = len(d4c)

print(f"{e_rep}, {d4c_len}")

e_rep_12 = d4c.count('e',0,13)
deeds = d4c.find('Deeds')

print(deeds, e_rep_12)

dirt = ('Dirt' in d4c)

print(dirt)

love = d4c.replace('1', 'Love Train')
print(love)