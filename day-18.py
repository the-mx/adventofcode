# https://adventofcode.com/2023/day/18
DS = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
    "0": (0, 1),
    "1": (1, 0),
    "2": (0, -1),
    "3": (-1, 0),
}


def shoelace_area(points):
    n = len(points)
    internal_area = 0
    perimeter = 0
    for i in range(n):
        j = (i + 1) % n
        internal_area += points[i][0] * points[j][1]
        internal_area -= points[j][0] * points[i][1]

        perimeter += abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])

    internal_area = abs(internal_area) / 2

    return internal_area + perimeter / 2 + 1


with open("input-18.txt", "r") as f:
    lines = f.read()

# Part 1
# directions = [(DS[d], int(steps)) for d, steps, color in [line.split(" ") for line in lines.split("\n")]]

# Part 2
directions = [
    (DS[code[5]], int(f"0x{code[:5]}", 16))
    for _, code in [line.split("#") for line in lines.split("\n")]
]

point = (0, 0)
points = []
for d, steps in directions:
    point = point[0] + d[0] * steps, point[1] + d[1] * steps
    points.append(point)

print(shoelace_area(points))
