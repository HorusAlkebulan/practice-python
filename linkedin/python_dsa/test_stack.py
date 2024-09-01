# test_stack.py
from stack import Stack
import pytest

def test_peek_empty_error():
    int_stack = Stack()
    with pytest.raises(IndexError) as e:
        _ = int_stack.peek()

