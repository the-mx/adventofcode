# https://adventofcode.com/2023/day/25
import random

with open("input-25.txt", "r") as f:
    lines = f.read()

original = {}
for line in lines.split("\n"):
    node, connected = line.split(":")
    for c in [s.strip() for s in connected.strip().split(" ")]:
        original.setdefault(node, []).append(c)
        original.setdefault(c, []).append(node)

while True:
    edges = original.copy()

    while len(edges) > 2:  # Karger rules!
        u = random.choice(list(edges.keys()))
        v = random.choice(list(edges[u]))

        edges[u + v] = [c for c in edges[u] if c != v] + [c for c in edges[v] if c != u]

        for c in set(edges[u + v]):
            edges[c] = [x if x not in (u, v) else u + v for x in edges[c]]

        del edges[u]
        del edges[v]

    if len(edges[list(edges.keys())[0]]) <= 3:
        subgraphs = [len(k) / 3 for k in edges.keys()]  # Since all node names are 3-symbol length
        print(subgraphs[0] * subgraphs[1])
        break
