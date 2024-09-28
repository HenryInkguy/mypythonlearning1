import math as m
import color_chart as c
      
start = int(input("The number it will start on: "))
end = int(input("The number it will end on: "))
jump = int(input("Interval (Every x numbers): "))


from time import sleep as s

even = 0
odds = 0
divth = 0
twodigit = 0

def starts():
    
    global function
    global functions
    
    function = int(input("""Tell me what do you want it to check: 
	(1) Quant. of even / odds
	(2) Quant. of numbers divisible by 3 or Not.
	(3) Quant. of numbers with 2 digits or more.
	(4) Square Root of the numbers.
	(5) Square of the numbers.
 """))
    
    if function == 1:
        def functions():
            if (test % 2) == 0:
                global even
                even += 1
            
            else:
                global odds
                odds += 1
                

    elif function == 2:
        def functions():
            if (test % 3) == 0:
                global divth
                divth += 1
        
    elif function == 3:
        def functions():
            quant = len(str(test))
            if quant > 1:
                global twodigit
                twodigit += 1

    elif function == 4:
        def functions():
            squareroot = m.sqrt(test)
            print(f"{c.color['yellow']}{test}{c.color['clear']} = {c.color['lilac']}{squareroot:.2f}{c.color['clear']}\n")
        
    
     
    elif function == 5:
        def functions():
            square = pow(test, 2)
            print(f"{c.color['yellow']}{test}{c.color['clear']} = {c.color['lilac']}{square}{c.color['clear']}\n")
    
    else:
        print("Invalid output, starting over in 5 seconds...")
        s(5)
        start()
    
    
    
starts()

for test in range(start, end, jump):
    functions()
    
total = (end - start) // jump
   
if function == 1:
    print(f"Number of Even: {c.color['lilac']}{even}{c.color['clear']}.")
    print(f"Number of Odds: {c.color['lilac']}{odds}{c.color['clear']}.")
    
elif function == 2:
    print(f"There are {c.color['lilac']}{divth}{c.color['clear']} numbers divisible by 3 between {c.color['yellow']}{start}{c.color['clear']} and {c.color['cyan']}{end}{c.color['clear']}.")
    print(f"So the rest that is not divisible by 3 is: {c.color['blue']}{(total) - divth}{c.color['clear']}")

elif function == 3:
    print(f"There are {c.color['lilac']}{divth}{c.color['clear']} numbers divisible by 3 between {c.color['yellow']}{start}{c.color['clear']} and {c.color['cyan']}{end}{c.color['clear']}.")
    print(f"So the rest that don't have two digits is: {c.color['blue']}{(total) - divth}{c.color['clear']}")
  

else:
    exit()
  
    