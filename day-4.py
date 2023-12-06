# https://adventofcode.com/2023/day/4
import re

with open("input-4.txt", "r") as f:
    lines = f.read()

lines = lines.split("\n")
length = len(lines)
cards = [
    1,
] * length

total = 0
pattern = re.compile(r"(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)")
for idx, line in enumerate(lines):
    matches = pattern.findall(line)
    winning = set(map(int, matches[0][0].split()))
    mine = set(map(int, matches[0][1].split()))
    number = len(winning.intersection(mine))
    for i in range(idx + 1, min(idx + number + 1, length)):
        cards[i] += cards[idx]

print(sum(cards))
