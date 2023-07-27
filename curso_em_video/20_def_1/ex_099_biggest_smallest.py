# Develop a program that has a function called bigger(), which receives several
# parameters with integer values. Your program has to look at all the values and
# say which one is the largest.
from time import sleep


def bigger(*nums):
    bigger = 0
    print("-=" * 30)
    print("Analyzing past values...")
    for num in nums:
        print(f"{num}", end=" ", flush=True)
        sleep(0.2)
        if bigger == 0:
            bigger = num
        if num > bigger:
            bigger = num
    print(f"A total of {len(nums)} values were reported")
    print(f"The bigger reported value was {bigger}")


bigger(2, 9, 4, 5, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
