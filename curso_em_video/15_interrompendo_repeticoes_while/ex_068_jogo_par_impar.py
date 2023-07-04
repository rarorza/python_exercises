# Faça um programa que jogo par ou impar com o computador. O jogo só será interrompido quando o
# jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR".center(30))
count = 0

while True:
    print("=-" * 15)
    num = int(input("Diga um valor: "))
    opcao = " "
    while opcao not in "PpIi":
        opcao = input("Par ou Ímpar? [P/I] ").strip().upper()[0]

    num_secreto = randint(0, 10)
    resultado = num + num_secreto
    print("-" * 30)

    if resultado % 2 == 0:
        print(f"Você jogou {num} e o computador {num_secreto}, total de {resultado}. DEU PAR!")
        if opcao in "Pp":
            print("Você VENCEU!")
            count += 1
            print("Vamos jogar novamente...")
        elif opcao in "Ii":
            print("Você PERDEU!")
            print("=-" * 15)
            break
    else:
        print(f"Você jogou {num} e o computador {num_secreto}, total de {resultado}. DEU IMPAR!")
        if opcao in "Ii":
            print("Você VENCEU!")
            count += 1
            print("Vamos jogar novamente...")
        elif opcao in "Pi":
            print("Você PERDEU!")
            print("=-" * 15)
            break
print(f"GAME OVER! Você venceu {count} vez(es).")
