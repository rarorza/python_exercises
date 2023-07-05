# Develop a program that will generate 5 random numbers (between 1 and 9) and
# put them in a tuple. After that, show the list of generated numbers and also
# indicate the smallest and largest values that are in the tuple.

import random

secret_numbers_list = []

for i in range(0, 5):
    secret = random.randint(1, 9)
    secret_numbers_list.append(secret)

secret_numbers_tuple = tuple(secret_numbers_list)
del secret_numbers_list
print(secret_numbers_tuple)
print(f"Max: {max(secret_numbers_tuple)} \nMin: {min(secret_numbers_tuple)}")
