# Crie um programa que leia o nome completo de uma pessoa:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome:

nome = input("Digite seu nome completo: ")
nome_sem_espacos = nome.replace(" ", "")
# Seria possível utilizar o método count para subtrair os espaços do número
# total do len.
#
# ex: len(nome) - nome.count' '

print(f"Seu nome em maiúsculas é {nome.lower()}")
print(f"Seu nome em minúsculas é {nome.upper()}")
print(f"Seu nome tem ao todo {len(nome_sem_espacos)} letras")
print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")
