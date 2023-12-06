# https://adventofcode.com/2023/day/11
import typing

with open("input-11.txt", "r") as f:
    lines = f.read()

lines = [line for line in lines.split("\n")]
xs = []
ys = []
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == "#":
            xs.append(x)
            ys.append(y)

ys.sort()


def expand_universe(r: typing.List[int]):
    incr = 0
    prev = -1
    for i in range(0, len(r)):
        if r[i] + incr - prev > 1:
            incr += 999999
        r[i] += incr
        prev = r[i]


expand_universe(xs)
expand_universe(ys)


def calc_sums(r: typing.List[int]):
    return [sum([r[j] - r[i] for j in range(i + 1, len(r))]) for i in range(0, len(r))]


xsums = calc_sums(xs)
ysums = calc_sums(ys)
total = sum(xsums) + sum(ysums)

print(total)
