# Develop a program that asks for an employee's salary and calculates the amount
# of his increase. For salaries greater than R$ 1,250.00, calculate a 10%
# increase. For lower or equal salaries, the increase is 15%.

salary = float(input("What is the employee's salary? $"))

if salary <= 1250:
    increase = (salary * 0.15) + salary
else:
    increase = (salary * 0.10) + salary

print(f"Those who used to earn ${salary:.2f} now earn ${increase:.2f}")
