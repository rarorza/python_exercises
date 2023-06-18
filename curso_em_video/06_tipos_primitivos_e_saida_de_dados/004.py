# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

everything = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(everything))
print("Só tem espaços? ")
print("É um número? ", everything.isnumeric())
print("É alfabético? ", everything.isalpha())
print("É alfanumérico? ", everything.isalnum())
print("Está em maiúsculas? ", everything.isupper())
print("Está em minúscula? ", everything.islower())
print("Está capitalizada? ", everything.istitle())
# istitle() retorna true se a primeira letra da string é maiúscula
