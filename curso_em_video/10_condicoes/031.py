# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 200km
# e R$0,45 para viagens mais longas.

km = float(input("Qual a distância da viagem em Km? "))
viagem_curta = 0.50
viagem_longa = 0.45
print(f"Você está prestes a começar uma viagem de {km}Km")

# if km <= 200:
#     valor_total = km * viagem_curta
# else:
#     valor_total = km * viagem_longa

valor_total = km * viagem_curta if km <= 200 else km * 0.45

print("E o preço da sua passagem será de R${:.2f}".format(valor_total))
