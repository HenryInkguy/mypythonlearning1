# Challenge 026
# Make a script that reads a sentence and shows: How many times the letter "A" shows up, in which position it is when first shown, and for last shown.

sent = str(input("Okay, continuing to the following steps, please type any sentence you'd like: ")).strip().lower()
quant = sent.count('a')
fshown = sent.find('a')
lshown = sent.rfind('a')

print("\n")

print(f"""In your sentence, referring to the one you typed, there's a total of {quant} "a's" in it.
The first "a" that we got to see is in the index: {fshown+1}.
And the last one is in the index: {lshown+1}. """)
