# Adapt the code from challenge 107, creating an additional function called
# coin(), which can show values as a formatted monetary value. Swapping a dot
# for a comma.
# For example: R$ 10,00

from coin import increase, decrease, double, half, coin

num = float(input("Enter a price: R$"))
print(f"Half of {coin(num)} is {coin(half(num))}")
print(f"Double {coin(num)} is {coin(double(num))}")
print(f"Increase of 10%, we have {coin(increase(num, 0.1))}")
print(f"Decrease of 10%, we have {coin(decrease(num, 0.1))}")
