# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
cidade_posicao_1 = cidade.split()
santo_existe = cidade_posicao_1[0].find("santo")

if santo_existe == -1:
    print('False')
else:
    print('True')
