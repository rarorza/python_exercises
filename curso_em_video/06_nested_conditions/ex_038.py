# Develop a program that reads two integers and compares them by displaying a
# message on the screen:
# - The first value is greater
# - The second value is higher
# - There is no greater value, both are equal
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if num1 > num2:
    print("The FIRST value is higher")
elif num2 > num1:
    print("The SECOND value is higher")
else:
    print("The two values are the SAME")
