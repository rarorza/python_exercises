# Develop a simple guessing game, the game have to choose an int number in
# between 0 and 5

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5. e peça
# para o usuário tentar descobrir qual foi número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero_secreto = randint(1, 5)  # parecido com o random.ranged
print("Vou pensar em um número entre 0 e 5. Tentem adivinhar...")
chute = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
if chute == numero_secreto:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {numero_secreto} e não no {chute}")
