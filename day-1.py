# https://adventofcode.com/2023/day/1
import re

with open("input-1.txt", "r") as f:
    lines = f.read()

MAP = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

for old, new in MAP.items():
    lines = lines.replace(old, new)

calibration = 0
for line in lines.split("\n"):
    digits = re.findall(r"\d", line)
    if digits:
        calibration += 10 * int(digits[0]) + int(digits[-1])

print(calibration)
