import itertools
import math
import re

with open("input-8.txt", "r") as f:
    direction_instructions = f.readline().strip()
    mapping_data = f.read()

binary_instructions = [
    0 if direction == "L" else 1 for direction in direction_instructions
]

landmark_pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
landmarks = {
    start: (left, right)
    for start, left, right in landmark_pattern.findall(mapping_data)
}

starting_points = [landmark for landmark in landmarks if landmark.endswith("A")]
stopping_points = {landmark for landmark in landmarks if landmark.endswith("Z")}

steps = []
for starting_point in starting_points:
    for step, instruction in enumerate(itertools.cycle(binary_instructions), start=1):
        starting_point = landmarks[starting_point][instruction]

        if starting_point in stopping_points:
            steps.append(step)
            break

total_steps = math.lcm(*steps)
print(total_steps)
