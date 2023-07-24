# Create a program that reads name, year of birth and work card number. Register
# them (with age) in a dictionary, if by chance the work card is different from
# ZERO, the dictionary will also receive the year of hiring and the salary.
# Calculate and add in addition to age, how old the person will retire.
from datetime import date

worker = {}
worker["Name"] = input("Name: ")
worker["Year of birth"] = int(input("Year of birth: "))
worker["Work card"] = input("Work card number (0 don't have): ").strip()[0]
worker["Age"] = date.today().year - worker["Year of birth"]
if int(worker["Work card"]) != 0:
    worker["Year of hire"] = int(input("Year of hire: "))
    worker["Salary"] = float(input("Salary: $"))
    worker["Retirement age"] = (worker["Year of hire"] + 35) - worker[
        "Year of birth"
    ]
print("=" * 30)
for key, value in worker.items():
    print(key, value)
