# imports
import lib as L
import random as ran
import copy as cp
import time as t

# variables

# change all hp stuff here
HP = 20
SPD = 30
ATK = 25

enemy = []
treaty_parts = 0
player = [{"NAME": "", "B_HP": HP, "B_SPD": SPD, "B_ATK": ATK}]
healing_factor = 0.4
boost = 1.5


# function methods
def trytry(low, hi):
    while 1:  # WILL ALWAYS RUN UNTIL HAS RETURNED A VALUE
        try:
            loop = 1
            while loop == 1:
                choose = int(input(":"))
                if choose < low:
                    print("Try again")
                elif choose > hi:
                    print("Try again")
                else:
                    loop = 0
                    return choose
        except ValueError:
            print("Try again")


def damage(n):  # Name because it computes damage
    if n == 1:
        player[0]["B_HP"] -= ran.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
        print("Your HP now: ", player[0]["B_HP"])
    if n == 0:
        enemy[0]["HP"] -= ran.randint(player[0]["B_ATK"] - 5, player[0]["B_ATK"])
        print("Enemy HP: ", enemy[0]["HP"])


def dead(xyz):
    if xyz <= 0:
        return 1


def opening():
    global player
    player = [{"NAME": "", "B_HP": HP, "B_SPD": SPD, "B_ATK": ATK}]
    print("==============================\nWelcome to New Zealand you have to find the Treaty of Waitangi\n"
          "that 6 "
          "birds have ate for breakfast!")
    player[0]["NAME"] = input("Enter your name: ")
    print("Welcome, ", player[0]["NAME"], "!")
    print("This game only requires you to input the number keys!\nSo typing out the words will not work!!")
    print("==============================\nHP:", player[0]["B_HP"], "\nATK:", player[0]["B_ATK"])
    print("Choose ONE status to be boosted!\n  1.Health\n  2.Attack")
    choice = trytry(1, 2)
    if choice == 1:
        player[0]["B_HP"] += round(player[0]["B_HP"] * boost)
        print("==============================\nHealth has been boosted to", player[0]["B_HP"], "!")
    if choice == 2:
        player[0]["B_ATK"] += round(player[0]["B_HP"] * boost)
        print("==============================\nAttack has been boosted to ", player[0]["B_ATK"], "!")


def fight():
    global enemy
    global treaty_parts
    print("==============================\nyou are fighting...")
    if len(enemy) == 0:  # Checks if enemy exists
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
    elif enemy[0]["HP"] <= 0:  # Checks if enemy HP below 0 (probably delete later now copy working)
        enemy.clear()
        enemy.append(cp.deepcopy(L.ENEMIES[ran.randint(0, len(L.ENEMIES) - 1)]))
    print("THE", enemy[0]["NAME"], "!!", "\n", "HP: ", enemy[0]["HP"], "\n", "ATK range: ", enemy[0]["ATK"] - 5, "-",
          enemy[0]["ATK"])  # Description of enemy

    while enemy[0]["HP"] > 0:  # loop for while enemy hp less than 0 but broken= not anymore
        if player[0]["B_SPD"] > enemy[0]["SPD"]:  # Speed stat determines who starts first
            print("==============================\nYou start first!")
        else:
            print("==============================\nEnemy starts first!")
            damage(1)
            if dead(player[0]["B_HP"]) == 1:
                # print("HP now: ", player[0]["B_HP"])
                break
        # print("==============================\n", enemy[0]["NAME"], "at", enemy[0]["HP"], "HP",)
        print("==============================\nTake your actions\n  1.Attack\n  2.Heal", int(healing_factor * 100),
              "% of current HP")
        # prints choices maybe add more
        choice = trytry(1, 2)
        if choice == 1:  # Attacking selection
            print("Attacking...")
            t.sleep(0.3)
            enemy[0]["HP"] -= player[0]["B_ATK"]
            damage(1)
            if enemy[0]["HP"] <= 0:  # Check if killed
                print("WON THE BATTLE!!!!")
                enemy.clear()
                treaty_parts += 1
                print("OBTAINED: Part", treaty_parts, "of treaty of Waitangi")
                break
            if dead(player[0]["B_HP"]) == 1:
                break
            else:
                pass
            print("what")
            print(enemy)
        if choice == 2:  # HEAL CHOICE
            player[0]["B_HP"] += round(player[0]["B_HP"] * healing_factor)

            print("Attacked by enemy!")
            damage(1)
            if dead(player[0]["B_HP"]) == 1:
                break  # Return to inter function which checks for hp value and ends game there

            print("HP now: ", player[0]["B_HP"])
        else:
            pass


def inter():
    global treaty_parts
    while 1:
        if dead(player[0]["B_HP"]) == 1:
            print("==============================\nYou have lost!")
            t.sleep(0.5)
            treaty_parts = 0
            break
        if treaty_parts < 5:
            print("==============================\nI must fight the birds...\n  1.Fight")
            if trytry(1, 2) == 1:
                fight()
        else:
            print('Beat the game!\nRights have been restored to New Zealand!\nSelf resetting in')
            treaty_parts = 0
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
