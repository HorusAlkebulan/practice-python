def get_path(predecessors: dict, start_cell: tuple, current_cell: tuple) -> list:
    current = current_cell
    path = []
    while current != start_cell:
        path.append(current)
        current = predecessors[current]
    path.append(start_cell)
    path.reverse()
    return path


def is_visitable_cell(maze: list, current_cell: tuple) -> bool:
    # get cell boundaries
    maze_num_rows = len(maze)
    maze_num_cols = len(maze[0])
    if (
        current_cell[0] < maze_num_rows
        and current_cell[1] < maze_num_cols
        and current_cell[0] > -1
        and current_cell[1] > -1
    ):
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
