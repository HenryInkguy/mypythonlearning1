# Challenge 014
# Make a script that reads certain temperature in Celsius (C°) and then show the equivalent in Fahrenheit (F°). Vice-Verse for further challenge.

print("1(Celsius to Fahrenheit) or 2(Fahrenheit to Celsius) converter, please type '1' for the first option or type '2' for the second one: ", end='')
c_or_f = int(input(''))

print('\n')

if (c_or_f == 1):
    print("Great, now type the temperature in Celsius you want to convert to Fahrenheit: ", end='')
    c1 = float(input(''))
    f1 = c1 * (9/5) + 32
    print(f'\nCelsius: {c1:.2f} C°\nin\nFahrenheit: {f1:.2f} F°')

elif (c_or_f == 2):
    print("Great, now type the temperature in Fahrenheit you want to convert to Celsius: ", end='')
    f1 = float(input(''))
    c1 = (f1 - 32) * (5/9)
    print(f'\nFahrenheit: {f1:.2f} F°\nin\nCelsius: {c1:.2f} C°')

else:
    print("Well... this ain't a valid number, try again.")

