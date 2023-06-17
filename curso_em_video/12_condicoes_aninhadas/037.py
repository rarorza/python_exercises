# Escreva um programa que leia um número inteiro qualquer e peça para
# o usuário qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# obs: todo esse problema poderia ter sido resolvido com as funções hex(),
# oct() e bin(), mas achei legal fazer meu próprio conversor.

num = input("Digite um número inteiro: ")
print(
    """Escolha uma das bases para conversão:
[ 1 ] converter em BINÁRIO
[ 2 ] converter em OCTAL
[ 3 ] converter em HEXADECIMAL
"""
)

opcao = int(input("Escolha sua opção: "))
resultado = 1
# Resultado tem o valor 1 para o while pode se iniciar antes do calculo
resto = []
# Lista onde serão armazenados os restos das divisões para conversão
num_int = int(num)
# Conversão da variável num para inteiro, optei por utilizar uma segunda
# variável para manter a variável num sem modificações
hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
# Dicionário com o valores hexadecimais

if opcao == 1:
    while resultado >= 1:
        resto.append(num_int % 2)
        # Acrescenta o resto da divisão na variável resto.
        resultado = num_int // 2
        # Armazena o resultado da divisão inteira, para que seja possível
        # quebrar o loop do while no final.
        num_int = resultado
        # num_int recebe o valor do resultado para as divisões sejam
        # progressivas, caso contrário o loop seria infinito.
    resto.reverse()
    # Inverte a sequência da lista, já que as conversões devem ser lidas da
    #  direita pra esquerda.
    print(f"{num} convertido para BINÁRIO é igual a ", end="")
    for i in range(len(resto)):
        # Para cada resto que foi armazenado em uma lista.
        print(resto[i], end="")
        # Printa o item da lista.
        # Essa solução foi utilizada para que fosse possível exibir na tela os
        # números da lista sem virgula e parenteses.
    print("")
elif opcao == 2:
    while resultado >= 1:
        resto.append(num_int % 8)
        resultado = num_int // 8
        num_int = resultado
    resto.reverse()
    print(f"{num} convertido em OCTAL é igual ", end="")
    for i in range(len(resto)):
        print(resto[i], end="")
    print("")
elif opcao == 3:
    while resultado >= 1:
        hexa = num_int % 16
        # A variável hexa irá executar o mesmo cálculo do resto.append, para
        # que seja possível verificar se o valor excede ou é igual a 10.
        if hexa >= 10:
            # Se hexa >= 10
            resto.append(hexadecimal.get(hexa))
            # A variável hexa quando gera um número entre 10 e 15, procura
            # esse valor no dicionário hexadecimal.
            # Foi utilizado o método get para procurar pelo número de 10 a 15
            # e devolver a letra que corresponde ao número.
        else:
            resto.append(num_int % 16)
        resultado = num_int // 16
        num_int = resultado
    resto.reverse()
    print(f"{num} convertido em HEXADECIMAL é igual ", end="")
    for i in range(len(resto)):
        print(resto[i], end="")
    print("")
else:
    print("Opção inválida!")
