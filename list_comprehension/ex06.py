# Get the index and the value as a tuple for items in the list:
# ["hi", 4, 8.99, 'apple', ('t,b','n')].
# Result would look like [(index, value), (index, value)]

values = ["hi", 4, 8.99, "apple", ("t,b", "n")]
result = [(i, value) for i, value in enumerate(values) if value]

print(result)
