# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

count = 1
while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 35)
    if num < 1:
        break
    while count <= 10:
        mult = num * count
        print(f"{num} x {count} = {mult}")
        count += 1
    print("-" * 35)
    count = 1
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")
