# Develop a program to read a int number e display it even or odd

number = int(input("Tell me a number: "))
result = number % 2
if result == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
