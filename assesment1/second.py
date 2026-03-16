# imports
import lib as l
import random as ran

# variables
enemy = []
kill_count = 0
character = [{"NAME": "", "B_HP": 100, "B_SPD": 30, "B_ATK": 25}]


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
    print("Welcome to new zealand you will have to kill to survive!")
    character[0]["NAME"] = input("Enter your name: ")
    print("Welcome, ", character[0]["NAME"], "!")
    print("==============================\nHP:", character[0]["B_HP"], "\nATK:", character[0]["B_ATK"])
    print("Choose ONE status to be boosted!\n  1.Health\n  2.Attack")
    choice = trytry(1, 2)
    if choice == 1:
        character[0]["B_HP"] = 125
        print("==============================\nHealth has been boosted to ", character[0]["B_HP"], "!")
    if choice == 2:
        character[0]["B_ATK"] = 35
        print("==============================\nAttack has been boosted to ", character[0]["B_ATK"], "!")
    print("You must slay 5 birds in order to restore the treaty of waitangi!")


def fight():
    global kill_count
    print("==============================\nyou are fighting...")
    enemy.append(l.enemies[ran.randint(0, len(l.enemies) - 1)])
    # print(enemy)
    print("THE", enemy[0]["NAME"], "!!", "\n", "HP: ", enemy[0]["HP"], "\n", "ATK range: ", enemy[0]["ATK"] - 5, "-",
          enemy[0]["ATK"])
    if character[0]["B_SPD"] > enemy[0]["SPD"]:
        print("==============================\nyou start first")
    else:
        print("==============================\nenemy starts first")
        character[0]["B_HP"] -= ran.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
        print("HP now: ", character[0]["B_HP"])
    print("==============================\nTake your actions\n  1.Attack\n  2.idk")
    while enemy[0]["HP"] > 0:  # loop for while enemy hp less than 0 but broken
        if trytry(1, 2) == 1:
            print("Attacking...")
            enemy[0]["HP"] -= character[0]["B_ATK"]
            # print(enemy)
        if enemy[0]["HP"] <= 0:
            print("YOU HAVE WON!!!!")
            enemy.clear()
            print(enemy)
            kill_count += 1
        print("HI")
        # for some reason freezes here
    print("Hi")


def inter():  # fix again this is very very very very bad
    if kill_count < 5:
        print("==============================\nWhat to do...\n  1.Fight")
        if trytry(1, 2) == 1:
            fight()
    else:
        print("beat game")


def main():
    while 1:
        opening()
        inter()


# main loop
main()
