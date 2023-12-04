"""
https://adventofcode.com/2023/day/4
"""
from collections import defaultdict

points = 0
cards = defaultdict(lambda: 0)
with open("input.txt") as file:
    for i, line in enumerate(file.read().splitlines()):
        wins, picks = [set(num for num in l.split(" ") if len(num) > 0) for l in line[line.index(":") + 1:].split("|")]
        hits = len(wins.intersection(picks))
        if hits > 0:
            points += 2 ** (hits - 1)
        cards[i + 1] += 1
        for j in range(i + 2, i + 2 + hits):
            cards[j] += cards[i + 1]
print("Points:", points)
print("Cards:", sum(cards.values()))
