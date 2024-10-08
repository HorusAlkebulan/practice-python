"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

# cd linkedin/python_recursion
# pytest factorial_recursive.py -v


from trace_recursion import trace


def factorial_recursive_while(n):  # Condition-controlled version

    # n = 5
    # f = 5 * 4 * 3 * 2 * 1

    # n = 4
    # f = 4 * 3 * 2 * 1

    # initial conditions
    result = 1

    result = result * factorial_recursive(n)

    # n = 1
    # result = factorial_recursive(n=1, result=1)

    # n = 2
    # result = factorial_recursive(n=2, result=1)

    return result


def factorial_recursive(n):

    # base case to exit
    if n <= 1:
        # what do we return in the base case?
        return 1

    # take action

    # move towards base case
    recurse_n = n - 1  # 1

    # recursive call
    result = n * factorial_recursive(recurse_n)
    return result


# Let's do some basic testing
def test_4():
    assert factorial_recursive_while(4) == 24


def test_6():
    assert factorial_recursive_while(6) == 720


def test_1():
    assert factorial_recursive_while(1) == 1


def test_0():
    assert factorial_recursive_while(0) == 1


def test_neg_7():
    assert factorial_recursive_while(-7) == 1


def test_50():
    assert (
        factorial_recursive_while(50)
        == 30414093201713378043612608166064768844377641568960512000000000000
    )


if __name__ == "__main__":

    # trace this function
    factorial = trace(factorial_recursive_while)
    factorial_recursive_while(5)
    # print(f"x: {x} for n=5")
