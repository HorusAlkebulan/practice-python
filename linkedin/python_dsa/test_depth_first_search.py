# test_depth_first_search.py
from depth_first_search import dfs
from lists_2d import PROJECT_ROOT, read_maze
import os

def test_1():
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

def test_2():
    maze_path = os.path.join(PROJECT_ROOT, "mazes", "mini_maze_dfs.txt")
    maze = read_maze(maze_path)
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

def test_3():
    maze_path = os.path.join(PROJECT_ROOT, "mazes", "mini_maze_dfs.txt")
    maze = read_maze(maze_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None

if __name__ == "__main__":
    test_1()