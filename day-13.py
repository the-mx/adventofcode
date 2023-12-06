# https://adventofcode.com/2023/day/13
import numpy as np

with open("input-13.txt", "r") as f:
    lines = f.read()

patterns = []
pattern = []
for line in lines.split("\n"):
    if not line:
        patterns.append(np.array(pattern))
        pattern.clear()
    else:
        pattern.append(np.array([int(c == "#") for c in line], dtype=np.int8))

if pattern:
    patterns.append(np.array(pattern))


def find_reflection(matrix, diff):
    rows, cols = matrix.shape
    for offset in range(1, rows):
        size = min(offset, rows - offset)
        diff_count = np.sum(
            np.abs(
                matrix[offset - size : offset, :]
                - np.flip(matrix[offset : offset + size, :], 0)
            )
        )
        if diff_count == diff:
            return offset
    return None


total = 0
for pattern in patterns:
    r = find_reflection(pattern, diff=1)
    if r is not None:
        total += r * 100
        continue

    r = find_reflection(np.transpose(pattern), diff=1)
    if r is not None:
        total += r
        continue

print(total)
