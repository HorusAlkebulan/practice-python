# test_selection_sort.py
from selection_sort import selection_sort


def test_single_value():

    xs = [7]
    expected = [7]
    actual = selection_sort(xs)
    assert actual == expected


def test_high_to_low():

    xs = [9, 4, 2, 1, -1]
    expected = [-1, 1, 2, 4, 9]
    actual = selection_sort(xs)
    assert actual == expected


def test_random():

    xs = [3, 2, 1, 5, 4]
    expected = [1, 2, 3, 4, 5]
    actual = selection_sort(xs)
    assert actual == expected
