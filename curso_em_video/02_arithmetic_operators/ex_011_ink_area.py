# Make a program that reads the width and height of a wall in meters, calculates
# its area and the amount of paint needed to paint it, knowing that each liter
# of paint paints an area of 2m².

width = float(input("Wall width: "))
height = float(input("Wall height: "))
area = width * height
ink = area / 2
print(
    f"Its wall has the dimension of {width}x{height} and its area is {area}m²."
)
print(f"To paint this wall, you will need {ink}l of paint.")
