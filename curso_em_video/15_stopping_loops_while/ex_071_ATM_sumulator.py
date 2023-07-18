# Create a program that simulates the operation of an ATM. At first, ask the
# user what will be the amount to be withdrawn (integer number) and the program
# will inform how many bills of each value will be delivered.
#
# Note: Consider that the cashier has bills of $50, $20, $10 and $1.

print("=" * 35)
print("CEV BANK".center(35))
print("=" * 35)
withdraw = int(input("What amount do you want to withdraw? $"))
count_50 = count_20 = count_10 = count_1 = 0
while 50 <= withdraw:
    withdraw -= 50
    count_50 += 1
if count_50 > 0:
    print(f"Total of {count_50} $50 bills")
while 20 <= withdraw:
    withdraw -= 20
    count_20 += 1
if count_20 > 0:
    print(f"Total of {count_20} $20 bills")
while 10 <= withdraw:
    withdraw -= 10
    count_10 += 1
if count_10 > 0:
    print(f"Total of {count_10} $10 bills")
while 1 <= withdraw:
    withdraw -= 1
    count_1 += 1
if count_1 > 0:
    print(f"Total of {count_1} $1 bills")
print("=" * 35)
print("Always come back to CEV BANK! Have a good day!")
