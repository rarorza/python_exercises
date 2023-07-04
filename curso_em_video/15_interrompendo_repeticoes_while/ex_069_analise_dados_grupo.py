# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homes foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

maioridade = 0
homens = 0
mulher_menos_20_anos = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)

    idade = int(input("Idade: "))
    if idade >= 18:
        maioridade += 1

    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo: [M/F] ").strip().upper()[0]
    print("-" * 30)
    if sexo in "M":
        homens += 1
    if sexo in "F" and idade < 20:
        mulher_menos_20_anos += 1

    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? [S/N] ").strip().upper()[0]
    if opcao in "N":
        break
    elif opcao in "S":
        continue

print(f"""
Total de pessoas com mais de 18 anos é {maioridade}.
Ao todo temos homens {homens} cadastrados.
Temos {mulher_menos_20_anos} mulheres com menos de 20 anos.
""")
