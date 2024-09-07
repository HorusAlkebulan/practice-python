def fibonacci(n: int) -> int:
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive
    # fib = fib(n-1) + fib(n-2)
    left = fibonacci(n - 1)
    right = fibonacci(n - 2)

    # combine
    return left + right
