# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passo do prazo.

from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
maior_idade = 18
tempo_faltante = maior_idade - idade
tempo_excedido = idade - maior_idade
ano_alistamento = tempo_faltante + ano_atual


def militar():
    if ano_nascimento > ano_atual:
        print("Opção inválida!")
    else:
        print(f"Quem nasceu em {ano_nascimento} tem {idade} em {ano_atual}")
        if idade > maior_idade:
            print(f"Você já deveria ter se alistado há {tempo_excedido} ano(s)")
            print(f"Seu alistamento foi em {ano_alistamento}")
        elif idade < maior_idade:
            print(f"Ainda falta(m) {tempo_faltante} ano(s) para o alistamento.")
            print(f"Seu alistamento será em {ano_alistamento}")
        elif idade == maior_idade:
            print("Você tem que se alistar IMEDIATAMENTE!")


if __name__ == "__main__":
    militar()
