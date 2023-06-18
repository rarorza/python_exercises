# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições
# de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco_compra = float(input("Preço das compras: R$"))
print(
    """
      FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão
      """
)
opcao = int(input("Qual é a opção? "))
desconto_dez = preco_compra - (preco_compra * 0.1)
desconto_cinco = preco_compra - (preco_compra * 0.05)
preco_juros = preco_compra + (preco_compra * 0.2)

if opcao == 1:
    print(f"Sua compra de R${preco_compra} vai custar R${desconto_dez:.2f} no final")
elif opcao == 2:
    print(f"Sua compra de R${preco_compra} vai custar R${desconto_cinco:.2f} no final")
elif opcao == 3:
    parcela_duas_vezes = preco_compra / 2
    print(f"Sua compra de R${preco_compra} vai custar R${preco_compra:.2f} no final")
    print(f"Sua compra será parcelada em 2x de R${parcela_duas_vezes} SEM JUROS")
elif opcao == 4:
    parcela_opcao = int(input("Quantas parcelas? "))
    parcela_sem_limite = preco_juros / parcela_opcao
    print(f"Sua compra de R${preco_compra:.2f} vai custar R${preco_juros:.2f} no final")
    print(
        f"Sua compra será parcelada em {parcela_opcao}x de R$ {parcela_sem_limite:.2f}"
    )
else:
    print("Opção inválida")
    print(f"Sua compra de R${preco_compra} vai custar R${preco_compra:.2f} no final")
