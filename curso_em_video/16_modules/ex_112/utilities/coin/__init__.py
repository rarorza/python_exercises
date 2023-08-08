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
