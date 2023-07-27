# Develop a program that reads any integer and asks the user what the conversion
# base will be:
#
# 1 for binary
# 2 for octal
# 3 for hexadecimal

# Obs: this whole problem could have been solved with the hex(), oct() and bin()
# functions, but I thought it would be cool to make my own converter.

num = input("Type an integer: ")
print(
    """Choose one of the bases for conversion:
[ 1 ] convert to BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL
"""
)

option = int(input("Choose your option: "))
result = 1
rest = []
num_int = int(num)
hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

if option == 1:
    while result >= 1:
        rest.append(num_int % 2)
        result = num_int // 2
        num_int = result
    rest.reverse()
    print(f"{num} converted to BINARY is equal to ", end="")
    for i in range(len(rest)):
        print(rest[i], end="")
    print("")
elif option == 2:
    while result >= 1:
        rest.append(num_int % 8)
        result = num_int // 8
        num_int = result
    rest.reverse()
    print(f"{num} converted to OCTAL is equal to ", end="")
    for i in range(len(rest)):
        print(rest[i], end="")
    print("")
elif option == 3:
    while result >= 1:
        hexa = num_int % 16
        if hexa >= 10:
            rest.append(hexadecimal.get(hexa))
        else:
            rest.append(num_int % 16)
        result = num_int // 16
        num_int = result
    rest.reverse()
    print(f"{num} converted to HEXADECIMAL is equal to ", end="")
    for i in range(len(rest)):
        print(rest[i], end="")
    print("")
else:
    print("Opção inválida!")
