# Make a program that reads the weight of five people. At the end, show which
# was the highest and lowest weight read.

weight = []

for person in range(1, 5 + 1):
    weight.append(float(input(f"Peso da {person} pessoa: ")))

print(f"O maior peso lido foi de {max(weight)}")
print(f"O menor peso lido foi de {min(weight)}")
