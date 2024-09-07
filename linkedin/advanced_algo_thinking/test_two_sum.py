# test_two_sum.py

from two_sum import two_sum_problem


def test_two_sum_problem_1():
    assert two_sum_problem([1, 2, 3], 4) == (0, 2)


def test_two_sum_problem_2():
    assert two_sum_problem([1234, 5678, 9012], 14690) == (1, 2)


def test_two_sum_problem_3():
    assert two_sum_problem([2, 2, 3], 4) in [(0, 1), (1, 0)]


def test_two_sum_problem_4():
    assert two_sum_problem([2, 2], 4) in [(0, 1), (1, 0)]


def test_two_sum_problem_5():
    assert two_sum_problem([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]
