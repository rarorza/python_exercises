# Develop a program that reads the year of birth of a young person and informs,
# according to his age, if he is still going to enlist in the military, if it is
# time to enlist or if it has passed the enlistment time. Your program should
# also show how much time is left or how far past the deadline.

from datetime import date

birth_year = int(input("Ano de nascimento: "))
current_year = date.today().year
age = current_year - birth_year
AGE_MAJORITY = 18
missing_time = AGE_MAJORITY - age
time_exceeded = age - AGE_MAJORITY
enlistment_year = missing_time + current_year


def military():
    if birth_year > current_year:
        print("Invalid option!")
    else:
        print(f"Who was born in {birth_year} has {age} in {current_year}")
        if age > AGE_MAJORITY:
            print(f"Você já deveria ter se alistado há {time_exceeded} ano(s)")
            print(f"You should have enlisted {enlistment_year} years ago")
        elif age < AGE_MAJORITY:
            print(f"There are still {missing_time} years left for enlistment")
            print(f"Your enlistment will be in {enlistment_year}")
        elif age == AGE_MAJORITY:
            print("You must enlist IMMEDIATELY!")


if __name__ == "__main__":
    military()
