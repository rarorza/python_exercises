# create a tuple filled with the top 20 players in the Brazilian football league
# table, in order of ranking. Then show:
# a) top 5
# b) the last 4
# c) teams in alphabetical order
# d) in what position is the Santos team?


teams = (
    "Botafogo",
    "Grêmio",
    "Flamengo",
    "Palmeira",
    "Bragantino",
    "Fluminense",
    "São Paulo",
    "Internacional",
    "Athletico-PR",
    "Atlético Mineiro",
    "Fortaleza",
    "Cruzeiro",
    "Cuiabá",
    "Santos",
    "Bahia",
    "Corinthians",
    "Goiás",
    "Vasco da Gama",
    "América-MG",
    "Coritiba",
)
print(f"List of Brazilian soccer teams: {teams}")
print("-" * 60)
print(f"The top 5 {teams[:5]}")
print("-" * 60)
print(f"The last 4 {teams[-5:]}")
print("-" * 60)
print(f"Teams in alphabetical order {sorted(teams)}")
print("-" * 60)
print(f'Santos is in position {teams.index("Santos")}')
