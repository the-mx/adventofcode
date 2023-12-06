# https://adventofcode.com/2023/day/2
import re

with open("input-2.txt", "r") as f:
    lines = f.read()

games = []
for line in lines.split("\n"):
    game = {
        "blue": 1,
        "red": 1,
        "green": 1,
    }
    for value, color in re.findall(r"(\d+) (\w+)", line.split(":", 1)[1]):
        game[color] = max(game[color], int(value))
    games.append(game)

total = sum(game["red"] * game["blue"] * game["green"] for game in games)
print(total)
