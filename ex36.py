from sys import exit
import random

def riddle():
    print("The elf silently guides you through the doors, ")
    print("and presents you to the elf queen.")
    print("She asks you the following riddle:")
    print("""
    What breathes, consumes, and grows
    ...But
    was never, and will never,
        be alive?
    Your answer is:""")

    choice = input("==> ").lower()

    if choice == "fire":
                    print("""
    She smiles and gives you the prize:
    a brilliant diamond that shines like the sun.
    You win!
                    """)

    else:
        # print("Oh, too bad. Wrong answer. She kicks you out. Game over.")
        dead("Oh, too bad. Wrong answer. She kicks you out. Game over.")

def awkward():
    print("\nYou hang for a little longer, then the elf says you must leave before his watch is over. ")
    print("You take the hint and return to the base of the tree,")
    print("feeling somehow like you've lost the guards respect")
    print("....like you've missed an opportunity. ")
    print("Alas, you return to your original errand,")
    print("to visit your elderly auntie in the next village over. \n")

def wrestle():
    strength = random.randint(0,100)
    print("\nYou and the guard have a nice conversation.")
    print ("He answers many of your questions, and tells you the history of his people. ")
    print("You become fast friends and he wants to arm wrestle you.")
    print("You know elves are stronger than they look, but it's all in the name of fun, right?\n")
    print("Choose 1: \"No! That sounds humiliating!\"")
    print("       2: \"I've always wanted to arm wrestle an elf. Let's do it!\"")

    choice = input("==>")

    if choice == "1":
        awkward()
        exit()

    else:
        print("You must beat his strength of 74")
        print(f"You roll a {strength}")
    if strength <= 10:
        awkward()
        exit()

    elif strength in range(11, 76):
        print("Lets relax a bit and try again")
        # strength = random.randint(0,100)
        wrestle()
    else:
        print("Wow, you have amazing strength. Come with me, I want to introduce you to someone.")

def elf():
    print("You see stairs built into a tree. Do you procees up the stairs?")

    choice = input("==> ").lower()

    if choice == "no":
        # print("""The elf guard that sneaked up behind you forces to to ascend.
        # You are jailed for the rest of your life. You die here. """)
        dead("""The elf guard that sneaked up behind you forces to to ascend.
        You are jailed for the rest of your life. You die here. """)
    else:
        print("""
You enjoy the view.
Towards the top, you see a door cut into the tree trunk.
There is an elven guard standing by.
What do you do?""")

        choice = input("==> ").lower()
        dies = ["run", "fight", "challenge"]
        passed = ["talk", "ask", 'wave']

        if any(x in choice for x in dies):
            print("The guard stabs you and you die. Game over.")

        elif any(x in choice for x in passed):
            wrestle()

        else:
            print("I don't understand. Try again")
            elf()

def wrestle():
    strength = random.randint(0,100)
    print("You and the guard have a nice conversation.")
    print ("He answers many of your questions, and tells you the history of his people. ")
    print("You become fast friends and he wants to arm wrestle you.")
    print("You know elves are stronger than they look, but it's all in the name of fun, right?\n")
    print("Choose 1: \"No! That sounds humiliating!\"")
    print("       2: \"I've always wanted to arm wrestle an elf. Let's do it!\"")

    choice = input("==>")

    if choice == "1":
        print("You hang for a little longer, then the elf says you must leave before his watch is over. ")
        print("You take the hint and return to the base of the tree,")
        print("feeling somehow like you've lost the guards respect")
        print("....like you've missed an opportunity. ")
        print("Alas, you return to your original errand,")
        print("to visit your elderly auntie in the next village over. ")
        exit()
    else:
        print("You must beat his strength of 74")
        print(f"You roll a {strength}")
    if strength <= 10:
        print("You hang for a little longer, then the elf says you must leave before his watch is over. ")
        print("You take the hint and return to the base of the tree,")
        print("feeling somehow like you've lost the guards respect")
        print("....like you've missed an opportunity. ")
        print("Alas, you return to your original errand,")
        print("to visit your elderly auntie in the next village over. ")
        exit()
    elif strength in range(11, 76):
        print("Lets relax a bit and try again")
        # strength = random.randint(0,100)
        wrestle()
    else:
        print("\nHe looks at you, amazed by his new friends brute strength. And from a human!")
        print("""
        "Wow!" he exclaims. "You have amazing strength."
        "Come with me, I want to introduce you to someone."
        """)
        riddle()

def mermaid():
    print("She sings to you a lovely song that makes you fall in love.")
    print("She laughs at your affections, and swims away.")
    print("Such is your love, you can only swim after her or drown yourself.")
    print("Which do you do?")

    choice = input("==> ").lower()

    if "drown" in choice:
        print("You die for love.")
        # dead("You die for love.")
    elif "swim" in choice:
        print("You catch her tail and ask her to take you")
        print("to her lands so you can be together.")
        print("She says to answer her riddle and she will.")
        print("""
"What always runs, yet doesn't walk,
                often murmurs but doesn't talk.
        Has a bed, but doesn't sleep,
            has a mouth but never eats."   """)

        choice = input("==> ").lower()

        if "river" in choice:
            print("You are correct. She turns you into a merperson")
            print("and you live happily ever after.")
        else:
            # print("Incorrect. She drowns you.")
            dead("Incorrect. She drowns you.")

def move_croc():

    choice = input("==> ").lower()
    eaten = ["fight", "kick", "taunt", "stab", "wrestle"]
    flee = ["run", "away", "flee", "walk", "feed", "food"]

    if any(x in choice for x in eaten):
        print("Dummy. The croc eats you.")
        exit()
        #dead("Dummy. The croc eats you.")

    elif any(x in choice for x in flee):
        print("You escape!")
        print("Soon enough you are on the other side of the lake.")
        print("There are lots of big trees on this side.")
        elf()

    else:
        print("That's not a good idea. Try again, goofball.")
        move_croc()


def croc():
    print("As you are walking, you see a log in your way! Do you move it or jump over it?")

    choice = input("==> ").lower()

    if "move" in choice:
        print("That's no log! That's a crocodile!")
        print("He kills and eats you.")

    elif "jump" in choice:
        print("Wise decision. That was a croc, not a log! It's hissing at you.")
        print("What do you do?")
        move_croc()

def lake():
    print("You see a lake and a row boat. Do you cross or go around? ")
    choice = input("==> ").lower()

    if "around" in choice:
        croc()
        # dead("You trip on an crocydile and get eaten. Sorry.")
    elif "cross" in choice:
        print("You're about half way across when a mermaid appears.")
        print("She asks you if you want to hear a song.")
        print("Do you tell her yes or no?")

        choice = input("==> ").lower()

        if choice == "yes":
            mermaid()

        else:
            print("She gently sinks below the surface of the lake.")
            print("As you gain the other shore, you see a giant tree.")
            elf()
    else:
        print(" I don't understand. Try again.")
        lake()

def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are traveling and you come upon a dark and foreboding forest.")
    print("As you enter the trees, you see your path diverges.")
    print("Do you go left or right?")

    choice = input("==> ").lower()

    if choice == "left":
        lake()
    elif choice == "right":
        elf()
    else:
        print("You didn't type that correctly. Try again. ")
        start()

start()
