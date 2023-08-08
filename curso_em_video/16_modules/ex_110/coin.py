def increase(num, percent, format=False):
    result = num
    result += num * percent
    return result if format is False else coin(result)


def decrease(num, percent, format=False):
    result = num
    result -= num * percent
    return result if not format else coin(result)


def double(num, format=False):
    result = num * 2
    if format:
        return coin(result)
    else:
        return result


def half(num, format=False):
    result = num / 2
    if format:
        return coin(result)
    else:
        return result


def coin(value, coin="R$"):
    result = f"{value:.2f}"
    return coin + result.replace(".", ",")


def resume(price, incre=0.1, decre=0.1):
    print("-" * 32)
    print("RESUME".center(32))
    print("-" * 32)
    print(f"Price analyzed: \t{coin(price)}")
    print(f"Double the price: \t{double(price, True)}")
    print(f"Half price: \t\t{half(price, True)}")
    print(f"{incre * 100:.0f}% increase: \t\t{increase(price, incre, True)}")
    print(f"{decre * 100:.0f}% increase: \t\t{decrease(price, decre, True)}")
    print("-" * 32)
