# Make a program to read an int number and display it your multiplication table

multiplying = int(input(
    "Type a number to display it in the multiplication table: "
))
multiplier = 1

print("---------------")

while multiplier <= 10:
    result = multiplying * multiplier
    print("{} x {} = {}".format(multiplying, multiplier, result))
    multiplier += 1

print("---------------")
