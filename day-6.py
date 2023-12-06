# https://adventofcode.com/2023/day/6

import math

# TIMES = [7, 15, 30]
# DISTANCES = [9, 40, 200]
# TIMES = [56, 97, 78, 75]
# DISTANCES = [546, 1927, 1131, 1139]
TIMES = [56977875]
DISTANCES = [546192711311139]

options = 1
for time, distance in zip(TIMES, DISTANCES):
    d = math.sqrt(time * time - 4 * distance)
    x1 = (time - d) / 2.0
    x2 = (time + d) / 2.0
    x1 = math.ceil(x1) if math.ceil(x1) - x1 > 0.00000001 else int(x1) + 1
    x2 = math.floor(x2) if x2 - math.floor(x2) > 0.00000001 else int(x2) - 1
    options *= x2 - x1 + 1

print(options)
