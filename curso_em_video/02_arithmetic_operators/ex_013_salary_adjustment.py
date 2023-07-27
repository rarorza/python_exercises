# Write an algorithm that reads an employee's salary and outputs their new
# salary, with a 15% increase.

salary = float(input("What is the employee's salary? $"))
new = salary + (salary * 15 / 100)
print(
    f"An employee who earned ${salary:.2f}, with a 15% raise, now earns ${new:.2f}"
)
