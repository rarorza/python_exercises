# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

import math

numero = int(input("Digite um número: "))
print("O dobro de {} é {}".format(numero, numero * 2))
print("O triplo de {} é {}".format(numero, numero * 3))
print("A raiz quadrada de {} é igual a {:.2f}".format(numero, math.sqrt(numero)))
# Também poderia ter utilizado o metodo pow(numero,(1/2)) para calcular a raiz
# quadrada sem o import math
