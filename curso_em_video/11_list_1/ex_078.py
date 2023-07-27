# Develop a program that reads 5 numerical values and stores them in a list. At
# the end, show which was the highest and lowest value typed and their
# respective positions in the list.
# nums = list()

nums = []
for i in range(0, 5):
    num = int(input(f"Type a number to the position {i}: "))
    nums.append(num)
maxi = max(nums)
mini = min(nums)

print(f"The highest value was {maxi} at position", end=" ")
for i, num in enumerate(nums):
    if num == maxi:
        print(f"{i}...", end=" ")

print(f"\nThe highest value was {mini} at position", end=" ")
for i, num in enumerate(nums):
    if num == mini:
        print(f"{i}...", end=" ")
print("")
