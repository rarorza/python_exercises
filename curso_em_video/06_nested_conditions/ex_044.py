# Develop a program that calculates the amount to be paid for a product,
# considering its normal price and payment terms:
#
# - Cash/check payment: 10% discount
# - Cash on card: 5% discount
# - In up to 2 installments on the card: normal price
# - 3x or more on the card: 20% interest

price = float(input("Purchase price: $"))
print(
    """
PAYMENT METHODS
[1] Cash/check
[2] At sight card
[3] 2x on card
[4] 3x or more on card
"""
)
option = int(input("What is the option? "))
discount_ten = price - (price * 0.1)
discount_five = price - (price * 0.05)
fees_price = price + (price * 0.2)

if option == 1:
    print(f"Sua compra de R${price} vai custar R${discount_ten:.2f} no final")
elif option == 2:
    print(f"Sua compra de R${price} vai custar R${discount_five:.2f} no final")
elif option == 3:
    two_installments = price / 2
    print(f"Sua compra de R${price} vai custar R${price:.2f} no final")
    print(
        f"Your purchase will be paid in 2 installments of ${two_installments}"
    )
elif option == 4:
    opt_installments = int(input("How many plots? "))
    unlimited = fees_price / opt_installments
    print(f"Your purchase of ${price:.2f} will cost ${fees_price:.2f}")
    print(
        f"Your purchase will be paid {opt_installments}x in $ {unlimited:.2f}"
    )
else:
    print("Invalid option")
    print(f"Your purchase of ${price} will cost ${price:.2f} at the end")
