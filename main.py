"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""


def main():

c1 = "Calico"
c2 = "Siamese"
c3 = "Ragdoll"
player = 0
top = ""
bottoms = ""
    
def choose():
    player = int(input(f"Choose your character: \n{c1}\n{c2}\n{c3} \n(Enter 1, 2, or 3)\n"))
    confirm(player)
    
def confirm(player):
    if (player == 1):
        decide = input(f"Do you want to be the {c1} cat?\n")
        if(decide == "Y" or decide == "y"):
            nameit(player)
        else:
            choose()
    if (player == 2):
            decide = input(f"Do you want to be the {c2} cat?\n")
            if(decide == "Y"or decide == "y"):
                nameit(player)
            else:
                choose()
    if (player == 3):
            decide = input(f"Do you want to be the {c3} cat?\n")
            if(decide == "Y"or decide == "y"):
                nameit(player)
            else:
                choose()
            
            
def dressup(player):
    top = input("What top do you want to wear?")
    print("Top 1\nTop 2\nTop 3") 
    bottoms = input("What bottoms do you want to wear?")
    print("Bottom 1\nBottom 2\nBottom 3")  

    
def nameit(player):
    print("Lets name your charcater!")
    name:str = input("What do you want to name your cat?\n")
    display(player, name)
    
def display(player, name, top, bottoms):
    if player == 1:
        print(f"You are a {c1} cat named {name}!")
    elif player == 2:
        print(f"You are a {c2} cat named {name}!")
    elif player == 3:
        print(f"You are a {c3} cat named {name}!")    
    
choose()




#print("CSCI 1030U group project - not built yet.")
#print("Replace main() with your core loop. See MILESTONES.md for what is due when.")


if __name__ == '__main__':
    main()
