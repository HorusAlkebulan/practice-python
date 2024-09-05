import os
import os
import pytest

PROJECT_ROOT = os.path.dirname(__file__)


def read_maze(file_path):

    print(f"Loading maze file: {file_path}")

    with open(file_path, mode="r") as f:
        maze = []
        file_lines = f.readlines()
        file_maze_row_count = len(file_lines)
        for line in file_lines:
            maze_row = []
            for char in line.strip("\n"):
                maze_row.append(char)
            maze_row_col_count = len(maze_row)
            if file_maze_row_count == maze_row_col_count:
                maze.append(maze_row)
            else:
                raise OSError(
                    f"Maze is not rectangular: rows={file_maze_row_count}, columns={maze_row_col_count}"
                )
    return maze


if __name__ == "__main__":

    maze_path = os.path.join(PROJECT_ROOT, "mazes", "modest_maze.txt")
    maze = read_maze(maze_path)

    print(f"maze: {maze_path}")

    for i, row in enumerate(maze):
        cols_in_row = ""
        for col in row:
            cols_in_row += col
        print(f"{i:2d}: {cols_in_row}")
