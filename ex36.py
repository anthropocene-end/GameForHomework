from sys import exit

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
        print("Oh, too bad. Wrong answer. She kicks you out. Game over.")
        # dead("Oh, too bad. Wrong answer. She kicks you out. Game over.")
def elf():
    print("You see stairs built into a tree. Do you procees up the stairs?")

    choice = input("==> ").lower()

    if choice == "no":
        print("""The elf guard that sneaked up behind you forces to to ascend.
        You are jailed for the rest of your life. You die here. """)
            # dead("""The elf guard that sneaked up behind you forces to to ascend.
            # You are jailed for the rest of your life. You die here. """)
    else:
        print("""
You enjoy the view.
Towards the top, you see a door cut into the tree trunk.
There is an elven guard standing by.
What do you do?""")

        choice = input("==> ").lower()
        dies = ["run", "fight", "challenge"]
        passed = ["talk", "ask"]

        if any(x in choice for x in dies):
            print("The guard stabs you and you die. Game over.")

        elif any(x in choice for x in passed):
            riddle()


        else:
            print("I don't understand. Try again")
            elf()
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
            print("Incorrect. She drowns you.")
            # dead("Incorrect. She drowns you.")
def lake():
    print("You see a lake and a row boat. Do you cross or go around? ")
    choice = input("==> ").lower()

    if "around" in choice:
        print("You trip on an crocydile and get eaten. Sorry.")
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
