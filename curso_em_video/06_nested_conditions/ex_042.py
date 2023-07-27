# Redo the challenge 035 of the triangles, adding the feature of showing what
# kind of triangle will be formed:
#
# Equilateral: all sides equal
# Isosceles: two equal sides
# Scalene: all different sides

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
    if side_a == side_b == side_c:
        print("The above segments CAN FORM an EQUILATERAL TRIANGLE")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("The above segments CAN FORM an ISOSCELES TRIANGLE")
    else:
        print("The segments above CAN FORM a SCALENE TRIANGLE")
else:
    print("The above segments CANNOT form a triangle")
