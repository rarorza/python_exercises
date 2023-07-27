# Develop a program that reads four values and stores them in a tuple. At the
# end, show:
#
# a) How many times did the value 9 appear.
# b) In what position was the first value 3 entered.
# c) What were the even numbers.
array = []
for i in range(1, 5):
    num = int(input(f"Type {i}° value: "))
    array.append(num)
list_tuple = tuple(array)
del array

print(f"The number 9 appeared {list_tuple.count(9)} times")
if 3 in list_tuple:
    print(f"The number 3 first appears in position {list_tuple.index(3) + 1}")
else:
    print("The number 3 did not appear")
print("The even values entered were ", end="")
for i in list_tuple:
    if i % 2 == 0:
        print(f"{i}", end=" ")
print("")
