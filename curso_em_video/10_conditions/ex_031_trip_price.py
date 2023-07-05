# Develop a program to ask for the distance of a trip in Km. Calculate the
# ticket price, $0.50 per Km for trips over 200Km and $0.45 for longer trips.

km = float(input("How far is the trip in Km? "))
short_trip = 0.50
long_trip = 0.45
print(f"You are about to start a {km}Km journey")

total_price = km * short_trip if km <= 200 else km * long_trip

print(f"And the price of your ticket will be ${total_price:.2f}")
