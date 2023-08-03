# Create a program that has the readInt() function, which will work similarly to
# Python's input() function, only doing the validation to accept only a numeric
# value.
# Ex:
# n = readInt('Enter a number')


def read_int(text=None):
    while True:
        if text:
            print(text, end="")
        try:
            n = int(input())
            break
        except:
            print("Error! Please enter a valid integer.")
    return n


n = read_int("Enter a number: ")
print(f"You just enter the number {n}")
# Obs: could be solved with isnumeric
