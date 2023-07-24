# Develop a program where 4 players roll a die and get random results. Store
# these results in a dictionary. In the end, put that dictionary in order,
# knowing that the winner got the highest number on the dice.
from random import randint
from time import sleep

players = {}
for i in range(1, 5):
    players["Player {}".format(i)] = randint(1, 6)
    print(f"Player {i} rolled {players['Player {}'.format(i)]} on the dice")
    sleep(0.5)

for i, place in enumerate(sorted(players, key=players.get, reverse=True)):
    print(f"{i + 1} place: {place} with {players[place]}")
    sleep(0.5)
