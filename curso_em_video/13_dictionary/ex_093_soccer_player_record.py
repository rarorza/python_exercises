# Develop a program that manages the performance of a football player. The
# program will read the player's name and how many games he played. Then you
# will read the number of goals scored in each match. In the end, all of this
# will be stored in a dictionary, including the total number of goals scored
# during the championship.

player = {}
goals = []
player["Name"] = input("Player name: ").title()
games = int(input("How many games he played? "))
for game in range(0, games):
    goals.append(int(input(f"How many goals in match {game + 1}: ")))
player["Goals"] = goals
player["Total"] = sum(goals)
print("-" * 30)
print(player)
print("-" * 30)
for key, value in player.items():
    print(f"{key} {value}")
print("-" * 30)
print(f"The player {player['Name']} played {games} games")
for game in range(0, games):
    print(f"In game {game + 1}, scored {player['Goals'][game]} goals")
