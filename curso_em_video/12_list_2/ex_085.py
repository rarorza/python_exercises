# Develop a program where the user can enter seven numeric values and register
# them in a single list that keeps even and odd values separate. At the end show
# the even and odd values in ascending order.

nums = [[], []]
for i in range(1, 8):
    num = int(input(f"Type {i}º value: "))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print(f"Even values: {nums[0]}")
print(f"Odd values: {nums[1]}")
