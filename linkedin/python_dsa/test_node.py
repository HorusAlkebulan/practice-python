# test_node.py
from node import Node

def test_null_node():
    stack_node = Node(None)
    assert str(stack_node) == "[]"

def test_int_node():
    stack_node = Node(42)
    assert str(stack_node) == "[42]"

def test_str_node():
    stack_node = Node("Horus")
    assert str(stack_node) == "[Horus]"