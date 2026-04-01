# imports
import random as r
# import random as r
import copy as cp
import time as t

# variables

# change all hp stuff here
e_HP=20
e_SPD=15
e_ATK=10

ENEMIES = ({"NAME": "Tui", "HP": r.randint(e_HP, e_HP+20), "SPD": r.randint(e_SPD, e_SPD+20), "ATK": r.randint(e_ATK, e_ATK+5), },
           {"NAME": "Kereru", "HP": r.randint(e_HP, e_HP+10), "SPD": r.randint(e_SPD, e_SPD+10), "ATK": r.randint(e_ATK, e_ATK+5), },
           {"NAME": "Weka", "HP": r.randint(e_HP, e_HP+10), "SPD": r.randint(e_SPD, e_SPD+5), "ATK": r.randint(e_ATK, e_ATK+5), },
           {"NAME": "Kakapo", "HP": r.randint(e_HP, e_HP+10), "SPD": r.randint(e_SPD, e_SPD+5), "ATK": r.randint(e_ATK, e_ATK+10), },
           {"NAME": "Pukeko", "HP": r.randint(e_HP, e_HP+10), "SPD": r.randint(e_SPD, e_SPD+5), "ATK": r.randint(e_ATK, e_ATK+10), }, )

HP = 50
SPD = 30
ATK = 35

enemy = []
treaty_parts = 0
player = [{"NAME": "", "B_HP": HP, "B_SPD": SPD, "B_ATK": ATK}]
healing_factor = 0.4
boost = 1.5


# function methods
def trytry(low, hi):  # Start of the function that makes sure user inputs a valid number
    while 1:  # WILL RUN FOREVER UNTIL HAS RETURNED A VALUE
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


def damage(n):  # Changes enemy or player health depending on given n value
    if n == 1:
        player[0]["B_HP"] -= r.randint(enemy[0]["ATK"] - 5, enemy[0]["ATK"])
        print("Your HP now: ", player[0]["B_HP"])
    if n == 0:
        enemy[0]["HP"] -= r.randint(player[0]["B_ATK"] - 5, player[0]["B_ATK"])
        print("Enemy HP: ", enemy[0]["HP"])


def dead(thing):  # Quick check to make sure whatever as thing is dead or not
    if thing <= 0:
        return 1


def opening():
    global player  # To allow writing into player list for name and stat boosts
    player = [{"NAME": "", "B_HP": HP, "B_SPD": SPD, "B_ATK": ATK}]
    print("==============================\nWelcome to New Zealand you have to find the Treaty of Waitangi\n"
          "that 6 "
          "birds have ate for breakfast!")
    player[0]["NAME"] = input("Enter your name: ")  # Decided not to use any checks whether name is valid or not
    # because user might input a name with numbers and characters
    print("Welcome, ", player[0]["NAME"], "!")
    print("This game only requires you to input the number keys!\nSo typing out the words will not work!!")
    print("==============================\nHP:", player[0]["B_HP"], "\nATK:", player[0]["B_ATK"])
    print("Choose ONE status to be boosted!\n  1.Health\n  2.Attack")
    choice = trytry(1, 2)  # uses boost value to increase the desired stat
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
        enemy.append(cp.deepcopy(ENEMIES[r.randint(0, len(ENEMIES) - 1)]))
    elif enemy[0]["HP"] <= 0:  # Checks if enemy HP below 0 (probably delete later now copy working)
        enemy.clear()
        enemy.append(cp.deepcopy(ENEMIES[r.randint(0, len(ENEMIES) - 1)]))
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
            damage(0)
            damage(1)
            # Both player and enemy take damage
            if dead(player[0]["B_HP"]) == 1:
                break
            if enemy[0]["HP"] <= 0:  # Check if killed
                print("WON THE BATTLE!!!!")
                enemy.clear()  # Clear enemy ready for next loop
                treaty_parts += 1  # Add one treaty part
                print("OBTAINED: Part", treaty_parts, "of treaty of Waitangi")
                break
            else:
                pass  # should loop back to start until either player or enemy hp is =< 0
        if choice == 2:  # HEAL CHOICE
            player[0]["B_HP"] += round(player[0]["B_HP"] * healing_factor)  # Round final HP after times by the
            # healing_factor in order to look nicer
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
        if dead(player[0]["B_HP"]) == 1:  # Player is dead comes back to here
            print("==============================\nYou have lost!")
            t.sleep(0.5)
            treaty_parts = 0
            break
        if treaty_parts < 5:  # Game is still running
            print("==============================\nI must fight the birds...\n  1.Fight")
            if trytry(1, 2) == 1:
                fight()
        else:  # If player is not dead and treaty_parts > 5 (completed game)
            print('Beat the game!\nTreaty rights have been restored to New Zealand!\nSelf resetting in')
            treaty_parts = 0  # resets treaty_parts no. for next player
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
