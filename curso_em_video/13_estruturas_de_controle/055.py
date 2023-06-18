# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

pesos = []

for pessoa in range(1, 5 + 1):
    pesos.append(float(input(f"Peso da {pessoa} pessoa: ")))

print(f"O maior peso lido foi de {max(pesos)}")
print(f"O menor peso lido foi de {min(pesos)}")
