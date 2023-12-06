# https://adventofcode.com/2023/day/19
import re
from collections import deque
from functools import reduce
from typing import Dict, List, Tuple

Instruction = Tuple[str, List[int], str]
Workflow = Tuple[List[Instruction], str]
Part = Dict[str, int]

MIN_VALUE = 1
MAX_VALUE = 4000
DEFAULT_WORKFLOW = "in"

# Precompiled regex patterns
PATTERN_WORKFLOW = re.compile(r"^([a-z]+){(.+,)([ARa-z]+)}")
PATTERN_INSTRUCTIONS = re.compile(r"([xmas])([<>])([0-9]+):([ARa-z]+),")
PATTERN_PART = re.compile(r"([xmas])=([0-9]+)")


def read_input(filename) -> Tuple[List[str], List[str]]:
    with open(filename, "r") as f:
        workflows_lines, parts_lines = f.read().strip().split("\n\n")
    return workflows_lines.split("\n"), parts_lines.split("\n")


def parse_workflows(workflows_lines: List[str]) -> Dict[str, Workflow]:
    workflows = {}
    for line in workflows_lines:
        name, instructions, default = PATTERN_WORKFLOW.match(line).groups()
        parsed_instructions = [
            (
                cat,
                [MIN_VALUE, int(value) - 1]
                if sign == "<"
                else [int(value) + 1, MAX_VALUE],
                w,
            )
            for cat, sign, value, w in PATTERN_INSTRUCTIONS.findall(instructions)
        ]
        workflows[name] = (parsed_instructions, default)
    return workflows


def parse_parts(parts_lines: List[str]) -> List[Part]:
    return [{k: int(v) for k, v in PATTERN_PART.findall(line)} for line in parts_lines]


def evaluate_part(part: Part, workflows: Dict[str, Workflow]) -> bool:
    workflow = DEFAULT_WORKFLOW
    while True:
        instructions, default = workflows[workflow]
        for cat, values, w in instructions:
            if values[0] <= part[cat] <= values[1]:
                workflow = w
                break
        else:
            workflow = default

        if workflow == "A":
            return True
        elif workflow == "R":
            return False


def evaluate_parts(workflows: Dict[str, Workflow], parts: List[Part]) -> List[Part]:
    return [part for part in parts if evaluate_part(part, workflows)]


def calculate_total(accepted_parts: List[Dict[str, int]]) -> int:
    return sum(sum(part.values()) for part in accepted_parts)


def calculate_combinations(workflows: Dict[str, Workflow]) -> int:
    combs_to_check = deque(
        [
            (DEFAULT_WORKFLOW, {cat: [MIN_VALUE, MAX_VALUE] for cat in "xmas"}),
        ]
    )
    accepted = []
    while combs_to_check:
        cur_wf_name, cur_comb = combs_to_check.popleft()
        instructions, default = workflows[cur_wf_name]
        next_wf_name = None
        for cat, values, wf_name in instructions:
            [left, right] = cur_comb[cat]
            if right < values[0] or left > values[1]:
                continue

            if left >= values[0] and right <= values[1]:
                next_wf_name = wf_name
                break

            if left >= values[0]:
                new_ranges = [[left, values[1]], [values[1] + 1, right]]
            else:
                new_ranges = [[left, values[0] - 1], [values[0], right]]

            for r in new_ranges:
                next_comb = cur_comb.copy()
                next_comb[cat] = r
                combs_to_check.append((cur_wf_name, next_comb))
            break
        else:
            next_wf_name = default

        if next_wf_name is None:
            continue
        elif next_wf_name == "A":
            accepted.append(cur_comb)
        elif next_wf_name != "R":
            combs_to_check.append((next_wf_name, cur_comb))

    return sum(
        [reduce(lambda a, b: a * (b[1] - b[0] + 1), c.values(), 1) for c in accepted]
    )


def main():
    workflows_lines, parts_lines = read_input("input-19.txt")
    workflows = parse_workflows(workflows_lines)

    # Part 1
    parts = parse_parts(parts_lines)
    accepted_parts = evaluate_parts(workflows, parts)
    total = calculate_total(accepted_parts)
    print(total)

    # Part 2
    combindations = calculate_combinations(workflows)
    print(combindations)


main()
