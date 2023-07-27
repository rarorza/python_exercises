# Develop a program that reads several integers from the keyboard. The program
# will only stop when the user types the value 999, which is the stop condition.
# At the end, show how many numbers were entered and what was the sum between
# them (disregarding the flag).

count = sum = 0
while True:
    num = int(input("Enter a value (999 to stop): "))
    if num == 999:
        break
    sum += num
    count += 1
print(f"The sum of the {count} was {sum}")
