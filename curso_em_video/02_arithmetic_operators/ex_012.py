# Write an algorithm that reads the price of a product and displays its new
# price, with a 5% discount.

price = float(input("What is the price of the product? R$"))
new = price - (price * 5 / 100)
print(
    f"The product that cost ${price:.2f}, in the 5% discount will cost ${new:.2f}"
)
