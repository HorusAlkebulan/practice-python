# test_zero_shift_right.py
from zeros_shift_right import shift_zeros_right

def test_with_empty_input():

    arr = [] 
    expected = []
    result = shift_zeros_right(arr)
    assert result == expected


def test_with_unique_values_one_zero():

    arr = [1,8,2,3,7,0,4,5] 
    expected = [1,8,2,3,7,4,5,0]
    result = shift_zeros_right(arr)
    assert result == expected


def test_with_unique_values_two_zeros():

    arr = [1,8,2,0,7,0,4,5] 
    expected = [1,8, 2, 7,4,5,0,0]
    result = shift_zeros_right(arr)
    assert result == expected


def test_with_double_zeros():

    # Eg) I/P - [1,8,0,0,7,0,4,5] 
    arr = [1,8,0,0,7,0,4,5] 
    # O/P - [1,8,7,4,5,0,0,0]
    expected = [1,8,7,4,5,0,0,0]
    result = shift_zeros_right(arr)
    assert result == expected

test_with_unique_values_one_zero()
