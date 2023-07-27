# Develop a simple guessing game, the game have to choose an int number in
# between 0 and 5

from random import randint

random_num = randint(1, 5)
print("I will think in a number between 0 and 5. Try guess...")
guess = int(input("What number did I think of? "))
print("LOADING...")
if guess == random_num:
    print("GOOD! You win!")
else:
    print(f"I WIN! I was thinking in the number {random_num} and not {guess}")
