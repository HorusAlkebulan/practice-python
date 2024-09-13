class Node:
    def __init__(self, data: any, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return (
            (f"[left: {self.left}, " if self.left is not None else "[")
            + f"data: {self.data}"
            + (f", right: {self.right}]" if self.right is not None else "]")
        )


def traverse_in_order(root_node: Node) -> None:
    # base case
    if root_node is None:
        return

    # move towards base case
    # combine results
    traverse_in_order(root_node.left)
    print(root_node.data)
    traverse_in_order(root_node.right)


def test_node():
    #
    node = Node("10")
    print(f"node={node}")

    assert repr(node) == "[data: 10]"

    left = Node("5")
    node.left = left
    print(f"left={left}")

    assert repr(node) == "[left: [data: 5], data: 10]"

    right = Node("15")
    node.right = right

    assert repr(node) == "[left: [data: 5], data: 10, right: [data: 15]]"


def test_traverse():
    node_tree = Node("10")
    left = Node("5")
    node_tree.left = left
    right = Node("15")
    node_tree.right = right

    traverse_in_order(node_tree)
    assert node_tree is not None
