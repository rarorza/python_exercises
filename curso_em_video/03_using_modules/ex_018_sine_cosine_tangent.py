# Make a program that reads any angle and shows on the screen the value of sine,
# cosine and tangent of that angle
from math import radians, sin, cos, tan

angle = float(input("Enter the angle you want: "))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print(f"The angle of {angle} has the sine of {sine:.2f}")
print(f"The angle of {angle} has the cosine of {cosine:.2f}")
print(f"The angle of {angle} has the tangent of {tangent:.2f}")
