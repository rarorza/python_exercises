# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

numero_secreto = randint(1, 10)
tentativas = 0
acertou = False
print("Sou seu computador...")
sleep(0.5)
print("""Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
""")
sleep(0.5)

while not acertou:
    chute = int(input("Qual será seu palpite? "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Acerto em {tentativas}. Parabéns!")
        acertou = True
    else:
        if chute > numero_secreto:
            print("Menos... Tente mais uma vez.")
        elif chute < numero_secreto:
            print("Mais... Tente mais uma vez.")
