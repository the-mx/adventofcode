# https://adventofcode.com/2023/day/22
import numpy as np

with open("input-22.txt", "r") as f:
    lines = f.read()

starts = []
ends = []
blocks = []
for line in lines.split("\n"):
    start, end = line.split("~")
    blocks.append((list(map(int, start.split(","))), list(map(int, end.split(",")))))

blocks.sort(key=lambda block: block[0][2])

max_ends = np.amax(np.array([block[0] for block in blocks]), axis=0)
shape = max_ends + 1
pile = np.zeros(shape, dtype=np.int16)

supported_by = {}
for i, [start, end] in enumerate(blocks, start=1):
    while start[2] > 1:
        support = set(
            np.unique(pile[start[0] : end[0] + 1, start[1] : end[1] + 1, start[2] - 1])
        )
        if support == {0}:
            start[2] -= 1
            end[2] -= 1
        else:
            support.discard(0)
            supported_by[i] = support
            break
    pile[start[0] : end[0] + 1, start[1] : end[1] + 1, start[2] : end[2] + 1] = i

total = 0
for i in range(1, len(blocks) + 1):
    fell = {i}
    for j in range(i + 1, len(blocks) + 1):
        if j not in supported_by:
            continue
        if not (supported_by[j] - fell):
            fell.add(j)
    total += len(fell) - 1

print(total)
