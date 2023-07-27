# Improve the previous challenge, showing at the end:
# a) The sum of all even values entered.
# b) The sum of the values in the third column.
# c) The largest value in the second row.

matrix = [[], [], []]
EVEN_SUM = THIRD_COLUMN = 0

for row in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Type a value to [{row}, {i}]: "))
        matrix[row].append(num)
print("-=" * 30)
for row in matrix:
    for i, value in enumerate(row):
        if value % 2 == 0:
            EVEN_SUM += value
        if i == 2:
            THIRD_COLUMN += value
        print(f"[{value:^5}]", end="")
    print("")
print("-=" * 30)
print(f"The sum of all even values entered: {EVEN_SUM}")
print(f"The sum of the values in the third column: {THIRD_COLUMN}")
print(f"The largest value in the second row: {max(matrix[1])}")
