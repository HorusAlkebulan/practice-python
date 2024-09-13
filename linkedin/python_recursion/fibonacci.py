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


def fibonacci_cached(n: int, cache: dict = None) -> int:
    # NOTE We don't do cache: dict = {} due to unexpected referencing
    print(f"LOCALS: {locals()}")
    if cache is None:
        cache = {}

    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive
    # fib = fib(n-1) + fib(n-2)
    if (n - 1) in cache:
        left = cache[n - 1]
    else:
        left = fibonacci_cached(n - 1, cache)
        cache[n - 1] = left
    if (n - 2) in cache:
        right = cache[n - 2]
    else:
        right = fibonacci_cached(n - 2, cache)
        cache[n - 2] = right

    # combine
    return left + right
