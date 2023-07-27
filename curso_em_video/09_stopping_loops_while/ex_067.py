# Develop a program that displays the table of several numbers, one at a time,
# for each value entered by the user. The program will stop when the requested
# number is negative.

count = 1
while True:
    num = int(input("Do you want to see the table of what value? "))
    print("-" * 35)
    if num < 1:
        break
    while count <= 10:
        multiplication = num * count
        print(f"{num} x {count} = {multiplication}")
        count += 1
    print("-" * 35)
    count = 1
print("TABLES PROGRAM CLOSED. Check back often!")
