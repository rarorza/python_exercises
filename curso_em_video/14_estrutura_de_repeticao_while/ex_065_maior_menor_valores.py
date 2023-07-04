# Crie um programa que leia vários números inteiro pelo teclado. No final da Execução, mostre a
# média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

stop = False
soma = 0
contador = 0
num = int(input("Digite um número: "))
maior = num
menor = num

while not stop:
    soma += num
    contador += 1

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    opcao = str(input("Quer continuar? [S/N] ").upper().split())
    if opcao in "S":
        num = int(input("Digite um número: "))
    elif opcao in "N":
        stop = True
    else:
        print("Opção inválida!")
        stop = True

media = soma / contador
print(f"Você digitou {contador} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
