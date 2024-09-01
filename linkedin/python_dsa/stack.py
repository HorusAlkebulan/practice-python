from node import Node


class Stack:
    def __init__(self):
        super().__init__()
        self.items: list = []
        self.top_idx: int = 0

    def push(self, item: any) -> None:

        #   [1, 2, 3, 4]
        #             ^
        #             top
        node = Node(item)
        self.items.append(node)
        self.top_idx += 1

    def pop(self) -> any:
        if self.top_idx == 0:
            raise IndexError("Empty stack")
        else:
            top_node = self.items[self.top_idx]
            self.top_idx -= 1
            return top_node.data

    def peek(self) -> any:
        if self.top_idx == 0:
            raise IndexError("Empty stack")
        else:
            top_node = self.items[self.top_idx]
            return top_node.data

    def is_empty(self) -> bool:
        if self.top_idx == 0:
            return True
        else:
            return False
