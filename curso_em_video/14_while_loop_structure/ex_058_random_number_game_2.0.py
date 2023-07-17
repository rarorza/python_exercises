# Improve the 028 CHALLENGE game where the computer will think of a number
# between 0 and 10. But now the player will try to guess until he gets it right,
# showing in the end how many guesses were needed to win.

from random import randint
from time import sleep

random_num = randint(1, 10)
tries = 0
print("I'm your computer...")
sleep(0.5)
print(
    """I just thought of a number between 0 and 10.
Can you guess which one it was?
"""
)
sleep(0.5)

while True:
    guess = int(input("What will your guess be? "))
    tries += 1
    if guess == random_num:
        print(f"Hit in {tries} tries. Congratulation!")
        break
    else:
        if guess > random_num:
            print("Less... Try again.")
        elif guess < random_num:
            print("More... Try again.")
