# Color in Python's Terminal

'\033[0;33;44m'

"""Style -
0 = None
1 = Bold
3 = Itallic
4 = Underline
7 = Negative"""

"""Text -
30 = White
31 = Red
32 = Green
33 = Yellow
34 = Blue
35 = Lilac
36 = Cyan
37 = Gray"""

"""Background -
40 up to 47 = Same as Text"""

print("Classic Hello World!")
print("\033[3;30;41mHello World!\033[0m")
print("\033[4;33;46mHello World!\033[0m")
print("\033[1;35;43mHello World!\033[0m")
print("\033[0;30;42mHello World!\033[0m")
print("\033[0mHello World!")
print("\033[7;37mHello World!\033[0m")