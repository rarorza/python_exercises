# Given a list of numbers, remove floats

original_list = [2, 3.75, 0.04, 59.354, 6, 7.7777, 8, 9]
result = [number for number in original_list if type(number) == int]

print(result)
