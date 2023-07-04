# Develop a program to read a full name and display it the first and
# last name separate.

name = input("Type the full name: ").strip().lower().split()
print(
    f"""
      Your first name is {name[0].capitalize()}
      Your last name is {name[len(name) - 1].capitalize()}
      """
)
