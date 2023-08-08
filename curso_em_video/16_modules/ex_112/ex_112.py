# Within the utilities package we created in the 111 challenge, we have a module
# called data. Create a function called readMoney() that is able to work like
# the input() function, but with data validation to only accept values that are
# monetary.

from utilities import data

price = data.readMoney("Enter a price: R$")
increase = int(input("Increase: ")) / 100
decrease = int(input("Decrease: ")) / 100
data.resume(price, increase, decrease)
