# Inverta a lista sem utilizar reverse() ou [::-1]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
indice_fim_lista = len(lista) - 1  # 14

for i in range(len(lista) // 2):
    # len é // 2 porque o for só precisa percorrer metade da lista para trocar os valores
    auxiliar = lista[i]  # auxiliar = 1
    lista[i] = lista[indice_fim_lista]
    # Substituí o primeiro valor da lista (1) pelo último (15), então lista[0] = 15
    lista[indice_fim_lista] = auxiliar
    # substituí o último valor da lista pelo valor da variável auxiliar (1), então lista[14] = 1
    indice_fim_lista -= 1  # índice - 1 para dar sequência
print(lista)

# Essa é a forma que usará menos memória computacional
