# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#          20 60 120
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1

print(f"Calculando {num}!= {num} ", end="")

while num > 1:
    fatorial *= num
    num -= 1
    print(f"x {num} ", end="")
print(f'= {fatorial}')
