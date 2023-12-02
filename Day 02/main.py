"""
https://adventofcode.com/2023/day/2
"""

import functools

LIMIT_CUBES = {"r": 12, "g": 13, "b": 14}
sum_possible = 0
sum_powers = 0
with open("input.txt", mode="r") as file:
    for line in file.readlines():
        line = line.strip()[5:].replace("blue", "b").replace("red", "r").replace("green", "g")
        game, draws = line.split(": ")
        max_cubes = {"r": 0, "g": 0, "b": 0}
        for cube in draws.replace(";", ",").split(", "):
            count = int(cube[:-2])
            color = cube[-1]
            if count > LIMIT_CUBES[color]:
                game = 0
            if count > max_cubes[color]:
                max_cubes[color] = count
        sum_possible += int(game)
        sum_powers += functools.reduce(lambda x, y: x * y, max_cubes.values())
print("Sum of possible game IDs:", sum_possible)
print("Sum of set powers:", sum_powers)
