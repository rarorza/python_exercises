# Develop a program that reads the length of three lines and tells the user
# whether or not they can form a triangle.

print("-=" * 10)
print("Triangle Analyzer".center(20))
print("-=" * 10)

side_a = float(input("First side: "))
side_b = float(input("Second side: "))
side_c = float(input("Third side: "))

if (
    (side_a + side_b) > side_c
    and (side_a + side_c) > side_b
    and (side_b + side_c) > side_a
):
    print("The above segments CAN FORM a triangle")
else:
    print("The above segments CANNOT form a triangle")
