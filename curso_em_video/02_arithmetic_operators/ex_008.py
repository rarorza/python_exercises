# Develop a program to read a value in meters and display it converted to
# centimeters and millimeters.

meters = float(input("The distance in meters: "))
print(f"""
The average in {meters}m correspond to
{meters / 1000}km
{meters / 100}hm
{meters / 10}dam
{meters * 10:.0f}dm
{meters * 100:.0f}cm
{meters * 1000:.0f}mm
""")