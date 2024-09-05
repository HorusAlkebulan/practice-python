# node.py
class Node:
    def __init__(self, data: any):
        self.data: any = data
        self.next: any = None
        self.prev: any = None

    def __str__(self) -> str:
        if self.data is None:
            return "[]"
        else:
            return f"[{self.data}]"
            # return f"[{self.data} {type(self.data)}]"

    def __repr__(self) -> str:
        if self.data is None:
            return "[]"
        else:
            return f"[{self.data}, type: {type(self.data)}]"
