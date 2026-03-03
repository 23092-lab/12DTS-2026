import random
import pk_lib as m
import names as n


wild_pokemon=[]
own_pokemon=[]

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
    pass

let_there_be_life()
print(wild_pokemon)
pick_pokemon()
print(own_pokemon)