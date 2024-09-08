# test_knapsack.py

# pytest -l -s -v -x

from knapsack import knapsack
from tabulate import tabulate


def test_knapsack_ex1():
    max_capacity = 6
    weights = [0, 1, 2, 3, 5]
    values = [0, 10, 5, 20, 35]

    actual = knapsack(max_capacity, weights, values)
    expected_row_0 = [0, 0, 0, 0, 0, 0, 0]
    assert actual[0] == expected_row_0
    expected_row_1 = [0, 10, 10, 10, 10, 10, 10]
    assert actual[1] == expected_row_1
    expected_row_4 = [0, 10, 10, 20, 30, 35, 45]
    assert actual[4] == expected_row_4


def test_knapsack_ex2():
    max_capacity = 6
    weights = [0, 1, 3, 5, 6]
    values = [0, 25, 30, 40, 35]

    actual = knapsack(max_capacity, weights, values)
    expected_row_0 = [0, 0, 0, 0, 0, 0, 0]
    assert actual[0] == expected_row_0
    expected_row_1 = [0, 25, 25, 25, 25, 25, 25]
    assert actual[1] == expected_row_1
    expected_row_4 = [0, 25, 25, 30, 55, 55, 65]
    assert actual[4] == expected_row_4
