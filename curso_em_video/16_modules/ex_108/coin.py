def increase(num, percent):
    result = num
    result += num * percent
    return result


def decrease(num, percent):
    result = num
    result -= num * percent
    return result


def double(num):
    result = num * 2
    return result


def half(num):
    result = num / 2
    return result


def coin(value, coin="R$"):
    result = f"{value:.2f}"
    return coin + result.replace(".", ",")
