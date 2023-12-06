# https://adventofcode.com/2023/day/16
from collections import deque

STEP_RIGHT = (0, 1)
STEP_LEFT = (0, -1)
STEP_UP = (-1, 0)
STEP_DOWN = (1, 0)

STEPS = {
    ".": {
        STEP_RIGHT: [STEP_RIGHT],
        STEP_LEFT: [STEP_LEFT],
        STEP_UP: [STEP_UP],
        STEP_DOWN: [STEP_DOWN],
    },
    "|": {
        STEP_RIGHT: [STEP_UP, STEP_DOWN],
        STEP_LEFT: [STEP_UP, STEP_DOWN],
        STEP_UP: [STEP_UP],
        STEP_DOWN: [STEP_DOWN],
    },
    "-": {
        STEP_RIGHT: [STEP_RIGHT],
        STEP_LEFT: [STEP_LEFT],
        STEP_UP: [STEP_LEFT, STEP_RIGHT],
        STEP_DOWN: [STEP_LEFT, STEP_RIGHT],
    },
    "/": {
        STEP_RIGHT: [STEP_UP],
        STEP_LEFT: [STEP_DOWN],
        STEP_UP: [STEP_RIGHT],
        STEP_DOWN: [STEP_LEFT],
    },
    "\\": {
        STEP_RIGHT: [STEP_DOWN],
        STEP_LEFT: [STEP_UP],
        STEP_UP: [STEP_LEFT],
        STEP_DOWN: [STEP_RIGHT],
    },
}

with open("input-16.txt", "r") as f:
    lines = [line.strip() for line in f]

rows = len(lines)
cols = len(lines[0])

to_check = (
    [(0, j, STEP_DOWN) for j in range(cols)]
    + [(rows - 1, j, STEP_UP) for j in range(cols)]
    + [(i, 0, STEP_RIGHT) for i in range(rows)]
    + [(i, cols - 1, STEP_LEFT) for i in range(rows)]
)

totals = []
for start in to_check:
    visited = set()
    unique = set()
    to_visit = deque([start])
    while bool(to_visit):
        next = to_visit.popleft()

        if next in visited:
            continue

        visited.add(next)

        i, j, step = next
        unique.add((i, j))
        for next_step in STEPS[lines[i][j]][step]:
            if 0 <= i + next_step[0] < rows and 0 <= j + next_step[1] < cols:
                to_visit.append((i + next_step[0], j + next_step[1], next_step))

    totals.append(len(unique))

print(max(totals))
