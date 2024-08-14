# Python code​​​​​​‌​‌‌‌​​‌​​‌‌​​‌‌​​​​​‌​​‌ below
# Define a queue class using a list
class Queue:
    def __init__(self):
        self.list = []  # The list to store the elements
        self.head_idx = -1
        self.tail_idx = -1

    def enqueue(self, data: tuple):
        if self.isEmpty():
            # empty list
            self.head_idx = 0
            self.tail_idx = 0
            self.list.append(data)
        else:
            # at least one item
            self.list.append(data)
            self.tail_idx += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Empty queue.")
        
        dequeued_item = self.list[self.head_idx]
        self.head_idx += 1
        return dequeued_item

    def front(self):
        return self.list[self.head_idx]

    def rear(self):
        return self.list[self.tail_idx]

    def size(self):
        if self.isEmpty():
            return 0
        else:
            return (self.tail_idx - self.head_idx + 1)

    def isEmpty(self):
        return (self.tail_idx < 0)
        


# class Document():
#     def __init__(self, name: str, pages: int):
#         self.name = name
#         self.pages = pages

# Define a function that simulates the printing process using a queue
def printDocuments(documents):
    # TODO: Implement the printing function
    pass


showExpectedResult = False
showHints = False

