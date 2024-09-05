# breadth_first_search.py

from constants import HR, OFFSETS
from maze_utils import get_path, is_visitable_cell
from queue_using_deque import Queue


def bfs(maze: list, start_pos: tuple, goal_pos: tuple) -> list:
    
    # initialize
    queue = Queue()
    queue.enqueue(start_pos)
    predecessors = {start_pos: None}

    # algorithm
    while not queue.is_empty():
        print(HR)

        # pull from queue
        current_cell = queue.dequeue()

        # is this the goal, return success path
        if current_cell == goal_pos:
            return get_path(predecessors, start_pos, current_cell)
        
        # otherwise, queue up unvisited neighbors in order of 12 o'clock then clockwise
        else:
            directions = ["up", "right", "down", "left"]
            for direction in directions:
                offset = OFFSETS[direction]
                neighbor_cell = (
                    current_cell[0] + offset[0],
                    current_cell[1] + offset[1],
                )

                # if neighbor is visitable and not already processed, queue it up
                if (
                    is_visitable_cell(maze, neighbor_cell)
                    and neighbor_cell not in predecessors
                ):
                    queue.enqueue(neighbor_cell)
                    # also, add neighbor to pred dict
                    predecessors[neighbor_cell] = current_cell
                else:
                    print(f"Cell not visitable: {neighbor_cell}")

    # if we get here, no path found
    return None
