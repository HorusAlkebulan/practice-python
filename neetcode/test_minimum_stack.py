# test_minimum_stack.py

class StackNode:

    def __init__(self, val: int):
        self.value = val
        self.prev = None
        self.next = None

class MinStack:

    def __init__(self):
        self.top: StackNode = None
        self.min: StackNode = None

    def push(self, val: int) -> None:
        new_node = StackNode(val)
        if self.top is None:
            self.top = new_node
            self.min = new_node 
        else:
            if new_node.value < self.min.value:
                # new minimum node
                temp_node = self.min
                self.min = new_node
                # reset prev and next
                self.min.next = temp_node
                temp_node.prev = self.min
            else:
                # goes after minimum node
                temp_node = self.min.next
                self.min.next = new_node
                # reset prev and next
                new_node.next = temp_node
                temp_node.prev = new_node
        self.top = new_node

    def pop(self) -> None:
        top_saved = self.top
        self.top = top_saved.next
        self.top.prev = None
        return

    def top(self) -> int:
        return self.top.value

    def getMin(self) -> int:
        return self.min.value
