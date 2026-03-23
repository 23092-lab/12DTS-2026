# program will run again and again
# game idea: find scattered pieces of the treaty of waiting to piece back together and restore equal rights
#            use dictionaries in list for inventory, functions for robustness, 3 puzzles to solve
#            word search, quick time challenge,
#            choice to go places using keyboard.
# FIX LOOPS OR ELSE BIG CRASH!!!!
# Imports
import random
import time
# Variables
NO_PUZZLES=3
completion=[]
inventory=[]
loop=1
choice=0
# Functions
def bush_city():
    print("================================================\nWelcome to Bush City!")
    loop =1
    while loop==1:
        if int(input("solve the puzzle "))==1:
            loop = 0
            inventory.append("done")
            completion[0]=True
            print (inventory)
            game_check()
            print("e")
            break

def waitangi():
    print("================================================\nWelcome to Level 4, Treaty of Waitangi")

def art_studio():
    print("================================================\nWelcome to the Art Studio")

def cafe():
    print("================================================\nWelcome to the cafe!")

def range_check(x,min,max):
    if x >= min and x <= max:
        return 1 # returns true to range check func if true
    else:
        return 0

def game_check():
    if len(inventory)==3: # check for appends to list as amount of pieces
        print("thank you for playing the game, the program will now self destruct in 5")
        time.sleep(0.5)
        print("4")
        print("3")
        print("2")
        print("1")
        inventory.clear()
        starting_sequence()
    else:
        pass
def choice():
    loop=1
    while loop==1:
        try:
            print("================================================\nWhere do you want to go?")
            print(completion)
            if completion[0]==False:
                print("1. Bush City")
            if completion[0]==True:
                print("1. (COMPLETED) Bush City")
            if completion[1]==False:
                print("2. Treaty of Waitangi")
            if completion[1]==True:
                print("2. (COMPLETED) Treaty of Waitangi")
            if completion[2]==False:
                print("3. Art Studio")
            if completion[2]==True:
                print("3. (COMPLETED) Art Studio")
            choice = int(input())
            #choice = int(input("================================================\nWhere do you want to go?\n1. Bush City\n2. Level 4, Treaty of Waitangi: Signs of a Nation\n3. Level 5, Art Studio \n4. Cafe (HINT)\n:"))

            # fix choice to individual check so know when one place is done
            #start range check if valid between choices
            if range_check(choice,1,4)==1:
                loop=0 #stops loop if it is valid
            else:
                print("================================================\nTry again") # if out of range
                #time.sleep(0.1)
        except ValueError:         # if anything other than int
            print("================================================\nTry again")
            #time.sleep(0.1)
    if choice==1:
        bush_city()
    if choice==2:
        waitangi()
    if choice==3:
        art_studio()
    if choice==4:
        cafe()
def main():
    while 1:
        starting_sequence()
def starting_sequence():
    print("================================================\nWelcome to Te Papa!\nWe are in desperate need of someone to find the scattered pieces of the Treaty of Waitangi!"
          "\nTo find the pieces, go to each floor and solve the puzzles on that floor")
    choice()
# Main
for i in range(0,NO_PUZZLES):
    completion.append(False)
main()

