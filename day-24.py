# https://adventofcode.com/2023/day/24
import numpy as np

LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000
LOWER_LEFT = np.array([LOWER_BOUND, LOWER_BOUND])
UPPER_RIGHT = np.array([UPPER_BOUND, UPPER_BOUND])


with open("input-24.txt", "r") as f:
    lines = f.read()

hailstones = [
    (np.fromstring(ps, dtype=int, sep=",")[:2], np.fromstring(vs, dtype=int, sep=",")[:2])
    for ps, vs in (line.split("@") for line in lines.split("\n"))
]

norms = np.linalg.norm([h[1] for h in hailstones], axis=1)

total = 0
for i in range(len(hailstones) - 1):
    pi, vi = hailstones[i]
    norm_vi = norms[i]

    for j in range(i + 1, len(hailstones)):
        pj, vj = hailstones[j]
        norm_vj = norms[j]

        dot_product = np.dot(vi, vj)
        if np.isclose(np.abs(dot_product), norm_vi * norm_vj):
            continue

        A = np.stack([vi, -vj], axis=1)
        b = pj - pi
        t = np.linalg.solve(A, b)

        if np.any(t < 0):
            continue

        intersection = pi + t[0] * vi
        if np.all(LOWER_LEFT <= intersection) and np.all(intersection <= UPPER_RIGHT):
            total += 1

print(total)
