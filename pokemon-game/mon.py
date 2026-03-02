import random
import pk_lib as m
import names as n


wild_pokemon=[]
own_pokemon=[]
#for x in m.POKEMON_NAMES: #increment for amount of pokemon
#    wild_pokemon.append({"NAME": x,
#                            "Level": random.randint(m.MIN_LEVEL, m.MAX_LEVEL),
#                            "Health": random.randint(m.MIN_HEALTH, m.MAX_HEALTH)
#                            }
#   )
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
    print("Type name: ")
    name = input()
    own_pokemon.append(wild_pokemon[1][name])
    print(own_pokemon)
def battle_loop():
    pass
let_there_be_life()
pick_pokemon()