# Develop a program to makes the computer play rock, paper, scissors with you.

import time
from random import randint

print(
    """
Your options:
[0] ROCK
[1] PAPER
[2] SCISSORS
      """
)
moves = ["ROCK", "PAPER", "SCISSORS"]
random = randint(0, 2)
option = int(input("What's your move? "))

if option <= 2 and option >= 0:
    print("JO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PO!!!")
    print("-=" * 15)
    print(f"Computer played {moves[random - 1]}")
    print(f"Player played {moves[option - 1]}")
    print("-=" * 15)

    if option == random:
        print("TIE!")
    elif (
        (option == 0 and random == 1)
        or (option == 1 and random == 2)
        or (option == 2 and random == 0)
    ):
        print("COMPUTER WINS!")
    elif (
        (option == 0 and random == 2)
        or (option == 1 and random == 0)
        or (option == 2 and random == 1)
    ):
        print("PLAYER WINS!")
else:
    print("Invalid option")
