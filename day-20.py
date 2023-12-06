# https://adventofcode.com/2023/day/20
import math

LOW_PULSE = 0
HIGH_PULSE = 1

with open("input-20.txt", "r") as f:
    lines = f.read()

outgoings = {}
incomings = {}
flip_flops = {}
conjunctions = {}
for line in lines.split("\n"):
    is_flip_flop = line[0] == "%"
    is_conjunction = line[0] == "&"
    if is_flip_flop or is_conjunction:
        line = line[1:]

    name, destinations = line.split(" -> ")
    outs = [d.strip() for d in destinations.split(",")]
    outgoings[name] = outs

    for out in outs:
        incomings.setdefault(out, []).append(name)

    if is_flip_flop:
        flip_flops[name] = False

    if is_conjunction:
        conjunctions[name] = {}

for name, ins in conjunctions.items():
    ins.update({node: LOW_PULSE for node in incomings[name]})

# Ad-hoc solution for my input.
watched_nodes = set(incomings["gh"])
found_cycles = {}

counter = 0
while True:
    counter += 1

    if len(found_cycles) == len(watched_nodes):
        break

    pulses = [("broadcaster", "button", LOW_PULSE)]
    idx = 0
    while idx < len(pulses):
        dst, src, pulse = pulses[idx]
        idx += 1

        if pulse == HIGH_PULSE and src in watched_nodes:
            found_cycles.setdefault(src, counter)

        if dst in flip_flops:
            state = flip_flops[dst]
            if pulse == HIGH_PULSE:
                continue
            else:
                pulses.extend(
                    (out, dst, LOW_PULSE if state else HIGH_PULSE)
                    for out in outgoings.get(dst, [])
                )
                flip_flops[dst] = not state
        elif dst in conjunctions:
            ins = conjunctions[dst]
            ins[src] = pulse
            new_pulse = (
                LOW_PULSE
                if all(value == HIGH_PULSE for value in ins.values())
                else HIGH_PULSE
            )
            pulses.extend((out, dst, new_pulse) for out in outgoings.get(dst, []))
        else:
            pulses.extend((out, dst, pulse) for out in outgoings.get(dst, []))

print(math.lcm(*found_cycles.values()))
