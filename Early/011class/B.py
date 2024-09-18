colors = {'clear':'\033[m', 
         'blue':'\033[34m', 
         'yellow':'\033[33m', 
         'lilac':'\033[35m',
         'inverted':'\033[7;37m'}

name = str(input("What's your name?\n"))

print(f"Hello {colors['lilac']}{name}{colors['clear']}, how are you {colors['yellow']}doing today?{colors['clear']} If you want, you can be welcomed into my {colors['inverted']}inverted world...{colors['clear']}")