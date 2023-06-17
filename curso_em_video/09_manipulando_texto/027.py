# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida
# a primeiro e o último nome separadamente.

nome = input("Digite seu nome: ").strip().lower().split()
print(
    f"""
      Seu primeiro nome é {nome[0].capitalize()}
      Seu último nome é {nome[len(nome) - 1].capitalize()}
      """
)
