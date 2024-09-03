from node import Node


class Stack:
    def __init__(self):
        super().__init__()
        self.items: list = []
        self.top_idx: int = -1

    def push(self, item: any) -> None:

        #   [1, 2, 3, 4]
        #             ^
        #             top
        node = Node(item)
        self.items.append(node)
        self.top_idx += 1

    def pop(self) -> any:
        if self.top_idx == -1:
            raise IndexError("Empty stack")
        else:
            top_node = self.items[self.top_idx]
            self.top_idx -= 1
            return top_node.data

    def peek(self) -> any:
        if self.top_idx == -1:
            raise IndexError("Empty stack")
        else:
            top_node = self.items[self.top_idx]
            return top_node.data

    def is_empty(self) -> bool:
        if self.top_idx == -1:
            return True
        else:
            return False

    def size(self) -> int:
        return self.top_idx + 1
    
    
    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            str_rep = ""
            for i in range(0, self.top_idx + 1):
                if i == 0:
                    str_rep += str(self.items[i])
                else:
                    str_rep += f",{str(self.items[i])}"
            return str_rep
        
    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            str_rep = ""
            for i in range(0, self.top_idx + 1):
                if i == 0:
                    str_rep += str(self.items[i])
                else:
                    str_rep += f",{str(self.items[i])}"
            return str_rep