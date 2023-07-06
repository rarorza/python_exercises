# Develop a program where the user can type several num values and register
# them in a list. If the number already exists there, it will not be added. At
# the end, all unique values entered will be displayed, in ascending order.

nums = []

while True:
    num = int(input("Type a number: "))
    if num in nums:
        print("Duplicate value! I will not add")
    else:
        nums.append(num)
        print("Successfully added value!")
    option = input("Do you want to continue? [y/n] ").strip().lower()[0]
    if "n" in option:
        print("=-" * 20)
        print(f"You entered the values {sorted(nums)}")
        break
