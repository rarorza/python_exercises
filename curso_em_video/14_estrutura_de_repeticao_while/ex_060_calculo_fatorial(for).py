# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#          20 60 120
# Ex: 5! = 5x4x3x2x1 = 120

num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1

for i in range(1, num+1, +1):
    fatorial *= i
    print(fatorial)