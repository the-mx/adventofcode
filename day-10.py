# https://adventofcode.com/2023/day/10
import typing

DIRECTIONS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "7": ((0, -1), (1, 0)),
    "F": ((1, 0), (0, 1)),
}
RDIRECTIONS = {v: k for k, v in DIRECTIONS.items()}


def read_area() -> typing.List[str]:
    with open("input-10.txt", "r") as f:
        lines = ["." + line.strip() + "." for line in f.readlines()]
    padding = "." * len(lines[0])
    return [padding] + lines + [padding]


def find_start(area: typing.List[str]) -> typing.Tuple[int, int]:
    for i, row in enumerate(area):
        if "S" in row:
            return i, row.index("S")
    assert False, "S not found"


def trace_loop(
    area: typing.List[str],
) -> typing.Tuple[str, typing.Set[typing.Tuple[int, int]]]:
    max_loop = set()
    sdir = None
    start_directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while start_directions:
        start_direction = start_directions.pop()
        d = start_direction
        n, m = sn, sm
        loop = set()
        while True:
            n, m = n + d[0], m + d[1]
            rev = (-d[0], -d[1])
            p = area[n][m]
            loop.add((n, m))

            if p == ".":
                break

            if p == "S":
                start_directions.remove(rev)
                if len(max_loop) >= len(loop):
                    break
                max_loop = loop
                sdir = RDIRECTIONS[start_direction, rev]
                break

            pd = DIRECTIONS[p]
            if rev not in pd:
                break
            d = pd[0] if pd[0] != rev else pd[1]

    return sdir, max_loop


def count_nests(area: typing.List[str], top_edges: str) -> int:
    nests = 0
    for i in range(1, len(area) - 1):
        line = area[i]
        is_within_nest = False
        for j in range(1, len(area[i]) - 1):
            if (i, j) in max_loop:
                if line[j] in top_edges:
                    is_within_nest = not is_within_nest
            elif is_within_nest:
                nests += 1
    return nests


area = read_area()
sn, sm = find_start(area)
sdir, max_loop = trace_loop(area)

top_edges = "|LJ"
if sdir in top_edges:
    top_edges += "S"

nests = count_nests(area, top_edges)
print(nests)
