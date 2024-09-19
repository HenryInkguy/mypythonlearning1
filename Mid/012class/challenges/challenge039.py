# Challenge 039
# Make an application that reads the year of birth of a young person and show, according to his age:
# If he will have to enlist himself in the armies yet. If its already time for him to enlist himself in the armies. Or if its past time for him to enlist himself in the armies.
# The application also needs to show the missing or past time of the deadline.

ybirth = int(input("We need to know when you'll need to enlist yourself. What is your year of birth?\n"))
enlist = 2024 - ybirth
diff = abs(enlist - 18)

if enlist == 18:
    print(f"Oh you really have {enlist}? Its about time for you to finally enlist yourself. Like you or not.")

elif ybirth > 2017 or ybirth < 1960:
    print("This is no joke, dork. Tell me your true year of birth.")

elif enlist < 18:
    print(f"So you're getting there soon. You're {enlist} years old. So you'll need to enlist in {diff} years.")

elif enlist > 18:
    print(f"You're {enlist} years old? Well... past eighteen by a few, haha, maybe you really should enlist if you didn't yet. It's past {diff} years by now.")