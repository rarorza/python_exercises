# Write a program that reads the length of the opposite and adjacent sides of a
# right triangle, calculates and displays the length of the hypotenuse.
from math import hypot

side_opposite = float(input("Opposite leg length: "))
side_adjacent = float(input("Adjacent leg length: "))
hypotenuse = hypot(side_opposite, side_adjacent)
print(f"The hypotenuse will measure {hypotenuse:.2f}")
