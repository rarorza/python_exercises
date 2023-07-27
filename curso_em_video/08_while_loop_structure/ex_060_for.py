# Develop a program that reads any number and shows its factorial.
#          20 60 120
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input("Enter a number to calculate your factorial: "))
factorial = 1

for i in range(1, num + 1, +1):
    factorial *= i
    print(factorial)
