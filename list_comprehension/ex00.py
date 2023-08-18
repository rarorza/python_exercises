# Given a list of numbers, remove all odd numbers from the list:

numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]

result = [number for number in numbers if number % 2 == 0]

print(result)

# Explaining syntax
#
# [output_expression() for(set of values to iterate) if(conditional filtering)]
