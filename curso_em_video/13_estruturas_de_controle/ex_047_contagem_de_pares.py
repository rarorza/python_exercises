# Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50.

# for i in range(0, 50 + 1, 2):
#     print(f" {i} ", end="")
# print("Acabou")

for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("Acabou")
