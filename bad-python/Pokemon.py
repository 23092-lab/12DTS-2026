import random
import time
a=1
b=3
c=17
d=35


natrix = [{"yyy":"color"},{"ert"}]
print (natrix)

wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(a,b),"Health":random.randint(c,d)},
    {"Name":"Venasaur","Type":"Grass","Level":random.randint(a,b),"Health":random.randint(c,d)},
    {"Name":"Blastoise","Type":"Grass","Level":random.randint(a,b),"Health":random.randint(c,d)},
    {"Name":"Gardivour","Type":"Fairy","Level":random.randint(a,b),"Health":random.randint(c,d)},
    {"Name":"Vaporeon","Type":"Water","Level":random.randint(a,b),"Health":random.randint(c,d)},
    {"Name":"Leafeon","Type":"Grass","Level":random.randint(a,b),"Health":random.randint(c,d)}

]

own_pokemon =[{"Name":"Pidgy","Type":"Flying","Level":3,"Health":20,"Attack":["Flap":,random.randint(a,b)]}]
print(wild_pokemon)


def overworld_timer():
    timer = random.randint(1,5)
    print(timer)
    time.sleep(timer)
    print("battle begins")
    battle()

def enemy_attack(pokemon):


def battle():
    x=random.randint(0,len(wild_pokemon)-1)
    pokemon = wild_pokemon[x]
    print("A wild",pokemon["Name"],"appeared")
    print("It's a",pokemon["Type"], "type")
    print("Level: ",pokemon["Level"])
    print("It has", pokemon["Health"], "health")
    enemy_attack(x)


while 1:
    overworld_timer()
