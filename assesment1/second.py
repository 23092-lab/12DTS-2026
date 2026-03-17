# imports
import time

import lib as L
import random as ran
import copy as cp
import time as t

# variables
enemy = []
kill_count = 0
character = [{"NAME": "", "B_HP": 100, "B_SPD": 30, "B_ATK": 25}]
healing_factor = 0.4

# function methods
def trytry(min, max):
    while 1:
        try:
            loop = 1
            while loop == 1:
                choose = int(input())
                if choose < min:
                    print("Try again1")
                elif choose > max:
                    print("Try again2")
                else:
                    loop = 0
                    return choose
        except ValueError:
            print("Try again")


def opening():

    print("==============================\nWelcome to new zealand you have to find the treaty of waitingi\n that 5 "
          "birds have ate for breakfast!")
    character[0]["NAME"] = input("Enter your name: ")
    print("Welcome, ", character[0]["NAME"], "!")
    print("This game only requires you to input the number keys!\nSo typing out the words will not work!!")
    print("==============================\nHP:", character[0]["B_HP"], "\nATK:", character[0]["B_ATK"])
    print("Choose ONE status to be boosted!\n  1.Health\n  2.Attack")
    choice = trytry(1, 2)
    if choice == 1:
        character[0]["B_HP"] = 125
        print("==============================\nHealth has been boosted to", character[0]["B_HP"], "!")
    if choice == 2:
        character[0]["B_ATK"] = 35
        print("==============================\nAttack has been boosted to ", character[0]["B_ATK"], "!")


def fight():
    global enemy
    global kill_count
    print("==============================\nyou are fighting...")
    if len(enemy) == 0:
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
        print(L.ENEMIES)
    elif enemy[0]["HP"] <= 0:
        enemy.clear()
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
        print(L.ENEMIES)
    print(enemy)
    print("THE", enemy[0]["NAME"], "!!", "\n", "HP: ", enemy[0]["HP"], "\n", "ATK range: ", enemy[0]["ATK"] - 5, "-",
          enemy[0]["ATK"])
    if character[0]["B_SPD"] > enemy[0]["SPD"]:
        print("==============================\nyou start first")
    else:
        print("==============================\nenemy starts first")
        character[0]["B_HP"] -= ran.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
        print("HP now: ", character[0]["B_HP"])
    while enemy[0]["HP"] > 0:  # loop for while enemy hp less than 0 but broken
        print("==============================\n", enemy[0]["NAME"], "at", enemy[0]["HP"], "HP",
              "\nTake your actions\n  1.Attack\n  2.Heal",int(healing_factor*100),"% of current HP")
        choice = trytry(1, 2)
        if choice == 1:
            print("Attacking...")
            enemy[0]["HP"] -= character[0]["B_ATK"]
            if enemy[0]["HP"] <= 0:
                print("YOU HAVE WON!!!!")
                enemy.clear()
                print(enemy)
                kill_count += 1
                break
            # for some reason freezes here NOT ANYMORE AAAA
        if choice ==2 :
            character[0]["B_HP"] += character[0]["B_HP"] * healing_factor
            #ADD A ENEMY DAMAGE REMEBER
        else:
            break
    print("Hi")


def inter():  # fix again this is very very very very bad
    while 1:
        if kill_count < 5:
            print("==============================\nWhat to do...\n  1.Fight")
            if trytry(1, 2) == 1:
                fight()
        else:
            print('Beat the game\nSelf Destruct in')
            for i in range(1, 6):
                t.sleep(0.5)
                print(i)
            break


def main():
    while 1:
        opening()
        inter()


# main loop
main()
