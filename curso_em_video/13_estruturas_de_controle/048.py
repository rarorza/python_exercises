# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3 e que se encontram no
# intervalo de 1 e 500.

soma = 0
contador = 0

for i in range(1, 501):
    #  se i é multiplo de 3 e diferente de par
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        contador += 1

print(f"A soma de todos os {contador} valores solicitados é {soma}")
