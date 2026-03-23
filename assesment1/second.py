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
def trytry(low, hi):
    while 1:
        try:
            loop = 1
            while loop == 1:
                choose = int(input())
                if choose < low:
                    print("Try again")
                elif choose > hi:
                    print("Try again")
                else:
                    loop = 0
                    return choose
        except ValueError:
            print("Try again")


def damage_dead(n, mmm):
    if n == 1:
        character[0]["B_HP"] -= ran.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
    if n == 0:
        enemy[0]["HP"] -= ran.randint(character[0]["B_ATK"] - 5, character[0]["B_ATK"])
    if mmm <= 0:
        return 1


def opening():
    print("==============================\nWelcome to New Zealand you have to find the Treaty of Waitangi\n that 6 "
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
    if len(enemy) == 0:  # Checks if enemy exists
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
    elif enemy[0]["HP"] <= 0:  # Checks if enemy HP below 0 (probably delete later now copy working)
        enemy.clear()
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
    print("THE", enemy[0]["NAME"], "!!", "\n", "HP: ", enemy[0]["HP"], "\n", "ATK range: ", enemy[0]["ATK"] - 5, "-",
          enemy[0]["ATK"])  # Description of enemy
    if character[0]["B_SPD"] > enemy[0]["SPD"]:  # Speed stat determines who starts first
        print("==============================\nYou start first!")
    else:
        print("==============================\nEnemy starts first!")
        damage_dead(0, character[0]["B_HP"])
        # character[0]["B_HP"] -= ran.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
        print("HP now: ", character[0]["B_HP"])
    while enemy[0]["HP"] > 0:  # loop for while enemy hp less than 0 but broken= not anymore
        print("==============================\n", enemy[0]["NAME"], "at", enemy[0]["HP"], "HP",
              "\nTake your actions\n  1.Attack\n  2.Heal", int(healing_factor * 100), "% of current HP")
        choice = trytry(1, 2)
        if choice == 1:  # Attacking loop
            print("Attacking...")
            enemy[0]["HP"] -= character[0]["B_ATK"]
            if enemy[0]["HP"] <= 0:  # Check if killed
                print("WON THE BATTLE!!!!")
                enemy.clear()
                # print(enemy)
                kill_count += 1
                print("OBTAINED: Part", kill_count + 1, "of treaty of Waitangi")
                break
            # for some reason freezes here NOT ANYMORE AAAA
        if choice == 2:
            character[0]["B_HP"] += character[0]["B_HP"] * healing_factor
            print("Attacked by enemy!")
            damage_dead(1, character[0]["B_HP"])
            # character[0]["B_HP"] -= enemy[0]["ATK"]
            print("HP now: ", character[0]["B_HP"])
            # ADD A ENEMY DAMAGE REMEMBER done i think
        else:
            break


def inter():  # fix again this is very very very very bad
    while 1:
        if kill_count < 5:
            print("==============================\nWhat are you going to do...\n  1.Fight")
            if trytry(1, 2) == 1:
                fight()
        else:
            print('Beat the game!\nRights have been restored to New Zealand!\nSelf Destructing in')
            for i in range(1, 6):
                t.sleep(0.5)
                print(i)
            break


def main():
    while 1:
        opening()
        inter()


# Start Main loops
main()
