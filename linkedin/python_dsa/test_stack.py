# test_stack.py
from stack import Stack
import pytest
from node import Node   

def test_peek_empty_error():
    int_stack = Stack()
    with pytest.raises(IndexError) as e:
        _ = int_stack.peek()
    # assert str(e.value) == "Empty stack" 
    assert str(e.value) == "list index out of range"

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
    # expected = "[1 <class 'int'>]"
    assert stack_str == expected

def test_push_2():
    int_stack = Stack()
    int_stack.push(1)
    int_stack.push(2)
    stack_str = str(int_stack)
    expected = "[1], [2]"
    # expected = "[1 <class 'int'>],[2 <class 'int'>]"
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
    expected = "[1], [2]"
    # expected = "[1 <class 'int'>],[2 <class 'int'>]"
    assert stack_str == expected    

def test_push_4_tuples():
    tuple_stack = Stack()
    tuple_stack.push((0, 0))
    tuple_stack.push((0, 1))
    tuple_stack.push((1, 0))
    tuple_stack.push((1, 1))
    print(f"tuple_stack: {tuple_stack}")
    top = tuple_stack.peek()
    assert top == (1, 1)

def reverse_string(string: str) -> str:
    char_stack = Stack()
    for idx in range(len(string)):
        char_stack.push(string[idx])
    output = ""
    for i in range(len(string)):
        output += str(char_stack.pop())
    return output

def test_reverse_string_1_char():
    test_string = "x"
    result = reverse_string(test_string)
    expected = "x"
    assert result == expected

def test_reverse_string_2_chars():
    test_string = "xy"
    result = reverse_string(test_string)
    expected = "yx"
    assert result == expected

def test_reverse_string_many_chars():
    test_string = "gninraeL nIdekniL htiw tol a nraeL"
    result = reverse_string(test_string)
    expected = "Learn a lot with LinkedIn Learning"
    assert result == expected

def test_multi_ops_on_stack():

    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    assert s.peek() == 7
    print(s.size())
    assert s.size() == 2
if __name__ == "__main__":
    test_push_3_pop_1()