# Develop a program that has a function called area(), which receives the
# dimensions of a rectangular terrain (width and height) and shows the area of
# the terrain.


def area(width, height):
    return width * height


print("Terrain Control")
print("-" * 15)
width = float(input("Width (m): "))
height = float(input("Height (m): "))
print(f"The area of a plot {width} x {height} is {area(width, height):.1f}m²")
