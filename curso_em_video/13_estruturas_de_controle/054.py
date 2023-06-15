# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date

anos = []
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for i in range(1, 7 + 1):
    anos.append(input(f"Digite o {i}° ano de nascimento: "))

for ano in anos:
    if ano_atual - ano >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"Ao todo tivemos {maior_idade} pessoa(s) maior(es) de idade")
print(f"E {menor_idade} pessoa(s) menor(es) de idade")
