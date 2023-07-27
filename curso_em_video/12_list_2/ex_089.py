# Develop a program that reads the name and two grades of several students and
# stores them all in a composite list. At the end, show a bulletin containing
# the average of each one and allow the user to show the grades of each student
# individually.
group = []
while True:
    group.append(
        [
            input("Name: ").title(),
            float(input("Grade 1: ")),
            float(input("Grade 2: ")),
        ]
    )
    opt = input("Dow you want continue? [Y/N]").strip().upper()[0]
    if "N" in opt:
        break
print("-=" * 16)
print("No.".ljust(4) + "NAME".ljust(20) + "AVERAGE".rjust(7))
print("-" * 32)
for i, student in enumerate(group):
    print(f"{i}".ljust(4), end="")
    print(f"{student[0]}".ljust(20), end="")
    print(f"{(student[1] + student[2]) / 2}".rjust(7), end="")
    print("")
print("-" * 32)
while True:
    opt = int(input("Show grades for which student? (999 to stop)"))
    if opt != 999:
        if opt > (len(group) - 1):
            pass
        else:
            print(
                f"{group[opt][0]}'s grades: {group[opt][1]} and {group[opt][2]}"
            )
            print("-" * 32)
    else:
        break
