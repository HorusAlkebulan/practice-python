# test_priority_queue.py
from priority_queue import PriorityQueue

def test_happy_path():
    pq = PriorityQueue()
    pq.put(2, "eat")
    pq.put(1, "code")
    pq.put(3, "sleep")

    print(pq)
    assert not pq.is_empty()
    next = pq.get()
    print(pq)
    assert next == "code"
    next = pq.get()
    next = pq.get()
    print(pq)
    assert pq.is_empty()