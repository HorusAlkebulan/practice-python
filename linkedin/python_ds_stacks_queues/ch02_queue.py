# Python code​​​​​​‌​‌‌‌​​‌​​‌‌​​‌‌​​​​​‌​​‌ below
# Define a queue class using a list
class Queue:
    def __init__(self):
        self.list = []  # The list to store the elements
        self.head_idx = -1
        self.tail_idx = -1

    def enqueue(self, data: tuple):
        # NOTE: Alternative --> don't track head and tail. use list.pop(index) methods. use 0 for head, -1 for tail
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
        if self.head_idx < 0 or self.tail_idx < 0:
            return 0
        else:
            return self.tail_idx - self.head_idx + 1

    def isEmpty(self):
        return self.size() == 0


# class Document():
#     def __init__(self, name: str, pages: int):
#         self.name = name
#         self.pages = pages

# Define a function that simulates the printing process using a queue
def printDocuments(documents):
    # queue up each document in order
    # dequeue each document until empty, each time adding to output list
    # return output list report
    queue = Queue()
    print_report_ls = []
    for document in documents:
        queue.enqueue(document)
    while not queue.isEmpty():
        document = queue.dequeue()
        name = document[0]
        pages = document[1]
        print_time = pages * 0.5
        report = f"Document {name} printed in {print_time} minutes"
        print_report_ls.append(report)
    return print_report_ls


showExpectedResult = False
showHints = False
