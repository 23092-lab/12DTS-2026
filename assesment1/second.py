# imports
import lib as l
import random as ran
# variables
enemy = []
character = [{"NAME": "","B_HP": 100, "B_SPD": 30, "B_ATK": 25}]
# function methods
def trytry(min, max):
    try:
        loop = 1
        while loop == 1:
            choice = int(input())
            if choice < min:
                print("Try again")
            if choice > max:
                print("Try again")
            else:
                return choice
    except ValueError:
        print("Try again")
def opening():
    print("Welcome to new zealnd you will have to kill to survive!")
    character[0]["NAME"]=input("Enter your name: ")
    print("Welcome, ", character[0]["NAME"], "!")
    print("==============================\nHP:",character[0]["B_HP"],"\nATK:",character[0]["B_HP"])
    #print(character)
    print("Kill or be killed!!!")
def fight():
    print("you are fighting...")
    enemy.append(l.enemies[ran.randint(0, len(l.enemies) - 1)])
    print(enemy)
    print("1.Attack\n2.idk")
    while enemy[0]["HP"] > 0:
        if trytry(1, 2) == 1:
            print("Attacking...")
            enemy[0]["HP"] -= character[0]["B_ATK"]
            print(enemy)
        if enemy[0]["HP"]<=0:
            print("YOU WIN!")
            enemy.clear()
            break
def inter():
    print("==============================\nWhat to do...\n  1.Fight")
    if trytry(1, 2) == 1:
        fight()
def main():
    while 1:
        opening()
        inter()
# main loop
main()