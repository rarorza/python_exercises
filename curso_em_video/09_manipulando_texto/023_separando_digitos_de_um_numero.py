# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#
# Ex:
# Digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

numero = input("Digite um número: ")
numero_justificado = numero.rjust(4, "0")

print(f"Analisando o número {numero}")
print(
    f"""
      Unidade: {numero_justificado[3]}
      Dezena: {numero_justificado[2]}
      Centena: {numero_justificado[1]}
      Milhar: {numero_justificado[0]}
      """
)
