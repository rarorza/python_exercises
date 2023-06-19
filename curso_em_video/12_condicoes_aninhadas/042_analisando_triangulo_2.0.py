# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
#
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print("-=" * 10)
print("Analisador de Triângulo")
print("-=" * 10)

lado_a = float(input("Primeiro segmento: "))
lado_b = float(input("Segundo segmento: "))
lado_c = float(input("Terceiro segmento: "))

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    if lado_a == lado_b == lado_c:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")
