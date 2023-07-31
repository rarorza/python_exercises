# Create a program that has a factorial() function that receives two parameters:
# the first one indicating the number to be calculated and the other called
# show, which will be a logical value (optional) indicating whether or not the
# calculation process will be shown on the screen. factorial.


def factorial(n, show=False):
    """
    Calculates the factorial of a number.
    :param n: The number to calculate.
    :param show: (optional) Whether or not to show the account.
    :return: The Factorial value of a number n.
    """
    f = n
    print("-" * 30)
    for i in range(n - 1, 0, -1):
        f *= i
        if show is True:
            if i == 1:
                print(f"{i} =", end=" ")
            else:
                print(f"{i} x", end=" ")
    return f


print(factorial(6, show=False))
print(help(factorial))
