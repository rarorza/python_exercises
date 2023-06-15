# Crie um programa que leia um frase qualquer e diga se ela é
# palindromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").replace(" ", "").lower()
frase_inversa = ""

# esse for vai inverter o que foi digitado no input
# 1) len(frase) - 1 = é o início do range, ou seja, ele começa do final
# 2) -1 = é fim do range, indo até 0, se colocarmos 0 ele só irá até 1, por isso o -1
# 3) -1 = é o passo do range, sempre subtraindo 1
for letra in range(len(frase) - 1, -1, -1):
    frase_inversa += frase[letra]

print(f"O inverso de {frase} é {frase_inversa}")

if frase == frase_inversa:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
