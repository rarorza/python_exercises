# Car rent:

# Develop a program to ask the distance in Km traveled by a rented car and the
# number of days for which it was rented.

# Calc the price to pay, knowing that the car costs $60 per day and $0.15 per Km
# driven.

rent_days = int(input("How many days was the car rented? "))
driven_km = float(input("How many Km were traveled? "))
day_costs = 60
km_costs = 15
total_pay_per_day = day_costs * rent_days
total_pay_per_km = (km_costs / 100) * driven_km

print(f"The total to pay is ${total_pay_per_km + total_pay_per_day:.2f}")
