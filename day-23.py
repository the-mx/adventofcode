# https://adventofcode.com/2023/day/23
import numpy as np
from typing import Tuple, List, Set, Dict


def parse_input(filepath: str) -> np.ndarray:
    with open(filepath, "r") as f:
        lines = f.read()

    lines = (
        lines.replace("#", "1")
        .replace(".", "0")
        .replace("<", "0")
        .replace(">", "0")
        .replace("^", "0")
        .replace("v", "0")
    )

    return np.array(
        [np.array(list(map(int, [c for c in line]))) for line in lines.split("\n")],
        dtype=np.int8,
    )


def find_grid_endpoints(grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    rows, cols = grid.shape
    grid_start = (0, np.argmin(grid[0]))
    grid_end = (rows - 1, np.argmin(grid[rows - 1]))
    return grid_start, grid_end


def find_intersections_graph(
    grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]
) -> Dict[Tuple[int, int], Dict[Tuple[int, int], int]]:
    nodes = {start: {}, end: {}}
    queue: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [
        (start, (start[0] + 1, start[1]))
    ]

    idx = 0
    while idx < len(queue):
        node_id, step = queue[idx]

        length = 1
        prev_cell = node_id
        cell = step

        while True:
            if cell == end:
                break

            x, y = cell
            neighbors = [
                (x + dx, y + dy)
                for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]
                if grid[x + dx, y + dy] == 0 and (x + dx, y + dy) != prev_cell
            ]
            if len(neighbors) == 1:
                length += 1
                prev_cell = cell
                cell = neighbors[0]
            else:
                break

        if cell == end or len(neighbors) != 0:
            is_new_node = cell not in nodes
            current_node = nodes.setdefault(node_id, {})
            met_node = nodes.setdefault(cell, {})
            current_node[cell] = max(current_node.get(cell, 0), length)
            met_node[node_id] = max(met_node.get(node_id, 0), length)

            if is_new_node:
                queue.extend((cell, n) for n in neighbors)

        idx += 1

    return nodes


def main():
    grid = parse_input("input-23.txt")
    grid_start, grid_end = find_grid_endpoints(grid)

    nodes = find_intersections_graph(grid, grid_start, grid_end)

    def dfs_longest_path(
        node: Tuple[int, int],
        score: int,
        seen: Set[Tuple[int, int]],
        max_score: List[int],
    ) -> int:
        if node == grid_end:
            max_score[0] = max(max_score[0], score)
            return max_score[0]

        for p, dist in nodes[node].items():
            if p in seen:
                continue
            dfs_longest_path(p, score + dist, seen | {node}, max_score)
        return max_score[0]

    print(dfs_longest_path(grid_start, 0, set(), [0]))


main()
