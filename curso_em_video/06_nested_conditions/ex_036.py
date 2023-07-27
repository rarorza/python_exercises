# Develop a program to approve the bank loan for the purchase of a house. Ask
# the home's value, the buyer's salary and how many years he will pay. The
# monthly installment cannot exceed 30% of the salary or else the loan will be
# denied.

print("Easy loan!")
salary = float(input("What's your salary? $"))
bank_loan = float(
    input("What is the value of the property? $")
)
years_pay = int(
    input(
        "In how many years do you intend to pay off the loan amount? "
    )
)
loan_limit = salary * 0.30
parcels = bank_loan / (years_pay * 12)

print(f"""
To pay a house of $ {bank_loan:.2f}
in {years_pay} years the installment will be ${parcels:.2f}
""")
if parcels > loan_limit:
    print("Loan Denied!")
elif parcels < loan_limit:
    print("Loan approved!")
