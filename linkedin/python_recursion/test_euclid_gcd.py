# test_euclid_gcd.py
import pytest

from euclid_gcd import euclid_gcd_recursive

ARG_NAMES = ["a", "b", "expected"]
ARG_VALUES = [
    (32, 12, 4),
    (50, 15, 5),
    (42, 28, 14),
    (28, 42, 14),
    (345, 766, 1),
]


# @pytest.mark.parametrize(ARG_NAMES, ARG_VALUES)
# def test_euclid_gcd(a:int, b: int, expected: int):
#     actual = euclid_gcd(a, b)
#     assert actual == expected


@pytest.mark.parametrize(ARG_NAMES, ARG_VALUES)
def test_euclid_gcd_recursive(a: int, b: int, expected: int):
    actual = euclid_gcd_recursive(a, b)
    assert actual == expected
