# The National Swimming Confederation needs a program that reads the year of
# birth of an athlete and shows his category, according to age:
#
# - Up to 9 years: MIRIM
# - Up to 14 years: CHILDREN
# - Up to 19 years old: JUNIOR
# - Up to 25 years old: SENIOR
# - Above: MASTER

from datetime import date

current_year = date.today().year
birth_year = int(input("Year of birth: "))
age = current_year - birth_year


if birth_year <= current_year:
    print(f"The athlete is {age} years old")
    if age <= 9:
        print("Rating: MIRIM")
    elif age <= 14:
        print("Rating: CHILDREN")
    elif age <= 19:
        print("Rating: JUNIOR")
    elif age <= 25:
        print("Rating: SENIOR")
    else:
        print("Rating: MASTER")
else:
    print("Invalid information")
