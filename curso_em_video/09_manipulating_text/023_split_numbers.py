# Develop a program to read a number in between 0 and 9999 and display it each
# of the digits separated
#
# Example:
# Type a number: 1834
# Units: 4
# Tens: 3
# Hundreds: 8
# Thousands: 1

number = input("Type a number: ")
justified_number = number.rjust(4, "0")

print(f"Parsing the number {number}")
print(
    f"""
      Units: {justified_number[3]}
      Tens: {justified_number[2]}
      Hundreds: {justified_number[1]}
      Thousands: {justified_number[0]}
      """
)
