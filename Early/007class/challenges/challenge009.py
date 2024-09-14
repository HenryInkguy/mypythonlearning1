# Challenge 009
# Make a script that reads an int number and shows its multiplication table.

num = int(input("Tell me a number to show you the multiplacation table of it: "))
print('--'*12)
print(f"Good, here it is: \n{num} x {'1':2} = {num*1:>3}\n{num} x {'2':2} = {num*2:>3}\n{num} x {'3':2} = {num*3:>3}\n{num} x {'4':2} = {num*4:>3}\n{num} x {'5':2} = {num*5:>3}")
print(f"{num} x {'6':2} = {num*6:>3}\n{num} x {'7':2} = {num*7:>3}\n{num} x {'8':2} = {num*8:>3}\n{num} x {'9':2} = {num*9:>3}\n{num} x {'10':2} = {num*10:>3}.")
print('--'*12)