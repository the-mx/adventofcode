# https://adventofcode.com/2023/day/21
import sys
import numpy
import heapq
from typing import List, Tuple, Dict


def find_start(grid: List[str]) -> Tuple[int, int] | None:
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                return i, j
    return None


def dijkstra(
    grid: List[str], dest: Tuple[int, int], limit: int
) -> Dict[Tuple[int, int], int]:
    rows = len(grid)
    cols = len(grid[0])

    distances = {dest: 0}
    pq = [(0, dest)]
    while pq:
        dist, (i, j) = heapq.heappop(pq)

        if distances[i, j] != dist:
            continue

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if grid[ni % rows][nj % cols] != "#":
                new_dist = dist + 1
                if (
                    new_dist < distances.get((ni, nj), sys.maxsize)
                    and new_dist <= limit
                ):
                    distances[ni, nj] = new_dist
                    heapq.heappush(pq, (new_dist, (ni, nj)))

    return distances


def calculate_plots(distances: Dict[Tuple[int, int], int], limit) -> int:
    return len([d for d in distances.values() if (limit - d) % 2 == 0])


with open("input-21.txt", "r") as f:
    lines = f.read()

# Part 1
grid = lines.split("\n")
start = find_start(grid)
distances = dijkstra(grid, start, limit=64)
print(calculate_plots(distances, limit=64))

# Part 2

# Ad-hoc for the input.
# Starting point is (65, 65), the grid is square, the size is 131x131.
# All edges are plots and starting point is directly accessible.
# Required steps are 26501365 = 202300 * 131 + 65.

steps = [65 + 131 * x for x in range(0, 10)]
plots = [calculate_plots(dijkstra(grid, start, limit), limit) for limit in steps]

print(steps)
print(plots)

difference1 = numpy.diff(plots)
print(difference1)

# The differences between consecutive values seem to form an arithmetic sequence.

difference2 = numpy.diff(difference1)
print(difference2)

# The second differences are all the same. This indicates the quadratic function.

a, b, c = numpy.polyfit(range(len(plots)), plots, 2)
print(a, b, c)

target = 202300
plots = a * target * target + b * target + c
print(plots)
