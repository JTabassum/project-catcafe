import argparse
# This is a simple text-based adventure game 
# the player takes on the role of a cat baker who must deliver cupcakes to a princess.

print("Welcome to the Cat Baker Adventure Game!")

#step 1: Customize your cat
print("Before we start, customize your cat!")

fur_color = input("What is your cat's fur color? (black/white/ginger) ")

if fur_color not in ["black", "white", "ginger"]:
    print("Invalid fur color. defaulting to ginger.")
    fur_color = "ginger"
elif fur_color == "black":
    print("Your cat is a sleek black cat!")
elif fur_color == "white":
    print("Your cat is a fluffy white cat!")
elif fur_color == "ginger":
    print("Your cat is a vibrant ginger cat!")

eye_color = input("What is your cat's eye color? (blue/purple/pink) ")

if eye_color not in ["blue", "purple", "pink"]:
    print("Invalid eye color. defaulting to pink.")
    eye_color = "pink"
elif eye_color == "blue":
    print("Your cat has beautiful blue eyes!")
elif eye_color == "purple":
    print("Your cat has stunning purple eyes!")
elif eye_color == "pink":
    print("Your cat has charming pink eyes!")



# Story part of the Cat Bakery game.
# Decisions are always in this order: 1 = brave, 2 = smart, 3 = peaceful.

def ask(first, second, third):
    """Show the 3 decisions and return the player's choice as "1", "2" or "3"."""
    print()
    print(f"1. (Brave)    {first}")
    print(f"2. (Smart)    {second}")
    print(f"3. (Peaceful) {third}")
    choice = input("What will you do? (1, 2 or 3): ")
    if choice != "1" and choice != "2" and choice != "3":
        print("Please type 1, 2 or 3.")
        return ask(first, second, third)  # asks again
    return choice


def play_bakery(name):
    print()
    print(f"My name is {name} and it's my first day in the bakery!")

    print()
    print("Ring ring... ring ring...")
    input("Press Enter to answer the phone.")

    print()
    print(f"Princess: Hello, {name}! I need a cake delivered to the castle.")

    choice = ask("Say 'I'll deliver it right now, no matter what!'",
                 "Check the map and pack the cake safely first.",
                 "Politely ask the princess to wait while you bake it fresh.")
    if choice == "1":
        print("The princess cheers for your courage.")
    elif choice == "2":
        print("You study the map and plan the safest road.")
    else:
        print("The princess smiles and says she will wait for the fresh cake.")

    print(f"{name} packs the cake and runs to the castle!")
    return choice


def play_bubble_forest():
    print()
    print("Level 1: The Bubble Forest")
    print("In order to succeed in this quest and earn the maximum amount of coins you must avoid the bubbles at all costs.")

    choice = ask("Run straight through the bubbles!",
                 "Look for a hidden path around the bubbles.",
                 "Sit quietly and wait for the bubbles to float away.")
    if choice == "1":
        print("Pop! Pop! Pop! You burst through the bubbles. It was scary, but you made it!")
    elif choice == "2":
        print("You spot a narrow path behind the trees and tiptoe around every bubble.")
    else:
        print("You wait calmly. One by one the bubbles drift away and the way is clear.")
    return choice


def play_underwater():
    # Level 2 is the scoring code. It has no story decision, so nothing is returned.
    # When the files are put together, call the scoring code from here.
    print()
    print("[Level 2: Underwater - the scoring level goes here]")


def play_final_boss():
    print()
    print("Level 3: The final boss")
    print("In order to succeed in this quest and earn the maximum amount of coins you must defeat the final boss and save the princess.")

    choice = ask("Charge at the boss and fight!",
                 "Trick the boss into walking into its own trap.",
                 "Offer the boss a slice of cake and talk it out.")
    if choice == "1":
        print("You leap at the boss with your claws out!")
    elif choice == "2":
        print("You lay a trap with a trail of cake crumbs. The boss walks right into it!")
    else:
        print("The boss was only hungry. It happily eats the cake and puts down its sword.")
    return choice


def save_checkpoint(part, choices):
    # Tells the player how to continue from this point later.
    print()
    print(f"*** Checkpoint {part} reached! ***")
    print("To continue from here later, run:")
    print(f"python cat_bakery_game.py --checkpoint {part + 1} --choices {choices}")
    input("Press Enter to keep playing...")


def show_ending(choices):
    # Count how often each type of decision was chosen
    brave = choices.count("1")
    smart = choices.count("2")
    peaceful = choices.count("3")

    print()
    print(f"Your choices: Brave = {brave}, Smart = {smart}, Peaceful = {peaceful}")
    print()

    if brave >= 2:
        print("ENDING: The Fearless Hero")
        print("The whole kingdom cheers for the cat who never backed down. The princess makes you captain of the royal guard!")
    elif smart >= 2:
        print("ENDING: The Clever Baker")
        print("The princess is amazed by your clever plans. She asks you to be the royal advisor, and to bake for the castle every day!")
    elif peaceful >= 2:
        print("ENDING: The Kind Friend")
        print("Everyone in the kingdom becomes your friend. The princess invites you to a tea party in your honour!")
    else:
        print("ENDING: The Perfect Balance")
        print("You were brave, smart and kind. The princess opens the Whisker & Whisk Bakery's second shop, right inside the castle!")

    print()
    print("THE END")


def main(name=None):
    # name can be passed in if the character code already asked for it
    parser = argparse.ArgumentParser(description="Cat Bakery Adventure")
    parser.add_argument("--checkpoint", type=int, default=1, help="part to start from (1 to 4)")
    parser.add_argument("--choices", default="", help="choices made so far, for example 13")
    args = parser.parse_args()

    # Each digit in choices is one past decision: 1 = brave, 2 = smart, 3 = peaceful
    choices = args.choices

    if args.checkpoint <= 1:
        if name is None:
            name = input("What is your cat's name? ").strip()
            if name == "":
                name = "Mochi"
        choices = choices + play_bakery(name)
        save_checkpoint(1, choices)

    if args.checkpoint <= 2:
        choices = choices + play_bubble_forest()
        save_checkpoint(2, choices)

    if args.checkpoint <= 3:
        play_underwater()
        save_checkpoint(3, choices)

    if args.checkpoint <= 4:
        choices = choices + play_final_boss()

    show_ending(choices)


if __name__ == "__main__":
    main()
