# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    print("=" * 35)
    print("BANCO CEV".center(35))
    print("=" * 35)
    valor_saque = int(input("Que valor você quer sacar? R$"))
    count_50 = count_20 = count_10 = count_1 = 0
    while 50 <= valor_saque:
        valor_saque -= 50
        count_50 += 1
    if count_50 > 0:
        print(f"Total de {count_50} de R$50")
    while 20 <= valor_saque:
        valor_saque -= 20
        count_20 += 1
    if count_20 > 0:
        print(f"Total de {count_20} de R$20")
    while 10 <= valor_saque:
        valor_saque -= 10
        count_10 += 1
    if count_10 > 0:
        print(f"Total de {count_10} de R$10")
    while 1 <= valor_saque:
        valor_saque -= 1
        count_1 += 1
    if count_1 > 0:
        print(f"Total de {count_1} de R$1")
    break
print("=" * 35)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
