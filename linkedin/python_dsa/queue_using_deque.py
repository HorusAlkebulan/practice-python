from collections import deque

class Queue():
    def __init__(self):
        self.items = deque()

    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def enqueue(self, item: any) -> None:
        self.items.append(item)

    def dequeue(self) -> any:
        return self.items.popleft()
    
    def size(self) -> int:
        return len(self.items)
    
    def peek(self) -> any:
        return self.items[0]
    
    def __str__(self) -> str:
        return str(self.items)
    
    def __repr__(self) -> str:
        return f"size: {self.size}, items: {self.items}"