# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


def fibonacci() -> int:
    first = 1
    second = 1
    fib = 1
    fib_list = []
    for _ in range(1, 32):
        fib = first + second
        first = second
        second = fib
        if fib % 2 == 0:
            fib_list.append(fib)
    return sum(fib_list)


print(fibonacci())
