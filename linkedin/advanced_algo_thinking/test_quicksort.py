# test_quicksort.py

from quicksort import quicksort


# happy path
def test_quicksort_empty() -> list:
    input = []
    expected = []
    actual = quicksort(input)
    assert actual == expected


def test_quicksort_1() -> list:
    input = [5]
    expected = [5]
    actual = quicksort(input)
    assert actual == expected


def test_quicksort_2() -> list:
    input = [6, 2]
    expected = [2, 6]
    actual = quicksort(input)
    assert actual == expected


def test_quicksort_3() -> list:
    input = [8, 3, -1]
    expected = [-1, 3, 8]
    actual = quicksort(input)
    assert actual == expected


def test_quicksort_4() -> list:
    input = [9, 6, 7, 10]
    expected = [6, 7, 9, 10]
    actual = quicksort(input)
    assert actual == expected


def test_quicksort_9():
    input = [9, 6, 7, 10, 8, 3, -1, 0, 2]
    expected = [-1, 0, 2, 3, 6, 7, 8, 9, 10]
    actual = quicksort(input)
    assert actual == expected
