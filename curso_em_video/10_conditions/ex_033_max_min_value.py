# Develop a program to read 3 numbers and display it which is smaller

num1 = input("First value: ")
num2 = input("Second value: ")
num3 = input("Third value: ")
nums = [num1, num2, num3]

min_num = min(nums, key=int)
max_num = max(nums, key=int)

print(f"Min: {min_num}")
print(f"Max: {max_num}")
