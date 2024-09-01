# node.py
class Node():
    def __init__(self, data: any):
        self.data: any = data
        self.next: any = None
        self.prev: any = None

    def __str__(self) -> str:
        if self.data is None:
            return "[]"
        else:
            return f"[{self.data}]"