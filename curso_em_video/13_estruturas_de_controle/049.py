# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

fator = int(input("Digite um número: "))

for multiplicador in range(1, 10 + 1):
    produto = fator * multiplicador
    print(f"{fator} x {multiplicador} = {produto}")
