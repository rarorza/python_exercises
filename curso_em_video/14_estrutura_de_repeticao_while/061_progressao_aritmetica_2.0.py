# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print("=" * 25)
print("10 TERMOS DE UMA PA".center(25))
print("=" * 25)
termo_inicial = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo_final = termo_inicial + (10 * razao)

while termo_inicial < termo_final:
    print(f"{termo_inicial}", end=" -> ")
    termo_inicial += razao
print("ACABOU")
