# Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros.

metro = float(input("Uma distância em metros: "))
print(
    "A medida de {}m corresponde a \n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm".format(
        metro,
        (metro / 1000),
        (metro / 100),
        (metro / 10),
        (metro * 10),
        (metro * 100),
        (metro * 1000),
    )
)
