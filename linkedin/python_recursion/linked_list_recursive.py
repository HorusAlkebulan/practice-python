class Node:
    def __init__(self, data: any, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"[data: {self.data}" + (
            f", next: {self.next}]" if self.next is not None else "]"
        )


def traverse(head_node: Node) -> None:
    # base case
    if head_node is None:
        return

    # move towards base case
    rest_of_the_list = head_node.next

    # combine results
    traverse(rest_of_the_list)
    print(head_node.data)


def test_node():
    node = Node("First")
    print(f"node={node}")

    assert repr(node) == "[data: First]"

    node = Node("Second", node)
    print(f"node={node}")

    assert repr(node) == "[data: Second, next: [data: First]]"

    node = Node("Third", node)
    print(f"node={node}")

    assert repr(node) == "[data: Third, next: [data: Second, next: [data: First]]]"


def test_traverse():
    node_list = Node("First")
    node_list = Node("Second", node_list)
    node_list = Node("Third", node_list)

    traverse(node_list)
    assert node_list is not None
