# Develop a program that creates a 3x3 dimension matrix and fills it with values
# read from the keyboard.
# In the end, show the matrix on the screen, with the correct formatting.

matrix = [[], [], []]

for row in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Type a value to [{row}, {i}]: "))
        matrix[row].append(num)
print("-=" * 30)
for row in matrix:
    for i in row:
        print(f"[{i:^5}]", end="")
    print("")
