# Develop a program that reads two grades from a student and calculates their
# average, showing a message at the end, according to the average achieved:
# - Average below 5.0: FAILED
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or higher: PASSED

grade1 = float(input("First grade: "))
grade2 = float(input("Second grade: "))
average = (grade1 + grade2) / 2
print(f"With grades {grade1} and {grade2}, the student's average is {average}")
