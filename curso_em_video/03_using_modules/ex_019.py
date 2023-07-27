# A teacher wants to draw one of his four students to erase the blackboard. Make
# a program that helps him, reading their name and writing the name of the
# chosen one.
from random import choice

students = []
for i in range(0, 4):
    student = input(f"{i + 1}° student: ")
    students.append(student)
chosen = choice(students)
print(f"The chosen student was {chosen}")
