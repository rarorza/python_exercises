# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = int(input('Primeira nota do aluno: '))
nota2 = int(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print('A média entre {} e {} é igual a {}'.format(nota1,nota2,media))
