# Write a program that has a function called counter(), which takes three
# parameters: start, end and step. Your program has to perform three counts
# through the created function:
# a) From 1 to 10, from 1 to 1.
# b) From 10 to 0, from 2 to 2.
# c) A custom count.
# Obs1: if the step is 0, it must be considered as 1
# Obs2: if the step is negative, it must be converted to positive
from time import sleep


def counter(start, end, step):
    if step == 0:
        step = 1
        print("Step cannot be 0")
    print(f"Counting from {start} to {end} by {abs(step)} by {abs(step)}")
    while start != end:
        if start < end:
            print(f"{start}", end=" ", flush=True)
            start += abs(step)
            sleep(0.2)
            if start > end:
                break
        if start > end:
            print(f"{start}", end=" ", flush=True)
            start -= abs(step)
            sleep(0.2)
            if start < end:
                break
    print(f"{end} END!")


counter(1, 10, 1)
counter(10, 0, 2)
print("Now its your time!")
counter(int(input("Start: ")), int(input("End: ")), int(input("Step: ")))
