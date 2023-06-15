# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print("=" * 25)
print("10 TERMOS DE UMA PA".center(25))
print("=" * 25)
termo_inicial = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
# O termo final é igual ao termo inicial menos a razão
# para que o contador não pule o termo inicial
termo_final = termo_inicial - razao

for i in range(1, 11):
    termo_final += razao
    print(f"{termo_final}", end=" -> ")
print("ACABOU")

# Formula matemática correta
# 10 é o termo final, podendo ser subtitído por X
# termo_final = termo_inicial + (10 - 1) * razao
# for i in range(termo_inicial, termo_final + razao, razao):
#     print(f"{i}", end="-> ")
# print("ACABOU")
#
