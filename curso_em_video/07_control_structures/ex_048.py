# Develop a program that calculates the sum of all odd numbers that are
# multiples of 3 and are in the range 1 to 500.

sum = 0
count = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        sum += i
        count += 1

print(f"The sum of all requested {count} values is {sum}")
