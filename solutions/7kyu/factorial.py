# Your task is to write function factorial.

# https://en.wikipedia.org/wiki/Factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
