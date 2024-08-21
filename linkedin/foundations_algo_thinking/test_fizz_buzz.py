# test_fizz_buzz.py
from fizz_buzz import fizz_buzz

def test_fizz_buzz_1():

    result = fizz_buzz(1)
    expected = ["1"]
    assert result == expected
 
def test_fizz_buzz_3():

    result = fizz_buzz(3)
    expected = ["1", "2", "fizz"]
    assert result == expected

def test_fizz_buzz_5():

    result = fizz_buzz(5)
    expected = ["1", "2", "fizz", "4", "buzz"]
    assert result == expected

def test_fizz_buzz_15():

    result = fizz_buzz(15)
    expected = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizz buzz"]
    assert result == expected
