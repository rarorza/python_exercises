# Develop a program that has a list called numbers and two functions called
# sort() and sumEven(). The first function will draw 5 numbers and place them in
# a list and the second function will show the sum of all the EVEN values drawn
# by the previous function.
from random import randint


def sort():
    nums = []
    print("Drawing 5 values from the list: ", end="")
    for i in range(0, 5):
        num = randint(1, 10)
        print(f"{num}", end=" ")
        nums.append(num)
    print("Ready!")
    return nums


def sumEven(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    print(f"Adding the even values of {nums}, we have {sum}")


sumEven(sort())
