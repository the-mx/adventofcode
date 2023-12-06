# https://adventofcode.com/2023/day/7# https://adventofcode.com/2023/day/7

with open("input-7.txt", "r") as f:
    lines = f.read()

replacements = {"A": "Z", "K": "Y", "Q": "X", "T": "V", "J": "0"}
lines.translate(str.maketrans(replacements))

lines = lines.split("\n")

HAND_MAP = {
    (5, 1): 1,  # High card
    (4, 2): 2,  # One pair
    (3, 2): 3,  # Two pairs
    (3, 3): 4,  # Three of a kind
    (2, 3): 5,  # Full house
    (2, 4): 6,  # Four of a kind
    (1, 5): 7,  # Five of a kind
}


def find_type(s: str) -> int:
    if s == "00000":
        return 7

    without_jokers = hand.replace("0", "")
    jokers = len(s) - len(without_jokers)

    counts = {card: without_jokers.count(card) for card in set(without_jokers)}
    best_card = max(counts, key=lambda c: (counts[c], c), default="0")
    counts[best_card] += jokers

    return HAND_MAP[(len(counts), max(counts.values()))]


hands = []
for line in lines:
    hand, bid = line.split(" ")
    hands.append((find_type(hand), hand, int(bid)))

hands.sort()

total = sum(idx * bid for idx, (_, _, bid) in enumerate(hands, start=1))
print(total)
