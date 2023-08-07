# Create a module called coin.py that has built-in functions increase(),
# decrease(), double() and half(). Also make a program that imports this module
# and uses some of these functions.

from coin import increase, decrease, double, half

num = float(input("Enter a price: $"))
print(f"Half of {num} is {half(num)}")
print(f"Double {num} is {double(num)}")
print(f"Increase of 10%, we have {increase(num, 0.1)}")
print(f"Decrease of 10%, we have {decrease(num, 0.1)}")
