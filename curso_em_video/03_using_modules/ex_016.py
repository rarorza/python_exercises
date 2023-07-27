# Create a program that reads any real number from the keyboard and displays its
# entire portion on the screen.
# Ex: Enter a number: 6.127
# The number 6.127 has the integer part 6.
num = float(input("Type a float number: "))
print(f"The value entered was {num} and its integer portion is {int(num)}")
