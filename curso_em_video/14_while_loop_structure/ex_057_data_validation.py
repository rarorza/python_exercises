# Develop a program that reads a person's gender, but only accepts the values
# 'M' or 'F'. If it is wrong, ask for typing again until you have a correct
# value.

sex = input("Enter your gender: [M/F] ").upper().strip()[0]

while sex not in "MmFf":
    sex = (
        input("Invalid data. Please enter your gender: ")
        .upper()
        .strip()[0]
    )

print(f"{sex} sex successfully registered!")
