# Develop a program that reads name and weight of several people, keeping
# everything in a list. At the end, show:
#
# a) How many people were registered
# b) A list of the heaviest people.
# c) A list of the lightest people.

max_weight = min_weight = 0
people = []

while True:
    name = input("Name: ")
    weight = float(input("Weight: "))
    people.append([name, weight])
    if max_weight == 0:
        max_weight = min_weight = weight
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight
    option = input("Do you want to continue? [Y/N] ").strip().upper()[0]
    if "N" in option:
        break
print("-=" * 30)
print(f"In total, you registered {len(people)} people")
print(f"The highest weight was {max_weight}Kg. weight of ", end="")
for person in people:
    if max_weight == person[1]:
        print(f'{person[0]}', end=" ")
print("")
print(f"The smallest weight was {min_weight}Kg. weight of ", end="")
for person in people:
    if min_weight == person[1]:
        print(f'{person[0]}', end=" ")
print("")
