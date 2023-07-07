# Develop a program where the user can enter five numerical values and register
# them in a list, already in the correct insertion position, without using
# sort(). At the end, show the sorted list on the screen.

nums = []
for count in range(0, 5):
    num = int(input("Type a value: "))
    if len(nums) == 0:
        higher = lower = num
        nums.append(num)
        print("Add in end of list.")
    else:
        if lower > num:
            lower = num
            nums.insert(0, lower)
            print(f"Add in position {nums.index(lower)}")
            continue
        if higher < num:
            higher = num
            nums.append(num)
            print("Add in end of list.")
            continue
        for i, n in enumerate(nums):
            if i == 0:
                pass
            else:
                if n > num:
                    nums.insert(i, num)
                    print(f"added at position {nums.index(num)} of the list")
                    break
print(nums)
