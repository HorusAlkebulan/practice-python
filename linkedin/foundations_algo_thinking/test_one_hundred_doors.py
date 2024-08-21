# test_one_hundred_doors.py
from one_hundred_doors import flip_doors


def test_flip_doors_1():

    num_doors = 1
    result = flip_doors(num_doors)
    expected = [True]
    assert result == expected


def test_flip_doors_2():

    # 0: [F, F]
    # 1: [T, T]
    # 2: [T, F]
    num_doors = 2
    result = flip_doors(num_doors)
    expected = [True, False]
    assert result == expected


def test_flip_doors_5():

    num_doors = 5
    result = flip_doors(num_doors)
    expected = [True, False, False, True, False]
    assert result == expected


def test_flip_doors_6():

    num_doors = 6
    result = flip_doors(num_doors)
    expected = [True, False, False, True, False, False]
    assert result == expected


def test_flip_doors_100():

    num_doors = 100
    result = flip_doors(num_doors)
    expected = [
        True,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
    ]
    assert result == expected


test_flip_doors_2()
