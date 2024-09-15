# Desafio (1)
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input ("Good morning, please confirm your name, I'll check in the list. Input: ")
print("Okay, so your name is",nome,", right?")
print("..."); print("...")
sobrenome = input ("I still can't find you here, may you tell me your last name, please? Input: ")
print("Yeah, good enough",nome,sobrenome,", welcome to the convention, enjoy.") 


# Desafio (2)
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

nome = input ("Your name please: ")
dia = input ("Your birth day: ")
mês = input ("Your birth month number: ")
ano = input ("Your birth year: ")
mes2 = str

print("Okay, so you're",nome,", born in month:",mês,"on day",dia,"of",ano)

# Desafio (3)
# Crie um script Python que leia números e tenta mostrar a soma entre eles.

num1 = input("Fine, so, type a number please, I will at the end, add the first to the third, the second to the fourth, and so on: ")
num2 = input("Another: ")
num3 = input("Another: ")
num4 = input("Another: ")
num5 = input("Another: ")
num6 = input("Another: ")
num7 = input("Almost there...: ")
num8 = input("The last one...: ")


sum1 = int(num1)+int(num3)
sum2 = int(num2)+int(num4)
sum5 = int(num5)+int(num7)
sum6 = int(num6)+int(num8)

print(f"Perfect! You ruled it! Now it's my turn, I'll take here num1 and add it to num3... so it's {num1} + {num3} equals... {sum1}")
print(f"Great, right? I think that's right, well you're new to coding but it should still be easy stuff for ya, now let's do the next... uhm... {num2} + {num4} equals... {sum2}")
print(f"Okay, now let's finish it already. {num5} + {num7} equals {sum5} and {num6} + {num8} equals {sum6}!")
print("Great friend, we got it, now go to your next exercise... or class, well I don't know, have a good one!")