# Develop a program to read a full name of a person:
# - The name with all letters to upper case
# - The name with all letters to lower case
# - How many letters does it have (without considering spaces)
# - How many letters are in the first name

name = input("Type your full name: ")
first = name.split()[0]
name_without_space = name.replace(" ", "")
# It is possible to use the count method to subtract spaces from the total
# number of the length.
# Example: len(nome) - nome.count' '

print(f"Your full name in lower case is {name.lower()}")
print(f"Your full name in upper case is {name.upper()}")
print(f"Your full name has a total of {len(name_without_space)} letters")
print(
    f"Your 1° name is {first.title()} and it has {len(first[0])} letters")
