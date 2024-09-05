# test_a_star_search.py
from a_star_search import heuristic_distance, a_star
from lists_2d import PROJECT_ROOT, read_maze
import os

def test_heuristic_same_point():
    p1 = (2, 2)
    p2 = (2, 2)
    assert heuristic_distance(p1, p2) == 0


def test_heuristic_neighbors():
    p1 = (2, 2)
    p2 = (1, 2)
    assert heuristic_distance(p1, p2) == 1


def test_heuristic_big_gap_with_negative():
    p1 = (2, 2)
    p2 = (4, 4)
    assert heuristic_distance(p1, p2) == 4


def test_heuristic_big_gap_with_negative():
    p1 = (2, 2)
    p2 = (-2, -2)
    assert heuristic_distance(p1, p2) == 8

def test_1():
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

def test_2():
    maze_path = os.path.join(PROJECT_ROOT, "mazes", "mini_maze_bfs.txt")
    maze = read_maze(maze_path)
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

def test_3():
    maze_path = os.path.join(PROJECT_ROOT, "mazes", "mini_maze_bfs.txt")
    maze = read_maze(maze_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None

if __name__ == "__main__":
    test_1()