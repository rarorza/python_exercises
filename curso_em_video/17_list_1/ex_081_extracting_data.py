# Create a program that will read several numbers and put them in a list. After
# that show:
# a) How many numbers were entered.
# b) The list of values, sorted in descending order.
# c) If the value 5 was typed and is or is not in the list.

nums = []

while True:
    num = int(input("Enter a number: "))
    nums.append(num)
    answer = input("Do you want continue? (y/n): ").strip().lower()
    if "n" in answer:
        break
print("-=" * 30)
print(f"You entered {len(nums)} numbers.")
print(f"The list is {sorted(nums, reverse=True)}")
if 5 in nums:
    print("The value 5 was entered")
else:
    print("The value 5 was not entered")
