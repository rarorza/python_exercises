# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = input("Primeiro valor: ")
num2 = input("Segundo valor: ")
num3 = input("Terceiro valor: ")
nums = [num1, num2, num3]

menor_num = min(nums, key=int)
maior_num = max(nums, key=int)

print(f"O menor valor digitado foi {menor_num}")
print(f"O maior valor digitado foi {maior_num}")
