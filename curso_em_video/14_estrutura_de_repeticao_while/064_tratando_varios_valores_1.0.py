# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o
# usuário digitar o valor 999, sendo uma condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag 999).

stop = False
acumulador = 0
contador = 0

while not stop:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        acumulador += num
        contador += 1
    else:
        stop = True
print(f"Você digitou {contador} e a soma entre eles foi {acumulador}.")
