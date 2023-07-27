# Develop a program that reads the name, age and gender of 4 people. At the end
# of the program, show:
# 1 - The average age of the group
# 2 - What is the name of the older man.
# 3 - How many women are under 20 years old.

sum_age = highest_age_man = young_women = 0
man = ""

for person in range(1, 4 + 1):
    print(f"----- {person}ª PERSON -----")
    name = input("Name: ").title().strip()
    age = int(input("Age: "))
    sex = input("Sex [M/F]: ").upper().strip()
    sum_age += age
    if sex == "M":
        if age > highest_age_man:
            highest_age_man = age
            man = name
    elif sex == "F":
        if age <= 20:
            young_women += 1
    else:
        sex = ""


average_age = sum_age / 4
print(f"The average age of the group is {average_age} years")
print(f"The older man has {highest_age_man} years old and it's called {man}")
print(f"Altogether there are {young_women} women under 20")
