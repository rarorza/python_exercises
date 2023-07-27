# Create a program that reads a person's name and says if they have "Smith" in
# their name.

name = input("What's your full name? ")
print(f"Does your name have Smith? {'smith' in name.lower()}")
