# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

contador = 0
lista_numeros = []
executando = True

while executando:
    numero = int(input("Digite um número: "))
    if numero >= 2:  # Para o número ser primmo ele tem que ser maior que 1
        for divisor in range(1, numero + 1):  # loop para dividir o número pelo divisor
            lista_numeros.append(f"{divisor}")  # adiciona o divisor em uma lista
            if numero % divisor == 0:  # se o resta da divisão for igual a 0
                contador += 1  # o contador irá somar +1
                lista_numeros.remove(f"{divisor}")
                # o dividor dessa divisão é apagado da lista, a variável divisor
                # está envolvida em um format string pois os números estão sendo
                # armazenados como string na lista, pois deve-se utilizar o método
                # remove() para apagar os itens
                lista_numeros.insert(
                    divisor, f"\033[1;31m{divisor}\033[m"
                )  # adiciona novamente o divisor, porém agora na cor vermelha
        for item in lista_numeros:
            # loop para printar na tela todos os itens da lista de itens
            print(f"{item}", end=" ")

        if contador == 2:
            # se o contador for igual a 2, então o número é PRIMO, pois só foi
            # possível fazer a divisão inteira com 1 e o próprio número
            print(f"\nO número {numero} foi divisível por {contador} vezes")
            print("E por isso ele É PRIMO!")
            executando = False
        elif contador > 2:
            # se o contador for maior que 2, então número não é PRIMO
            print(f"\nO número {numero} foi divisível {contador} vezes")
            print("Por isso ele NÃO É PRIMO!")
            executando = False
    else:
        print("O número deve ser maior que 1")
        continue
