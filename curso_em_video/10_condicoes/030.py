# Crie um programa que leia um número inteiro e mostre na tela se é PAR ou IMPAR.

numero = int(input("Me diga um número qualquer: "))
resultado = numero % 2
if resultado == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é IMPAR")
