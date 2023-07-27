# Develop a program to read the speed of a car. If the car exceeds 80 km/h, show
# a message saying that it was fined. The fine will cost $7.00 for each km over
# the limit.

speed = float(input("Qual a velocidade atual do carro? "))
speed_limit = 80
price_per_km = 7
fined = (speed - speed_limit) * price_per_km


if speed > speed_limit:
    print(
        f"""
        FINED! You have exceeded the permitted limit which is {speed_limit}km/h
        You must pay a fine of ${fined:.2f}!
          """
    )
print("Have a good day! Drive safe!")
