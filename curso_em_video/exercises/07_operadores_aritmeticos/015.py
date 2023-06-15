# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
km_percorrido = float(input("Quantos kms foram percorridos? "))
custo_dia = 60
custo_km = 15
total_a_pagar_dia = custo_dia * dias_alugados
total_a_pagar_km = (custo_km / 100) * km_percorrido

print(f"O total a pagar é de R${total_a_pagar_km + total_a_pagar_dia:.2f}")
