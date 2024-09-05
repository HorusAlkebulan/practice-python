from constants import HR
from maze_utils import get_path, is_visitable_cell
from stack import Stack


def dfs(maze: list, start_pos: tuple, goal_pos: tuple) -> list:

    # initalize
    stack = Stack()
    stack.push(start_pos)
    predecessors = {start_pos: None}

    # algorithm
    while not stack.is_empty():
        print(HR)

        # pop the stack
        current_cell = stack.pop()

        # is this the goal?
        if current_cell == goal_pos:
            # if yes, return success
            return get_path(predecessors, start_pos, current_cell)
        else:
            # otherwise, push unvisited neighbors on to the stack and predecessors map
            # convention: start at 12 o'clock and go clockwise
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                neighboring_cell: tuple = (
                    current_cell[0] + direction[0],
                    current_cell[1] + direction[1],
                )
                if (
                    is_visitable_cell(maze, neighboring_cell)
                    and neighboring_cell not in predecessors
                ):
                    print(
                        f"- Pushing neighbor {neighboring_cell} on the stack, logging it's preceeded by as {current_cell}"
                    )
                    stack.push(neighboring_cell)
                    predecessors[neighboring_cell] = current_cell
                    print(f"-- stack: {stack}")
                    print(f"-- predecessors: {predecessors}")

        print(f"After processing current_cell as {current_cell}:")
        print(f"stack: {stack}")
        print(f"predecessors: {predecessors}")
    return None
