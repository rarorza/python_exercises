# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma sequência de fibonacci.
#
# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

print("-" * 26)
print("SEQUÊNCIA DE FIBONACCI".center(26))
print("-" * 26)

primeiro_termo = 0
segundo_termo = 1
termo_final = int(input("Quantos termos você quer mostrar? "))
contador = 0
print(f"{primeiro_termo} -> {segundo_termo} -> ", end="")
while contador != termo_final:
    fibonacci = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = fibonacci
    contador += 1
    print(f"{fibonacci}", end=" -> ")
print("FIM!")
