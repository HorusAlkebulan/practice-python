# test_make_change.py
from make_change import make_change


def test_base_case():

    actual = make_change(amount=2.00)
    expected = ["1x2q"]
    assert actual == expected


def test_less_than_1_quid():

    actual = make_change(amount=0.24)
    expected = ["1x20p", "2x2p"]
    assert actual == expected


def test_more_than_1_quid():

    actual = make_change(amount=1.63)
    expected = ["1x1q", "1x50p", "1x10p", "1x2p", "1x1p"]
    assert actual == expected
