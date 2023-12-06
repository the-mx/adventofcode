# https://adventofcode.com/2023/day/17
import heapq
import sys

STEP_RIGHT = (0, 1)
STEP_LEFT = (0, -1)
STEP_UP = (-1, 0)
STEP_DOWN = (1, 0)
STEP_FIRST = (0, 0)

DIRECTIONS = {
    STEP_FIRST: [STEP_RIGHT, STEP_DOWN],
    STEP_RIGHT: [STEP_RIGHT, STEP_UP, STEP_DOWN],
    STEP_LEFT: [STEP_LEFT, STEP_UP, STEP_DOWN],
    STEP_DOWN: [STEP_DOWN, STEP_LEFT, STEP_RIGHT],
    STEP_UP: [STEP_UP, STEP_LEFT, STEP_RIGHT],
}

MAX_STRAIGHT_STEPS = 10
MIN_STRAIGHT_STEPS = 4


def dijkstra(lines) -> int:
    rows = len(lines)
    cols = len(lines[0])

    distances = {}

    # Priority queue:
    pq = [(0, (0, 0), STEP_FIRST, 0)]
    while pq:
        current_dist, current_pos, current_direction, steps = heapq.heappop(pq)

        if current_pos == (rows - 1, cols - 1):
            return current_dist

        for next_direction in DIRECTIONS[current_direction]:
            if next_direction != current_direction:
                next_pos = (
                    current_pos[0] + MIN_STRAIGHT_STEPS * next_direction[0],
                    current_pos[1] + MIN_STRAIGHT_STEPS * next_direction[1],
                )

                if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                    continue

                next_steps = MIN_STRAIGHT_STEPS
                next_dist = current_dist
                next_pos = current_pos
                for _ in range(MIN_STRAIGHT_STEPS):
                    next_pos = (
                        next_pos[0] + next_direction[0],
                        next_pos[1] + next_direction[1],
                    )
                    next_dist += lines[next_pos[0]][next_pos[1]]

            elif steps + 1 <= MAX_STRAIGHT_STEPS:
                next_pos = (
                    current_pos[0] + next_direction[0],
                    current_pos[1] + next_direction[1],
                )
                if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                    continue

                next_steps = steps + 1
                next_dist = current_dist + lines[next_pos[0]][next_pos[1]]
            else:
                continue

            best_dist = distances.get(
                (next_pos, next_direction, next_steps), sys.maxsize
            )
            if next_dist < best_dist:
                distances[(next_pos, next_direction, next_steps)] = next_dist
                heapq.heappush(pq, (next_dist, next_pos, next_direction, next_steps))


with open("input-17.txt", "r") as f:
    lines = [[int(c) for c in line.strip()] for line in f]

print(dijkstra(lines))
