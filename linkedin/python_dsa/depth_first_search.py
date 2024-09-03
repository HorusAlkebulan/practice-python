
from stack import Stack

def get_path(predecessors: dict, start_cell: tuple, current_cell: tuple) -> list:
    path_lst = [current_cell]
    while predecessor is not None and current_cell != start_cell:
        predecessor = predecessors[current_cell]
        path_lst.append(predecessor)
    return path_lst

def is_visitable_cell(maze: list, current_cell: tuple) -> bool:
    # get cell boundaries
    maze_num_rows = len(maze)
    maze_num_cols = len(maze[0])
    if current_cell[0] < maze_num_rows and current_cell[1] < maze_num_cols and current_cell[0] > -1 and current_cell[1] > -1:    
        # get cell contents
        cell_contents = maze[current_cell[0]][current_cell[1]]

        # if contains any obstactles, return False
        if cell_contents == "*":
            return False
        # otherwise return true
        else:
            return True
    else:
        return False

def dfs(maze: list, start_pos: tuple, goal_pos: tuple) -> list:

    # initalize
    stack = Stack()
    stack.push(start_pos)
    predecessors = {start_pos: None}

    # algorithm
    while not stack.is_empty():
        # pop the stack
        current_cell = stack.pop()

        # is this the goal?
        if current_cell == goal_pos:
            # if yes, return success
            success_path = get_path(predecessors, start_pos, current_cell)
            return success_path
        else:
            # otherwise, push unvisited neighbors on to the stack and predecessors map
            # convention: start at 12 o'clock and go clockwise
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                neighboring_cell: tuple = (current_cell[0] + direction[0], current_cell[1] + direction[1])
                if is_visitable_cell(maze, neighboring_cell) and neighboring_cell not in predecessors:
                    stack.push(neighboring_cell)
                    predecessors[neighboring_cell] = current_cell 

    return None