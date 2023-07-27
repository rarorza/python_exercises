# Develop a program that reads any year and shows if it is a leap year

from datetime import date

year = int(
    input("What year do you want to analyze? Put 0 to parse the current year: ")
)

if year == 0:
    year = date.today().year  # current year

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
