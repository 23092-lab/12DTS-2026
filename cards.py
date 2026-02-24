import random

VALUES=[1,2,3,4,5,6,7,8,9,10,11,12,13]
SUITS=["Hearts","Clubs","Spades","Diamonds"]
deck=[[],[]]
hand=[[],[]]

no=0

def available(IN):
    if IN>len(deck[0]):
        print("try again")

def draw_hand(amount):
    for i in range(0,amount):
        x = random.randint(0,len(deck[0]))
        hand[0].append(deck[0][x])
        deck[0].pop(x)
        hand[1].append(deck[1][x])
        deck[1].pop(x)
    for i in range(0,len(hand[0])):
        print("hand", i + 1, "is:", hand[0][i], hand[1][i])

print("working")
for x in SUITS:
    print(x)
    for y in VALUES:
        deck[0].append(x)
        deck[1].append(y)
        print(y,x)

print("done")
print("deck contents:")
for i in range(0,len(deck[0])):
    print("card",i+1,"is:", deck[0][i],deck[1][i])

draw_hand(int(input("How many cards: ")))