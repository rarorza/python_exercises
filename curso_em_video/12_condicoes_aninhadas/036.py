# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário
# ou então o empréstimo será negado.

print("Empréstimo fácil!")
salario = float(input("Qual o seu salário? R$\033[0;32m"))
valor_emprestimo = float(input("\033[mQual o valor do imóvel? R$\033[0;32m"))
anos_pagamento = int(
    input("\033[mEm quantos anos pretende pagar o valor do empréstimo? \033[0;32m")
)
limite_emprestimo = salario * 0.30
prestacao = valor_emprestimo / (anos_pagamento * 12)

print(
    f"\033[mPara pagar uma casa de R$ {valor_emprestimo:.2f} em {anos_pagamento} anos a prestação será de R${prestacao:.2f}"
)
if prestacao > limite_emprestimo:
    print("\033[0;031mEmpréstimo negado!")
elif prestacao < limite_emprestimo:
    print("Empréstimo aprovado!")
