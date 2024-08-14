from ch02_queue import Queue, printDocuments


def test_size():

    # This is how your code will be called.
    # Your answer should be the largest value in the numbers list.
    # You can edit this code to try different testing cases.
    documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
    # result = Answer.printDocuments(documents)

    queue = Queue()
    queue.enqueue(documents[0])
    queue.enqueue(documents[1])
    queue.enqueue(documents[2])
    assert queue.size() == 3


def test_isEmpty():

    queue = Queue()
    assert queue.isEmpty()


def test_front():

    documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
    # result = Answer.printDocuments(documents)

    queue = Queue()
    queue.enqueue(documents[0])
    queue.enqueue(documents[1])
    queue.enqueue(documents[2])
    assert queue.front() == documents[0]


def test_rear():

    documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
    # result = Answer.printDocuments(documents)

    queue = Queue()
    queue.enqueue(documents[0])
    queue.enqueue(documents[1])
    queue.enqueue(documents[2])
    assert queue.front() == documents[0]


def test_dequeue():

    documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
    # result = Answer.printDocuments(documents)

    queue = Queue()
    queue.enqueue(documents[0])
    queue.enqueue(documents[1])
    queue.enqueue(documents[2])
    item = queue.dequeue()
    assert item == documents[0]
    assert queue.size() == 2

class Answer():
    @staticmethod
    def printDocuments(documents):
        return printDocuments(documents)
    
def test_print_3_documents():

    documents = [("Report", 10), ("Essay", 5), ("Slides", 15)]
    result = Answer.printDocuments(documents)

    expected = []
    expected.append("Document Report printed in 5.0 minutes")
    expected.append("Document Essay printed in 2.5 minutes")
    expected.append("Document Slides printed in 7.5 minutes")

    assert result == expected
