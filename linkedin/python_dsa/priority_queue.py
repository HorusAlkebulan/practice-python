
import heapq


class PriorityQueue():
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return (len(self.elements) == 0)
    
    def put(self, priority, item) -> None:
        queue_element = (priority, item)
        heapq.heappush(self.elements, queue_element)

    def get(self) -> any:
        element_tuple = heapq.heappop(self.elements)
        return element_tuple[1]
    
    def __str__(self) -> str:
        return f"size: {len(self.elements)}, elements: {str(self.elements)}"
    

def process_tasks(tasks):
    # Create a priority queue

    # Iterate through the tasks
    for task, priority in tasks:
        # Add each task to the priority queue along with its priority value
        pass
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type (list in this case)
    # and build the solution by filling the bucket within a loop.
    ordered_task_list = []

    # Use a while loop with the exit condition that the priority queue is empty.
    # Within this loop, update result with items got from the priority queue.


    return ordered_task_list
