# Develop a program that reads any integer N and displays the first N elements
# of a Fibonacci sequence on the screen.
#
# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

print("-" * 26)
print("FIBONACCI SEQUENCE".center(26))
print("-" * 26)

first_term = count = 0
second_term = 1
final_term = int(input("How many terms do you want to show? "))
print(f"{first_term} -> {second_term} -> ", end="")
while count != final_term:
    fibonacci = first_term + second_term
    first_term = second_term
    second_term = fibonacci
    count += 1
    print(f"{fibonacci}", end=" -> ")
print("END!")
