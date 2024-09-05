from node import Node


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: any) -> None:

        #   [1, 2, 3, 4]
        #             ^
        #             top
        self.items.append(item)

    def pop(self) -> any:
        top_node = self.items.pop()
        return top_node

    def peek(self) -> any:
        top_node = self.items[-1]
        return top_node

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            str_rep = ""
            for i, item in enumerate(self.items):
                if i == 0:
                    str_rep += f"[{str(item)}]"
                else:
                    str_rep += f", [{item}]"
            return str_rep

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            str_rep = f"Count: {len(self.items)}, Contents: "
            for i, item in enumerate(self.items):
                if i == 0:
                    str_rep += f"[{str(item)}]"
                else:
                    str_rep += f", [{item}]"
            return str_rep
