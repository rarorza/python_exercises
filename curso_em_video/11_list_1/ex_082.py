# Develop a program that will read several numbers and put them in a list. After
# that, create two extra lists that will count only the even and odd values
# entered, respectively. At the end, show the contents of the three generated
# lists.

nums = []
even = []
odd = []

while True:
    num = int(input("Enter a number: "))
    nums.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    answer = input("Do you want continue? (y/n): ").strip().lower()
    if "n" in answer:
        break
print("-=" * 30)
print(f"The complete list is {nums}")
print(f"The even list is {even}")
print(f"The odd list is {odd}")
