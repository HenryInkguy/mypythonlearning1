# Challenge 010
# Make a script that reads how much a person has in its wallet and show them how many dolars they can buy. Considers that U$1.00 = R$ 5.57

cur_dolar_val = float(5.57)
print(f"Hello! I am here today to help you in some ways, tell me how much money you actually have in your wallet/digital wallet, in R$, I will put it to the 'current' value conversion in U$, which is {cur_dolar_val} okay? Here we go: ", end='')
wallet = float(input(''))
amdolar = wallet / cur_dolar_val

print(f"Here it is, R$ {wallet} is approximately U$ {amdolar:.2f}, hope I could help you, have a nice one!")