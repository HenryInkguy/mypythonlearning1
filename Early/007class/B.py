n1 = int(input('A value: '))
n2 = int(input('Another value: '))
s = n1 + n2
s2 = n1 - n2
m = n1 * n2
d = n1 / n2
mod = n1 % n2 
e = n1 ** n2
fd = n1 // n2

print('The sum is {}. The subtraction is {}. The multiplaction is {}. The division is {}.' .format(s,s2,m,d), end=' ')
print('The modulus is {}. The exponentiation is {}. The floor division is {}.' .format(mod,e,fd))

# \n for line breaking. (, end=' ') for continuing in the same line.

