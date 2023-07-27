# Make an algorithm to read a number and show your double, triple and
# square root:

import math

number = int(input("Type a number: "))
print("The double of {} is {}".format(number, number * 2))
print("The triple of {} is {}".format(number, number * 3))
print("The square root of {} is {:.2f}".format(number, math.sqrt(number)))
# Obs: You too can utilize the method pow(number,(1/2)) to calc square root
# without import math
