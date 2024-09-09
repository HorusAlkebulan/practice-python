# test_list_sum.py
import pytest

from list_sum import list_sum

ARG_NAMES = ["a_list", "expected"]
ARG_VALUES = [
    ([2, 3, 5, 7], 17),
    ([-4, -3, -2, -1, 10], 0),
    ([], 0),
    ([7], 7),
]


@pytest.mark.parametrize(ARG_NAMES, ARG_VALUES)
def test_list_sum(a_list: list, expected: int):
    actual = list_sum(a_list)
    assert actual == expected


@pytest.mark.parametrize(ARG_NAMES, ARG_VALUES)
def test_list_sum_recursive(a_list: list, expected: int):
    actual = list_sum(a_list)
    assert actual == expected
