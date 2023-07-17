# Develop a program that reads several integers from the keyboard. At the end of
# the Run, show the mean of all values and what was the highest and lowest
# values read. The program should ask the user whether or not he wants to
# continue typing values.

sum = count = 0
num = int(input("Enter a number: "))
biggest = num
smallest = num

while True:
    sum += num
    count += 1

    if num > biggest:
        biggest = num
    elif num < smallest:
        smallest = num

    option = str(input("Do you want to continue? [Y/N] ").upper().split())
    if option in "Y":
        num = int(input("Enter a number: "))
    elif option in "N":
        break
    else:
        print("Invalid option!")
        break

average = sum / count
print(f"You entered {count} numbers and the average was {average:.2f}")
print(f"The biggest value was {biggest} and the smallest was {smallest}")
