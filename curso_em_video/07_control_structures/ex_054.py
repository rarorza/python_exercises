# Develop a program that reads the year of birth of seven people. At the end,
# show how many people have not yet reached the age of majority and how many are
# already of age.

from datetime import date

years = []
current_year = date.today().year
majority_count = minority_count = 0

for i in range(1, 7 + 1):
    years.append(int(input(f"Digite o {i}° ano de nascimento: ")))

for year in years:
    if current_year - year >= 18:
        majority_count += 1
    else:
        minority_count += 1

print(f"Ao todo tivemos {majority_count} pessoa(s) maior(es) de idade")
print(f"E {minority_count} pessoa(s) menor(es) de idade")
