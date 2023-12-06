# https://adventofcode.com/2023/day/12
import typing
from functools import lru_cache


@lru_cache(maxsize=None)
def calculate(clues: typing.Tuple[int], row: str) -> int:
    if not clues:
        return "#" not in row

    row = row.lstrip(".")
    if not row:
        return 0

    count = 0
    if row[0] == "?":
        count += calculate(clues, row[1:])

    if "." not in row[: clues[0]] and "#" != row[clues[0]]:
        count += calculate(clues[1:], row[clues[0] + 1 :])

    return count


with open("input-12.txt", "r") as f:
    lines = f.read()

count = 0
for line in lines.split("\n"):
    row, clues = line.split(" ")
    clues = tuple(map(int, clues.split(",")))

    # unfolding
    row = "?".join([row] * 5) + "."
    clues = clues * 5

    count += calculate(clues, row)

print(count)
