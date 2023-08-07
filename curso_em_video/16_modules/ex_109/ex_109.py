# Modify the functions that were created in challenge 107 so that they accept
# one more parameter, informing whether or not the value returned by them will
# be formatted by the coin() function, developed in challenge 108

from coin import increase, decrease, double, half, coin

num = float(input("Enter a price: R$"))
print(f"Half of {coin(num)} is {half(num, format=True)}")
print(f"Double {coin(num)} is {double(num, format=True)}")
print(f"Increase of 10%, we have {increase(num, 0.1, format=True)}")
print(f"Decrease of 10%, we have {decrease(num, 0.1, format=True)}")
