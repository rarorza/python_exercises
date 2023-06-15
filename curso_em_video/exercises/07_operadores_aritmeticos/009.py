# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada

multiplicando = int(input("Digite um número para ver sua tabuada: "))
multiplicador = 1

print("---------------")

while multiplicador <= 10:
    resultado = multiplicando * multiplicador
    print("{} x {} = {}".format(multiplicando, multiplicador, resultado))
    multiplicador += 1

print("---------------")
