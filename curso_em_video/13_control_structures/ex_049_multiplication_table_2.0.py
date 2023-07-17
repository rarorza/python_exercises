# Redo challenge 009, showing the table of a number that the user chooses, only
# now using a for loop.

num = int(input("Type a number: "))

for multiplier in range(1, 10 + 1):
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")
