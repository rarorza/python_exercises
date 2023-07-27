# Create a program that reads how many Brazilian Reais a person has in their
# wallet and shows how much Dollars they can buy.

br_real = float(
    input("How many Brazilian reais do you have in your wallet? R$")
)
dolar = br_real / 4.72
print(f"With R${br_real:.2f} you can buy U${dolar:.2f}")
