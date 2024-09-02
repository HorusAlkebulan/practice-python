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

def test_push_1():
    int_stack = Stack()
    int_stack.push(1)
    stack_str = str(int_stack)
    expected = "[1]"
    assert stack_str == expected

def test_push_2():
    int_stack = Stack()
    int_stack.push(1)
    int_stack.push(2)
    stack_str = str(int_stack)
    expected = "[1],[2]"
    assert stack_str == expected

def test_push_3_pop_1():
    int_stack = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    top = int_stack.pop()
    expected = 3
    assert top == expected

    stack_str = str(int_stack)
    expected = "[1],[2]"
    assert stack_str == expected    

if __name__ == "__main__":
    test_push_3_pop_1()