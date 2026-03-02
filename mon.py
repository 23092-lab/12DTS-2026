import random

POKEMON_NAMES=["Charizard","Eevee","Evernight"]
NUMBER_OF_POKEMON=len(POKEMON_NAMES)
MIN_LEVEL=45
MAX_LEVEL=50

MIN_HEALTH=130
MAX_HEALTH=150

wild_pokemon=[]

for x in POKEMON_NAMES:
    wild_pokemon.append({"NAME":x,
                            "Level":random.randint(MIN_LEVEL,MAX_LEVEL),
                            "Health":random.randint(MIN_HEALTH,MAX_HEALTH)
                            }
    )



print(wild_pokemon)