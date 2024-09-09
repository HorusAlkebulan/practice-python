# test_multiply.py

import pytest

from multiply import multiply

ARG_NAMES = ["multiplier", "multiplicand", "expected"]
ARG_VALUES = [(4, 5, 20)]


@pytest.mark.parametrize(ARG_NAMES, ARG_VALUES)
def test_mulitiply(multiplier: int, multiplicand: int, expected: int):
    actual = multiply(multiplier, multiplicand)
    assert actual == expected
