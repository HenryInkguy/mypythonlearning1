quant = 0
quant1 = 0

for teste in range(0, 10000):
    if (teste % 8) == 0:
        quant = quant + 1
       

    elif (teste % 8) != 0:
        quant1 = quant1 + 1
    

print(f"{'=-='*20}")
print(f"Numbers divisible by 8 between 0 and 10000: {quant}")
print(f"Numbers not divisible by 8 between 0 and 10000: {quant1}")
print(f"{'=-='*20}")

# Jump from a number to other in for range function.

quant2 = 0
quant3 = 0

for t2 in range(0, 10000, 8):
    if (teste % 8) == 0:
        quant2 += 1
    
    elif (teste % 8) != 0:
        quant3 += 1

print(f"{'=-='*20}")
print(f"Numbers divisible by 8 between 0 and 1000, every 8 numbers: {quant2}")
print(f"Numbers not divisible by 8 between 0 and 1000, every 8 numbers: {quant3} ")
print(f"{'=-='*20}")

# Using variables for the same purpose.

init = int(input(f"Set in what number will it start: "))
end = int(input(f"Set in what number will it end: "))
jump = int(input(f"Set every what number will it read the value between {init} and {end}: "))

for t3 in range (init, end, jump):
    print(t3)
    