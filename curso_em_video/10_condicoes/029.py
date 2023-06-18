# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade atual do carro? "))
velocidade_limite = 80
aliquota_por_km = 7
multa = (velocidade - velocidade_limite) * aliquota_por_km


if velocidade > velocidade_limite:
    print(
        f"""
        MULTADO! Você excedeu o limite permitido que é de 80Km/h
        Você deve pagar uma multa de R${multa:.2f}!
          """
    )
print("Tenha um bom dia! Dirija com cuidado!")
