import pygame as pg
import time as t

dumb = False
print("You are a man.")
\
t.sleep(5)

favnum = int(input("What is your favorite number between 1-10? \n"))

t.sleep(2)
\
if favnum == 7 or favnum == 5:
    print(f"Oh, {favnum}, that's really cool, mine too!")
    if favnum == 7:
        t.sleep(2)
        print(f"Actually, I hardly can choose between {favnum} and 5, it's so hard sometimes. They're both great numbers!")
        match = True
    elif favnum == 5:
        t.sleep(2)
        print(f"Actually, I can barely choose between {favnum} and 7, it's so hard sometimes. They're both great numbers!")
        match = True
elif favnum <= 10 and favnum != 7 and favnum != 5:
    t.sleep(2)
    print(f"Then your favorite number is {favnum}? Well, that's fine I guess, mine is 7, or maybe 5. I don't know, too hard to decide between these two.")
    match = False

else:
    t.sleep(2)
    print(f"What the hell man, that wasn't what I... {favnum} isn't even between 1 and 10... ugh... nevermind.")
    match = False
    dumb = True

\
\

if match == False and dumb == False:
    t.sleep(2)
    print("Anyways, it was nice to chat with you. Goodbye.")
    \
    t.sleep(5)
    print("...")
    t.sleep(5)
    print("END.")
    ending = "Not Even Close."

elif match == False and dumb == True:
    t.sleep(2)
    print("Anyways, it was nice to chat with you... I think. Goodbye.")
    \
    t.sleep(5)
    print("...")
    t.sleep(5)
    print("END.")
    ending = "Too Dumb For Friendship."

else:
    t.sleep(3)
    print("Maybe we should be friends? I mean, between 1/10, you had 2/10 of chances to have the same favorite numbers as I... not so hard but a bit rare. So, what do you think?\n")
    ch = str(input("Yes or No?\n")).strip().lower()
    
    if ch == "yes":
        \
        t.sleep(5)
        print("Cool! There's a nearby pub here, maybe we could grab something to eat and drink a bit, what do you think?\n")
        pub = str(input("Yes or No?\n")).strip().lower()
        
        if pub == "yes":
            print("Alr! Let's go then.")
            \
            t.sleep(10)
            print(f"\033[3mYou Walked for a while\033[0m")
            t.sleep(2)
            \
            print("\033[3mBefore finally arriving.\033[0m")
            \
            t.sleep(3)
            print("\033[3mThe day was nice and you both talked a lot. This person was actually really nice. Suddenly they make a different question from what you expected.\033[0m")
            t.sleep(2)
            \
            print("So... you're into women or men?")
            \
            preference = str(input("Male, Female or Neither?\n")).strip().lower()

            if preference == "male":
                t.sleep(3)
                print("Oh cool, well... me too actually.")
                \
                t.sleep(2)
                print("""\033[3mYou can notice the shy smile on her face... it was cute.
                You two spent the whole night off, just talking about things of your lives.
                And then it was finally time to go back home, she invited you to hers, maybe afraid of letting you slip.
                But you two agreed in having a date next week, so you just headed to your home and took some sleep.
                You still had work to do in the next morning.""")
                \
                t.sleep(2)
                print("...")
                t.sleep(3)
                \
                print("END.")
                
                ending = "Have A Good One. (M)"

            elif preference == "female":
                t.sleep(3)
                print("Haha... well, nice I guess.")
                \
                t.sleep(2)
                print("""\033[3mYou can notice the shy smile on her face... it was cute.
                You two spent the whole night off, just talking about things of your lives.
                And then it was finally time to go back home, she invited you to hers, maybe afraid of letting you slip.
                But you two agreed in having a date next week, so you just headed to your home and took some sleep.
                You still had work to do in the next morning.""")
                \
                t.sleep(2)
                print("...")
                t.sleep(3)
                \
                print("END.")

                ending = "Have A Good One. (F)"

            else:
                t.sleep(2)
                print("Oh, okay so. Well... thank you for today, it was really good, I hope we could do it again soon...")
                t.sleep(2)
                \
                print("...")
                \
                t.sleep(2)
                print("Goodbye...")
                \
                t.sleep(2)
                print("...")
                \
                t.sleep(3)
                print("END.")

                ending = "Not Interested."
            

        else:
            t.sleep(2)
            print("Well, then I will see you around! 'Til later!")
            \
            t.sleep(5)
            print("\033[3m They seemed to be quite excited, willing to see you again soon.\033[0m")
            t.sleep(5)
            \
            print("...")
            \
            t.sleep(10)
            print("END.")
            ending = "Simple Friendship."

    else:
        t.sleep(2)
        print("Oh...\n\n Well, then...\n\n I will just let you with a music from my favorite game, see you anytime soon, or maybe not...")
        pg.mixer.init()
        pg.mixer.music.load('zelda.mp3')
        pg.mixer.music.play()
        while pg.mixer.music.get_busy(): 
            pg.time.Clock().tick(10)
        \
        t.sleep(5)
        print("...")
        \
        t.sleep(5)
        print("END.")
        \
        ending = "Lost Friendship Opportunity."

t.sleep(5)

if ending != "" and dumb == True:
    print(f"\n\n\033[3mCongratulations... if you even deserve it. Your ending was... \n\n{ending}..\n\nSuch a disappointment...")

elif ending != "":
    print(f"\n\n\033[3mCongratulations. Your ending was...\n\n{ending}")

        
        

    