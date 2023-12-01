"""
Task: https://adventofcode.com/2023/day/1
"""
import re

RE_PART_ONE = r"[0-9]"
RE_PART_TWO = r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"
WORD_TO_NUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7", "eight": "8", "nine": "9"}

calibration = 0
with open("input.txt") as file:
    for line in file.readlines():
        digits = [WORD_TO_NUM.get(d, d) for d in re.findall(RE_PART_TWO, line)]
        value = int(digits[0] + digits[-1])
        calibration += value
print("Sum of calibration values:", calibration)
