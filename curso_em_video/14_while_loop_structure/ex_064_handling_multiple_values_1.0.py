# Develop a program that reads several integers from the keyboard. The program
# only stops when the user enters the value 999, which is a stop condition. At
# the end, show how many numbers were entered and what was the sum between them
# (disregarding the 999 flag).

accumulator = count = 0

while True:
    num = int(input("Enter a number [999 to stop]: "))
    if num != 999:
        accumulator += num
        count += 1
    else:
        break
print(f"You typed {count} and the sum between them was {accumulator}.")
