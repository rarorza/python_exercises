# Crie um programa que faça o computador jogar pedra, papel e tesoura com você.

import time
import random

print(
    """
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
      """
)
jogadas = ["Pedra", "Papel", "Tesoura"]
sorteio = random.randint(0, 2)
opcao = int(input("Qual é a sua jogada? "))

if opcao <= 2 and opcao >= 0:
    print("JO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PO!!!")
    print("-=" * 15)
    print(f"Computador jogou {jogadas[sorteio - 1]}")
    print(f"Jogador jogou {jogadas[opcao - 1]}")
    print("-=" * 15)

    if opcao == sorteio:
        print("EMPATE!")
    elif (
        (opcao == 0 and sorteio == 1)
        or (opcao == 1 and sorteio == 2)
        or (opcao == 2 and sorteio == 0)
    ):
        print("COMPUTADOR VENCEU!")
    elif (
        (opcao == 0 and sorteio == 2)
        or (opcao == 1 and sorteio == 0)
        or (opcao == 2 and sorteio == 1)
    ):
        print("JOGADOR VENCEU!")
else:
    print("Opção inválida")
