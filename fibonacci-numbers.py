# The Fibonacci Sequence is a eries of numbers, where the next number is found by adding up the two numbers before it.
#
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9   ...
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#

values = {}


def fibonacci(n):
    if n in values:
        return values.get(n)

    if n == 0:
        return 0

    if n == 1:
        return 1

    value = fibonacci(n-1) + fibonacci(n-2)
    values[n] = value
    return value


if __name__ == "__main__":
    print(fibonacci(7))
