# test_node.py
from node import Node

def test_null_node():
    stack_node = Node(None)
    assert str(stack_node) == "[]"