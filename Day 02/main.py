"""
https://adventofcode.com/2023/day/2
"""

import functools

LIMIT_CUBES = {"red": 12, "green": 13, "blue": 14}
sum_possible = 0
sum_powers = 0
with open("input.txt", mode="r") as file:
    for line in file.read().splitlines():
        game, draws = line[5:].split(": ")
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for draw in draws.split("; "):
            for cube in draw.split(", "):
                count, color = cube.split(" ")
                count = int(count)
                if count > LIMIT_CUBES[color]:
                    game = 0
                if count > max_cubes[color]:
                    max_cubes[color] = count
        sum_possible += int(game)
        sum_powers += functools.reduce(lambda x, y: x * y, max_cubes.values())
print("Sum of possible game IDs:", sum_possible)
print("Sum of set powers:", sum_powers)
