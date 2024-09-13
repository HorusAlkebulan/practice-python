# test_fibonacci.py

import pytest

from fibonacci import fibonacci, fibonacci_cached

inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
expecteds = [0, 1, 1, 2, 3, 5, 8, 13, 21]

param_tuples = []
for i in range(len(inputs)):
    param_tuples.append((inputs[i], expecteds[i]))


@pytest.mark.parametrize(argnames=["input", "expected"], argvalues=param_tuples)
def test_fibonacci(input: int, expected: int) -> int:
    actual = fibonacci(input)
    print(f"input: {input}, expected: {expected}, actual: {actual}")
    assert actual == expected


@pytest.mark.parametrize(argnames=["input", "expected"], argvalues=param_tuples)
def test_fibonacci_cached(input: int, expected: int) -> int:
    actual = fibonacci_cached(input)
    print(f"input: {input}, expected: {expected}, actual: {actual}")
    assert actual == expected


if __name__ == "__main__":
    test_fibonacci_cached(3, 2)
