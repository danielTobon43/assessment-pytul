import numpy as np
import collections
import configparser


def bfs(grid: np.array, start: tuple, goal: tuple) -> list:
    """
    Breadth-First Search (BFS) - Iterative and Recursive Implementation

    Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores the neighbor nodes first before moving to the next-level neighbors.

    solution based on https://stackoverflow.com/a/47902476/16633625
    """
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            path.remove(start)
            path.remove(goal)
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < grid.shape[0] and 0 <= y2 < grid.shape[1] and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


if __name__ == "__main__":
    # configuration file
    config = configparser.ConfigParser()
    config.read("config.ini")

    # setting parameters
    n_size = int(config["DEFAULT"]["size"])
    start = tuple(map(int, config["DEFAULT"]["start"].split(",")))
    goal = tuple(map(int, config["DEFAULT"]["goal"].split(",")))

    # setting square matrix
    matrix = np.ones((n_size, n_size), dtype=int)
    print("- input matrix: ")
    print(matrix)

    # running shortest path algorithm
    shortest_path = bfs(matrix, start, goal)
    print(f"\n- shortest path: {shortest_path}")
    print(f"- cost: {len(shortest_path)}")
