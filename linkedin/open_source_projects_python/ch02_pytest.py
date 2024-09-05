# ch02_pytest.py

import pytest

def test_simple():

    s = ["a", "b", "c", "d", "e"]
    expected = ["e", "d", "c", "b", "a"]
    actual  = s.reverse()
    assert expected == actual

if __name__ == "__main__":
    test_simple()
    print("Tests complete.")