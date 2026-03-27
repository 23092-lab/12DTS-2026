import random as r

ENEMIES = [  # Picks random enemy stats adjusted for a balance of overall hp, speed and atk.
    {
        "NAME": "Tui",
        "HP": r.randint(15, 20),
        "SPD": r.randint(40, 50),
        "ATK": r.randint(6, 10),
    },
    {
        "NAME": "Kereru",
        "HP": r.randint(20, 30),
        "SPD": r.randint(35, 45),
        "ATK": r.randint(5, 15),
    },
    {
        "NAME": "Weka",
        "HP": r.randint(25, 35),
        "SPD": r.randint(30, 41),
        "ATK": r.randint(7, 14),
    },
    {
        "NAME": "Kakapo",
        "HP": r.randint(30, 35),
        "SPD": r.randint(25, 35),
        "ATK": r.randint(10, 14),
    },
    {
        "NAME": "Pukeko",
        "HP": r.randint(40, 55),
        "SPD": r.randint(15, 25),
        "ATK": r.randint(20, 40),
    },
]
