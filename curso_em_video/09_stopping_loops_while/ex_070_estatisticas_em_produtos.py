# Crie um programa que leia o nome e o preço de vários produtos. O produto deverá perguntar se o
# usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$ 1000.
# c) Qual é o nome do produto mais barato.
soma_preco = 0
mil_reais = 0
mais_barato = 0

print("-" * 30)
print("LOJA SUPER BARATÃO".center(30))
print("-" * 30)
while True:
    produto = input("Nome do produto: ").strip().capitalize()

    preco = float(input("Preço: R$"))
    soma_preco += preco
    if preco > 1000:
        mil_reais += 1
    if mais_barato < 1 or preco < mais_barato:
        mais_barato = preco
        nome_produto_barato = produto

    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? [S/N]").strip().upper()[0]
    if opcao in "N":
        break

print("{:-^30}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R${soma_preco:.2f}")
print(f"Temos {mil_reais} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_produto_barato} que custa R${mais_barato:.2f}")
