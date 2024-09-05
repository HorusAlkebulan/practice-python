# test_ch02_pytest.py

import pytest


def test_simple():

    s = ["a", "b", "c", "d", "e"]
    expected = ["e", "d", "c", "b", "a"]
    s.reverse()  # NOTE: reverses in place
    actual = s
    assert expected == actual


if __name__ == "__main__":
    test_simple()
