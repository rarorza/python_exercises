# Find all of the numbers from 1-1000 that are divisible by 7

numbers_list = [value for value in range(1, 1001)]

result = [number for number in numbers_list if number % 7 == 0]

print(result)
