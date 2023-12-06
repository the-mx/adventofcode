# https://adventofcode.com/2023/day/5
import re

with open("input-5.txt", "r") as f:
    lines = f.read()

seeds_pattern = re.compile(r"seeds:\s*([\d\s]+)")
seeds = list(map(int, seeds_pattern.search(lines)[1].split()))

map_pattern = re.compile(r"(\w+)-to-(\w+) map:\s*([\d\s]+)")

maps = [
    sorted(
        [list(map(int, line.split())) for line in values.split("\n") if line.strip()],
        key=lambda v: v[0],
    )
    for _, _, values in map_pattern.findall(lines)
]

# Any big enough number will work here
upper_bound = max([r[0] + r[1] + r[2] for m in maps for r in m])
upper_bound = max(upper_bound, 2 * max(seeds))

for m in maps:
    if m[0][0] != 0:
        m.insert(0, [0, 0, m[0][0]])
    m.append([m[-1][0] + m[-1][2], m[-1][0] + m[-1][2], upper_bound])


def find_seed(level, start, end):
    if level == -1:
        for i in range(0, len(seeds), 2):
            if start < seeds[i] + seeds[i + 1] and seeds[i] < end:
                return max(start, seeds[i])
        return None

    for dst_start, src_start, d in maps[level]:
        if start < dst_start + d and dst_start < end:
            intersection_start = max(start, dst_start)
            intersection_end = min(dst_start + d, end)
            next_start = intersection_start + src_start - dst_start
            next_end = intersection_end + src_start - dst_start
            seed = find_seed(level - 1, next_start, next_end)
            if seed is not None:
                return seed


def transform(v):
    for m in maps:
        for dst_start, src_start, d in m:
            if src_start <= v < src_start + d:
                v = dst_start + v - src_start
                break
    return v


seed = find_seed(len(maps) - 1, 0, upper_bound)
location = transform(seed)
print(location)
