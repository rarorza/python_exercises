# Develop a program that displays all even numbers between 1 and 50 on the
# screen.

# for i in range(0, 50 + 1, 2):
#     print(f" {i} ", end="")
# print("Acabou")

for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("END")
