# Develop a program that reads six integers and prints the sum of only those
# that are even. If the entered value is odd, disregard it.

print("Enter six even integers")
sum = 0
count = 0
for i in range(1, 7):
    print(f"Enter the {i}st number: ", end="")
    num = int(input(""))
    if num % 2 == 0:
        sum += num
        count += 1

print(f"{count} even numbers were added, the total sum being {sum}")
