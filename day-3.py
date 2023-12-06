# https://adventofcode.com/2023/day/3

import re

with open("input-3.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")
width = len(lines[0])
height = len(lines)
gears = {}

for idx, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        value = int(match.group(0))

        for i in range(max(0, idx - 1), min(height, idx + 2)):
            for j in range(max(0, match.start() - 1), min(width, match.end() + 1)):
                if not lines[i][j].isnumeric() and lines[i][j] != ".":
                    gears.setdefault((i, j), []).append(int(match.group(0)))

total = sum(v[0] * v[1] for v in gears.values() if len(v) == 2)
print(total)
