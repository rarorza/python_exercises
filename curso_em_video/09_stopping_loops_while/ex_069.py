# Create a program that reads the age and gender of several people. For each
# person registered, the program should ask if the user wants to continue or
# not. At the end, show:
# a) How many people are over 18 years old.
# b) How many men were registered.
# c) How many women are under 20 years old.

majority = 0
men = 0
women_under_20_years = 0

while True:
    print("-" * 30)
    print("REGISTER A PERSON".center(30))
    print("-" * 30)

    age = int(input("Age: "))
    if age >= 18:
        majority += 1

    gender = " "
    while gender not in "MF":
        gender = input("Gender: [M/F] ").strip().upper()[0]
    print("-" * 30)
    if gender in "M":
        men += 1
    if gender in "F" and age < 20:
        women_under_20_years += 1

    option = " "
    while option not in "YN":
        option = input("Do you want to continue? [Y/N] ").strip().upper()[0]
    if option in "N":
        break
    elif option in "Y":
        continue

print(f"""
Total number of people over 18 years old {majority}.
Altogether we have men {men} registered.
We have {women_under_20_years} women under 20 years old.
""")
