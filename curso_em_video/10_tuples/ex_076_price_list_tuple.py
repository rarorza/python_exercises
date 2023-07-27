# Develop a program that has a single tuple with product names and their
# respective prices, in sequence. At the end, show a price list, organizing the
# data in tabular form.

product_list = (
    "Pencil",
    1.75,
    "Eraser",
    2.00,
    "Journal",
    15.90,
    "Case",
    25.00,
    "Protractor",
    4.20,
    "Compass",
    9.99,
    "Schoolbag",
    120.32,
    "Book",
    34.90,
)

print("-" * 40)
print("PRICE LISTING".center(40))
print("-" * 40)

for i in range(0, len(product_list), 2):
    print(
        f"{product_list[i]}",
        "$",
        end="",
        sep="." * (31 - len(product_list[i])),
    )
    print(
        f"{product_list[i + 1]:.2f}".rjust(8)
    )
print("-" * 40)
