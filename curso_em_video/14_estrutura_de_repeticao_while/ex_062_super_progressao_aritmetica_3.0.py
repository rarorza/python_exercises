# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando o usuário disser que quer mostrar 0 termos.


def main():
    print("=" * 25)
    print("GERADOR DE PA".center(25))
    print("=" * 25)
    termo_inicial = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    termos = 10
    contador_termos = termos
    termo_final = termo_inicial + (termos * razao)
    progressao(termo_inicial, termo_final, razao)
    opcao = 1
    while opcao != 0:
        opcao = int(input("Quantos termos você quer mostrar a mais? "))
        termos = opcao
        contador_termos += opcao
        termo_inicial = termo_final
        termo_final = termo_inicial + (termos * razao)
        progressao(termo_inicial, termo_final, razao)
    print(f"Progressão finalizada com {contador_termos} mostrados")


def progressao(termo_inicial, termo_final, razao):
    while termo_inicial < termo_final:
        print(f"{termo_inicial}", end=" -> ")
        termo_inicial += razao
    print("PAUSA")


if __name__ == "__main__":
    main()
