# Challenge 012
# Make a script that reads the price of a product and shows a new value, with 5% of discount.

print('Tell me any value, and I will take 5% of discount from it (U$): ', end='')
product = float(input(''))
discount = product * (95/100)

print(f"The value of the product you typed is U$ {product:.2f}, the final value with 5% of discount is approximately U$ {discount:.2f}.")

