# Develop a program that reads a student's name and average, also saving the
# situation in a dictionary. At the end, show the contents of the structure on
# the screen.
student = {"Name": input("Name: "), "Average": float(input("Average: "))}
student["Situation"] = (
    "Pass"
    if student["Average"] >= 7
    else "Fail"
    if student["Average"] < 6
    else "Recovery"
)
print("-=" * 15)
print(f"- Name: {student['Name'].title()}")
print(f"- Average: {student['Average']}")
print(f"- Situation: {student['Situation']}")
