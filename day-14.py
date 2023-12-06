# https://adventofcode.com/2023/day/14
import numpy as np
from hashlib import sha256


def hash_platform(platform):
    return sha256(platform.tobytes()).hexdigest()


def calculate_north_load(platform):
    return np.sum((platform == 1) * (cols - np.arange(rows)[:, None]))


def sweep_platform(platform, row_indices, col_indices):
    rows, cols = platform.shape
    for j in col_indices:
        pos_i = 0
        for i in row_indices:
            if platform[i, j] == 1:
                if i != pos_i:
                    platform[i, j], platform[pos_i, j] = 0, 1
                pos_i += 1
            elif platform[i, j] == 2:
                pos_i = i + 1

    for i in row_indices:
        pos_j = 0
        for j in col_indices:
            if platform[i, j] == 1:
                if j != pos_j:
                    platform[i, j], platform[i, pos_j] = 0, 1
                pos_j += 1
            elif platform[i, j] == 2:
                pos_j = j + 1

    for j in col_indices:
        pos_i = rows - 1
        for i in row_indices[::-1]:
            if platform[i, j] == 1:
                if i != pos_i:
                    platform[i, j], platform[pos_i, j] = 0, 1
                pos_i -= 1
            elif platform[i, j] == 2:
                pos_i = i - 1

    for i in row_indices:
        pos_j = cols - 1
        for j in col_indices[::-1]:
            if platform[i, j] == 1:
                if j != pos_j:
                    platform[i, j], platform[i, pos_j] = 0, 1
                pos_j -= 1
            elif platform[i, j] == 2:
                pos_j = j - 1


with open("input-14.txt", "r") as f:
    lines = f.read()

lines = lines.translate(str.maketrans({".": "0", "O": "1", "#": "2"}))
platform = np.array([list(line) for line in lines.split("\n")], dtype=np.int8)

rows, cols = platform.shape
row_indices, col_indices = np.arange(rows), np.arange(cols)

repeat_start, cycle_length = None, None
seen_states = {}
final_state = None
total_iterations = 1000000000
for x in range(total_iterations):
    platform_hash = hash_platform(platform)
    if platform_hash in seen_states:
        repeat_start, _ = seen_states[platform_hash]
        cycle_length = x - repeat_start
        break

    seen_states[platform_hash] = (x, platform.copy())
    sweep_platform(platform, row_indices, col_indices)
else:
    final_state = platform

if final_state is None:
    assert cycle_length is not None

    final_iteration_within_cycle = (total_iterations - repeat_start) % cycle_length
    for x, state in seen_states.values():
        if x == repeat_start + final_iteration_within_cycle:
            final_state = state
            break

print(calculate_north_load(final_state))
