# Challenge 044
# Elaborate an application that calculates the value to be paid for a product, considering its normal price and the payment method:
# In cash: 10% Discount. In full (Card): 5% Discount. Up to 2x with a card: Normal price. 3x or more with a card: 20% Interest.

import color_chart as c
from time import sleep as t

def finalvalue():

    price = float(input(f"{c.text['itallic']}Type the value of the product you are going to buy: {c.text['clear']}"))
    paymeth = str(input(f"{c.text['itallic']}Choose what payment method you are going to use (Card or Cash): {c.text['clear']}")).strip().lower()

    yesno1 = str(input(f"{c.text['itallic']}So your payment method is {paymeth} and the value of the product you want to buy is U${price:.2f}, right? (Yes) or (No){c.text['clear']}\n")).strip().lower()
    
    if yesno1 == "yes":
        def method():
            if paymeth == "card":
                print(f"""{c.text['itallic']}Good. 
                (1)Paying in full you have 5% Discount.
                (2)Paying up to 2x you have the normal price.
                (3)Paying in 3x or more you have 20% of interest per installment.""")
                methodd = int(input(f"{c.text['bold']}What will be your method? (1) (2) (3)\n{c.text['clear']}"))
                if methodd == 1:
                    fullcard = price * 95 / 100
                    print(f"{c.text['bold']}Paying in full with card, you'll need to pay: U${fullcard:.2f}.{c.text['clear']}")
                    print(f"{c.text['itallic']}Do you want to try again with other method or values? (Type nothing to exit.)")
                    methval = str(input("(Method) or (Value)\n")).strip().lower()
                    if methval == "value":
                        print(f"Good, starting over after 5 seconds...")
                        t(5)
                        finalvalue()

                    elif methval == "method":
                        print(f"Good, starting over after 5 seconds...")
                        t(5)
                        method()

                    else:
                        print(f"{c.text['itallic']}Terminating code...")
                        exit()

                elif methodd == 2:
                    print(f"{c.text['bold']}Paying up to 2x you have to pay only the normal price, and it is the first price you typed: {price:.2f}.{c.text['clear']}")
                    print(f"{c.text['itallic']}Do you want to try again with other method or values? (Type anything to exit.)")
                    methval = str(input("(Method) or (Value)\n")).strip().lower()
                    if methval == "value":
                        print(f"{c.text['bold']}Good, starting over after 5 seconds...{c.text['clear']}")
                        t(5)
                        finalvalue()

                    elif methval == "method":
                        print(f"{c.text['bold']}Good, starting over after 5 seconds...{c.text['clear']}")
                        t(5)
                        method()

                    else:
                        print(f"{c.text['bold']}Terminating code...")
                        exit()

                elif methodd == 3:
                    def installments():
                        manytimes = int(input(f"{c.text['itallic']}Type how many installments, between 3 and 12, you're willing to pay: {c.text['clear']}"))
                        if manytimes >= 3 and manytimes <= 12:
                            installments = float((price / manytimes) + ((price / manytimes) * 20 / 100)) 
                            final_value = installments * manytimes
                            print(f"{c.text['bold']}You will pay it in {manytimes}, so every installment you'll pay is U${installments:.2f}, making the final value around U${final_value:.2f}.")
                            t(2)
                            print(f"{c.text['itallic']}Do you want to try again with other method or values? (Type anything to exit.)")
                            methval = str(input(f"(Method) or (Value)\n{c.text['clear']}")).strip().lower()
                            if methval == "value":
                                print(f"{c.text['bold']}Good, starting over after 5 seconds...{c.text['clear']}")
                                t(5)
                                finalvalue()

                            elif methval == "method":
                                print(f"{c.text['bold']}Good, starting over after 5 seconds...{c.text['clear']}")
                                t(5)
                                method()

                            else:
                                print(f"{c.text['bold']}Terminating code...")
                                exit()

                        else:
                            print(f"{c.text['bold']}Invalid value.")
                            print(f"{c.text['itallic']}Try again, returning in 5 seconds...{c.text('close')}")
                            t(5)
                            installments()

                else:
                    print("Invalid value, try again in 5 seconds.")
                    t(5)
                    method()
        


            elif paymeth == "cash":
                final_value = price - (price * 10 / 100)
                print(f"Good, paying on cash you'll have 10% discount, making the final value around U${final_value:.2f}")
                print(f"{c.text['itallic']}Do you want to check it with other product?")
                methval = str(input("(Yes) or (No)\n")).strip().lower()
                if methval == "yes":
                    print(f"{c.text['bold']}Good, starting over after 5 seconds...{c.text['clear']}")
                    t(5)
                    finalvalue()

                elif methval == "no":
                    print(f"{c.text['bold']}Terminating code...")
                    exit()

        
            else:
                print(f"Invalid Payment Method.")
                yesno2 = str(input(f"{c.text['itallic']}Do you want to try again? (Yes or No){c.text['clear']}")).strip().lower()
                if yesno2 == "yes":
                    finalvalue()

                elif yesno2 == "no":
                    print(f"{c.text['bold']}Good, if you want to use the application again soon, just run it.\n")
                    print(f"Terminating code...")
                    exit()

                else:
                    print(f"{c.text['bold']}Terminating code...")
                    exit()
        
        method()

    elif yesno1 == "no":
        yesno2 = str(input(f"{c.text['itallic']}Do you want to try again? (Yes or No){c.text['clear']}")).strip().lower()
        if yesno2 == "yes":
            finalvalue()

        elif yesno2 == "no":
            print(f"{c.text['bold']}Good, if you want to use the application again soon, just run it.\n")
            print(f"Terminating code...")
            exit()

        else:
            print(f"{c.text['bold']}Terminating code...")
            exit()

    else:
        print(f"{c.text['bold']}Terminating code...")
        exit()

finalvalue()