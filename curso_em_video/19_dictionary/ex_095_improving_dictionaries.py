# Improve CHALLENGE 093 to work with multiple players, including a system to
# view details of the performance of each player.

players = []
player = {}
goals = []
while True:
    player["Name"] = input("Player name: ").title()
    games = int(input("How many games he played? "))
    for game in range(0, games):
        goals.append(int(input(f"How many goals in match {game + 1}: ")))
    player["Goals"] = goals[:]
    player["Total"] = sum(goals)
    option = input("Do you want to continue? [Y/N] ").upper().strip()[0]
    players.append(player.copy())
    player.clear()
    goals.clear()
    if option == "N":
        break
print("-=" * 30)
print("id", "name".ljust(19), "goals".ljust(19), "total")
print("-" * 60)
for i, p in enumerate(players):
    print(
        f"{str(i).rjust(2)} {p['Name'].ljust(19)} {str(p['Goals']).ljust(19)} {p['Total']}"
    )
print("-" * 60)
while True:
    option = int(input("Show data of which player? (999 to stop) "))
    if option == 999:
        break
    if option > (len(players) - 1) or option < 0:
        print(f"Error! There is no player with code {option}")
    else:
        for i, p in enumerate(players):
            if int(option) == i:
                print(f"{p['Name']} player data")
                for game, goals in enumerate(p["Goals"]):
                    print(f"In game {game + 1} scored {goals} goals")
