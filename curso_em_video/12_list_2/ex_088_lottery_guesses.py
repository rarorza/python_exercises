# Develop a program that helps a lottery player make guesses. The program will
# ask how many games will be generated and will raffle 6 numbers between 1 and
# 60 for each game, registering everything in a composite list.
from random import randint
from time import sleep

print("-" * 38)
print("Lottery Game".center(38))
print("-" * 38)

list_games = []

while True:
    total_games = int(input("How many game do you want to draw? "))
    for list_game in range(0, total_games):
        list_games.append([])
    for i, game in enumerate(list_games):
        while len(game) != 6:
            num_random = randint(1, 60)
            if num_random in game:
                continue
            game.append(num_random)
        print(f"GAME {i + 1} {sorted(game)}")
        sleep(.3)
    break
print("< Good Look! >".center(38, "-"))
