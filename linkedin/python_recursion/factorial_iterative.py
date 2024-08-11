"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

# cd linkedin/python_recursion
# pytest factorial_iterative.py -v


def factorial_iterative_while(n):  # Condition-controlled version

    # n = 5
    # f = 5 * 4 * 3 * 2 * 1

    # n = 4
    f = 4 * 3 * 2 * 1
    result = 1
    dx = 0
    for _ in range(n):
        dx = dx + 1
        result = result * dx

    return result


# Let's do some basic testing
def test_4():
    assert factorial_iterative_while(4) == 24


def test_6():
    assert factorial_iterative_while(6) == 720


def test_1():
    assert factorial_iterative_while(1) == 1


def test_0():
    assert factorial_iterative_while(0) == 1


def test_neg_7():
    assert factorial_iterative_while(-7) == 1


def test_50():
    assert (
        factorial_iterative_while(50)
        == 30414093201713378043612608166064768844377641568960512000000000000
    )
