# Develop a program that reads two values and displays a menu on the screen.
#
# Ex:
# [ 1 ] sum
# [ 2 ] multiply
# [ 3 ] bigger
# [ 4 ] new numbers
# [ 5 ] exit the program
#
# Your program should perform the requested operation in each case.

from time import sleep

num1 = int(input("First value: "))
num2 = int(input("Second value: "))
option = 0

while True:
    print(
        """
[ 1 ] sum
[ 2 ] multiply
[ 3 ] bigger
[ 4 ] new numbers
[ 5 ] exit the program
          """
    )
    option = int(input("What's your option? "))

    if option == 1:
        sum = num1 + num2
        print(f"The sum between {num1} + {num2} = {sum}")
    elif option == 2:
        multiply = num1 * num2
        print(f"The multiplication between {num1} x {num2} = {multiply}")
    elif option == 3:
        if num1 > num2:
            biggest = num1
        else:
            biggest = num2
        print(f"Between {num1} and {num2} the biggest value is {biggest}")
    elif option == 4:
        print("Enter the numbers again")
        num1 = int(input("First value: "))
        num2 = int(input("Second value: "))
    elif option == 5:
        print("Finishing...")
        break
    else:
        print("Invalid option, try again.")

    print("=-=" * 11)
    sleep(2)

print("End of program! Check back often!")
