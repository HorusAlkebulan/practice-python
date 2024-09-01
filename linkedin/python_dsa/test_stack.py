# test_stack.py
from stack import Stack
import pytest
from node import Node   

def test_peek_empty_error():
    int_stack = Stack()
    with pytest.raises(IndexError) as e:
        _ = int_stack.peek()
    assert str(e.value) == "Empty stack" 

def test_std_library_stack_pop_empty():
    node_stack: list = []
    node = Node(42)
    node_stack.append(node)
    top = node_stack.pop()
    with pytest.raises(IndexError) as e:
        _ = node_stack.pop()
    assert str(e.value) == "pop from empty list"
