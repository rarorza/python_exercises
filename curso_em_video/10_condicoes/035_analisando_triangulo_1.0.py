# Desenvolva um programa que leia o comprimento de três retas e siga ao usuário se elas podem ou
# não formar um triângulo.

print("-=" * 10)
print("Analisador de Triângulo")
print("-=" * 10)

lado_a = float(input("Primeiro segmento: "))
lado_b = float(input("Segundo segmento: "))
lado_c = float(input("Terceiro segmento: "))

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    print("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")
