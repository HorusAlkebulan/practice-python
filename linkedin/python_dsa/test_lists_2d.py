# test_lists_2d.py
from lists_2d import read_maze
import os
import pytest

PROJECT_ROOT = os.path.dirname(__file__)


def test_read_maze_rectangular():
    maze_path = os.path.join(PROJECT_ROOT, "test_maze_rectangular.txt")
    maze = read_maze(maze_path)
    assert maze is not None


def test_read_maze_non_rectangular():
    maze_path = os.path.join(PROJECT_ROOT, "test_maze_non_rectangular.txt")
    with pytest.raises(OSError) as e:
        maze = read_maze(maze_path)
        assert maze is None
