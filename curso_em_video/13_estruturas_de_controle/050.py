# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma = 0
contador = 0

print("Digite seis números inteiros pares")
for i in range(1, 7):
    print(f"Digite o {i}° número: ", end="")
    num = int(input(""))
    if num % 2 == 0:
        soma += num
        contador += 1

print(f"Foram somados {contador} números pares, sendo a soma total {soma}")
