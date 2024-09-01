# test_stack.py
from stack import Stack
import pytest

def test_peek_empty_error():
    int_stack = Stack()
    peek_val = int_stack.peek()
    assert peek_val is None 
