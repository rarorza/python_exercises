# Develop a program that has a function called datasheet(), which receives two
# optional parameters: the player's name and how many goals he scored. The
# program must be able to show the player's technical file, even if some data
# has not been entered correctly.


def datasheet(player="<unknown>", goals="0"):
    player_name = input("Player name: ").title().strip()
    if len(player_name) != 0:
        player = player_name
    goals_number = input("Goals: ")
    if len(goals_number) != 0 and goals_number.isnumeric():
        goals = goals_number
    return player, goals


data = datasheet()
print(f"The player {data[0]} scored {data[1]} goals in the league")
