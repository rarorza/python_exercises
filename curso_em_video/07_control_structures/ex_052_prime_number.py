# Develop a program that reads an integer and tells whether or not it is a prime
# number.

count = 0
num_list = []

while True:
    num = int(input("Type a number: "))
    if num >= 2:
        for divisor in range(1, num + 1):
            num_list.append(f"{divisor}")
            if num % divisor == 0:
                count += 1
                num_list.remove(f"{divisor}")
                num_list.insert(divisor, f"\033[1;31m{divisor}\033[m")
        for item in num_list:
            print(f"{item}", end=" ")

        print(f"\nThe number {num} was divisible by {count} times")
        if count == 2:
            print("And that's why it's a PRIME NUMBER!")
            break

        if count > 2:
            print("And that's why IT'S NOT A PRIME NUMBER!")
            break
    else:
        print("The number must be greater than 1")
        continue
