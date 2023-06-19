# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
homem_mais_velho = ""
mulheres_novas = 0

for pessoa in range(1, 4 + 1):
    print(f"----- {pessoa}ª PESSOA -----")
    nome = input("Nome: ").title().strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    soma_idade += idade
    if sexo == "M":
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            homem_mais_velho = nome
    elif sexo == "F":
        if idade <= 20:
            mulheres_novas += 1
    else:
        sexo = ""


media_idade = soma_idade / 4
print(f"A média de idade do grupo é de {media_idade} anos")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {homem_mais_velho}")
print(f"Ao todo existe(m) {mulheres_novas} mulher(es) com menos de 20 anos")
