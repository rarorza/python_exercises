# Crie um programa que leia dois valores e mostre um menu na tela.
#
# Ex:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
executando = True
opcao = 0

while executando:
    print(
        """
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
          """
    )
    opcao = int(input("Qual é a sua opção? "))

    if opcao == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} + {num2} é {soma}")
    elif opcao == 2:
        multiplica = num1 * num2
        print(f"A multiplicação entre {num1} x {num2} é {multiplica}")
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"Entre {num1} e {num2} o maior valor é {maior}")
    elif opcao == 4:
        print("Informe os números novamente")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        executando = False
    else:
        print("Opção inválida, tente novamente.")

    print("=-=" * 11)
    sleep(2)

print("Fim do programa! Volte sempre!")
