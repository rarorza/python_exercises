# Develop a package called utilities, which has two built-in modules called coin
# and die. Transfer all functions used in challenges 107, 108 and 109 to the
# package and keep everything working.

from utilities import data

price = float(input("Enter a price: R$"))
increase = int(input("Increase: ")) / 100
decrease = int(input("Decrease: ")) / 100
data.resume(price, increase, decrease)
