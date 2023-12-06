# https://adventofcode.com/2023/day/15


def string_hash(text):
    value = 0
    for char in text:
        code = ord(char)
        value = ((value + code) * 17) & 255
    return value


def do_step(step, boxes):
    if step[-1] == "-":
        label = step[:-1]
        box_number = string_hash(label)
        boxes[box_number] = [(lb, fc) for lb, fc in boxes[box_number] if lb != label]
    else:
        label, focal = step.split("=")
        box_number = string_hash(label)
        for i, (lb, fc) in enumerate(boxes[box_number]):
            if lb == label:
                boxes[box_number][i] = (label, focal)
                break
        else:
            boxes[box_number].append((label, focal))


with open("input-15.txt", "r") as f:
    steps = f.read().strip().split(",")

boxes = [[] for _ in range(256)]
for step in steps:
    do_step(step, boxes)

power = sum(
    box_power * slot * int(focal)
    for box_power, box in enumerate(boxes, start=1)
    for slot, (label, focal) in enumerate(box, start=1)
)
print(power)
