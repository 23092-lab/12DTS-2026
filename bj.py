# python

# Libraries
import random

# Variables
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deck = []
hand = []
ai = []
handtotal = 0
aitotal = 0


# Functions
def draw(amount, player):
    for i in range(0, amount):
        x = random.randint(0, len(deck))
        player.append(deck[x - 1])
        deck.pop(x -1)


def sum(player):
    x = 0
    for i in range(0, len(player)):
        x = x + player[i]
    return x


# Main code
# Initialize deck
for x in VALUES:
    for y in range(0, 4):
        deck.append(x)
print(deck)

draw(2, hand)
draw(2, ai)
print(hand)
print(ai)
handtotal = sum(hand)
print(handtotal)
while 1:
    decision = int(input("hit or stand?"))
    if decision == 1:
        draw(1, hand)
        draw(1, ai)
        print(hand)
        print(ai)
        aitotal = sum(ai)
        handtotal = sum(hand)
        print(handtotal)
        if handtotal > 21:
            print("you lose!")
            handtotal = 0
            aitotal = 0
            break
        if aitotal > 21:
            print("you win")
            handtotal = 0
            aitotal = 0
            break
    if decision == 2:
        draw(1, ai)
        if handtotal > 21:
            print("you lose!")
            handtotal = 0
            aitotal = 0
            break
        if aitotal > 21:
            print("you win")
            handtotal = 0
            aitotal = 0
            break
