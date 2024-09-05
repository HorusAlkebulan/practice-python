# test_queue_ll.py
from queue_using_deque import Queue

def test_1_item():

    queue = Queue()
    queue.enqueue((0, 0))
    
    assert queue.size() == 1
    assert queue.peek() == (0, 0)
    assert queue.dequeue() == (0, 0)
    assert queue.is_empty()

def test_4_items():

    queue = Queue()
    queue.enqueue((0, 0))
    queue.enqueue((0, 1))
    queue.enqueue((1, 0))
    queue.enqueue((1, 1))
    
    assert queue.size() == 4
    assert queue.peek() == (0, 0)
    assert queue.dequeue() == (0, 0)
    assert queue.dequeue() == (0, 1)
    assert not queue.is_empty()

