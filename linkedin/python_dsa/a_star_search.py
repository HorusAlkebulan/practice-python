from priority_queue import PriorityQueue
from maze_utils import get_path, is_visitable_cell
from constants import OFFSETS


def heuristic_distance(p1: tuple, p2: tuple) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze: list, start_cell: tuple, goal_cell: tuple) -> list:

    # initialize
    pq = PriorityQueue()
    pq.put(0, start_cell)
    predecessors = {start_cell: None}
    g_values = {start_cell: 0}

    # algorithm
    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal_cell:
            return get_path(predecessors, start_cell, current_cell)
        else:
            directions = ["up", "right", "down", "left"]
            for direction in directions:
                offset = OFFSETS[direction]
                neighbor_cell = (
                    current_cell[0] + offset[0],
                    current_cell[1] + offset[1],
                )
                if (
                    is_visitable_cell(maze, neighbor_cell)
                    and neighbor_cell not in g_values
                ):
                    # add default cost for our maze: 1
                    new_cost = g_values[current_cell] + 1
                    g_values[neighbor_cell] = new_cost
                    f_value = new_cost + heuristic_distance(neighbor_cell, goal_cell)
                    pq.put(f_value, neighbor_cell)
                    predecessors[neighbor_cell] = current_cell
    return None
