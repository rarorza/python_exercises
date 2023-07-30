# Create a program that has a function called vote() that will receive the year
# of birth of each person as a parameter, returning a literal value indicating
# whether a person has a DENIED, OPTIONAL or MANDATORY vote in elections.


def vote(born_year):
    from datetime import date

    current_year = date.today().year
    age = current_year - born_year
    print(f"At age {age}:", end=" ")
    if age < 0:
        return "Please enter a valid year"
    elif age < 16:
        return "DENIED VOTE"
    elif 16 <= age < 18 or age >= 70:
        return "OPTIONAL VOTE"
    elif age >= 18:
        return "MANDATOY VOTE"


print(vote(int(input("Born year: "))))
