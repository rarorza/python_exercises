# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.
# Para salário superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual é o salário do funcionário? R$"))

if salario <= 1250:
    aumento = (salario * 0.15) + salario
else:
    aumento = (salario * 0.10) + salario

print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora")
