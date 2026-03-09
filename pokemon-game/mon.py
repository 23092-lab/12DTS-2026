import random
import pk_lib as m
import names as n

own_pokemon=[]
wild_pokemon=[]
battling=[]

def let_there_be_life():
    wild_pokemon.clear()
    for x in range(0,len(n.all_pokemon)):
        wild_pokemon.append({"NAME":n.all_pokemon[x]["name"],
                             "TYPE":n.all_pokemon[x]["type"],
                             "HP": n.all_pokemon[x]["hp"],
                             "ATK": n.all_pokemon[x]["attack"]

        })
        print(wild_pokemon[x])

def pick_pokemon():
    loop=1
    while loop==1:
        print("Type pokemon name: ")
        name = input().strip()
        match = next((i for i in wild_pokemon if i['NAME'].lower() == name.lower()), None)
        if match:
            own_pokemon.append(match.copy())
            print(f"You have chosen: {match['NAME']}.")
            loop =0
        else:
            print(f"Error: '{name}' was not found in the wild.")
def battle_loop():
    battling.append(wild_pokemon[random.randint(0,len(wild_pokemon))])
    print(battling)
    print("You are fighting ",battling[0]['NAME'],"!")
    print(own_pokemon)
    if own_pokemon[1]=='Normal':
        move = input("1.Tackle")
        if move == 1:
            (battling[2]['HP']) - (own_pokemon[3]['ATK'])

    print("")

let_there_be_life()
print(wild_pokemon)
pick_pokemon()
battle_loop()