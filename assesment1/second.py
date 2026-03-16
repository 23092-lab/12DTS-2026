#imports
#import lib as l

#variables
character = [{"NAME":""},{"B_HP":"100"},{"B_SPD":"30"},{"B_ATK":"25"}]
#function methods
def opening():
    print("Welcome to new zealnd you will have to kill to survive!")
    print(character)
    print("Kill or be killed!!!")

def main():
    while 1:
        opening()
        inter()

def fight():
    print("you are fighting...")
def inter():
    print("What to do...\n1.Fight")
    try:
        loop = 1
        while loop == 1:
            choice = int(input(""))
            if choice < 1:
                print("Try again")
            if choice >1:
                print("Try again")
            if choice ==1:
                loop = 0
                fight()
    except ValueError:
        print("Try again")

#main loop
main()
