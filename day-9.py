# https://adventofcode.com/2023/day/9
import numpy

with open("input-9.txt", "r") as f:
    lines = f.read()

sequences = [list(map(int, line.split())) for line in lines.split("\n")]

total_next = 0
total_prev = 0
for sequence in sequences:
    prev_value = sequence[0]
    next_value = 0
    s = -1
    while not all(v == 0 for v in sequence):
        next_value += sequence[-1]
        sequence = numpy.diff(sequence)
        prev_value += s * sequence[0]
        s = -1 * s
    total_next += next_value
    total_prev += prev_value

print(total_next)
print(total_prev)
