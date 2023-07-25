# Create a program that reads the name, gender and age of several people,
# storing each person's data in a dictionary and all dictionaries in a list. At
# the end, show:
# a) How many people registered
# b) The average age
# c) A list of women
# d) A list with above average age

person = {}
persons = []
gender = ""
sum_age = 0
while True:
    person["Name"] = input("Name: ")
    while "M" not in gender and "F" not in gender:
        person["Gender"] = gender = input("Gender: [M/F] ").upper().strip()[0]
        if gender not in "MF":
            print("Error! Please, type M or F.")
    person["Age"] = input("Age: ")
    persons.append(person.copy())
    person.clear()
    gender = ""
    option = input("Do you want to continue? [Y/N] ").upper().strip()[0]
    if "N" in option:
        break
print("-=" * 30)
print(f"A) We have a total of {len(persons)} users registered")
for p in persons:
    sum_age += int(p.get("Age"))
print(f"B) The average age is {sum_age / len(persons):.2f} years old")
print("C) The registered women were ", end="")
for p in persons:
    if p.get("Gender") == "F":
        print(p["Name"], end=" ")
print("D) List of people above average age:")
for p in persons:
    if int(p.get("Age")) > (sum_age / len(persons)):
        print(f"Name = {p['Name']}; Gender = {p['Gender']}; Age = {p['Age']}")
