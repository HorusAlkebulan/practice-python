class Stack():
    def __init__(self):
        super().__init__()
        self.items = []
        self.top_idx: int = 0

    def push(self, item: any) -> None:
        
        #   [1, 2, 3, 4]
        #             ^
        #             top
        self.items.append(item)
        self.top_idx += 1

    def pop(self) -> any:
        if self.top_idx == 0:
            raise IndexError("Empty stack")
        else:
            top_val = self.items[self.top_idx]
            self.top_idx -= 1
            return top_val

    def peek(self) -> any:
        if self.top_idx == 0:
            raise IndexError("Empty stack")
        else:
            return self.items[self.top_idx]

    def is_empty(self) -> bool:
        if self.top_idx == 0:
            return True
        else:
            return False

