from utilities import coin


def resume(price, incre=0.1, decre=0.1):
    print("-" * 32)
    print("RESUME".center(32))
    print("-" * 32)
    print(f"Price analyzed: \t{coin.coin(price)}")
    print(f"Double the price: \t{coin.double(price, True)}")
    print(f"Half price: \t\t{coin.half(price, True)}")
    print(f"{incre * 100:.0f}% increase: \t\t{coin.increase(price, incre, True)}")
    print(f"{decre * 100:.0f}% increase: \t\t{coin.decrease(price, decre, True)}")
    print("-" * 32)


def readMoney(text=None):
    while True:
        if text:
            print(text, end="")
        value = input().replace(",", ".")
        try:
            float(value)
            break
        except:
            print(f"ERROR, '{value.strip()}' is an invalid price")
    return float(value)
