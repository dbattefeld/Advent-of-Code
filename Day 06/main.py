"""
https://adventofcode.com/2023/day/6
"""

with open("input.txt", mode="r") as file:
    content = file.read().splitlines()
times = [int(s) for s in content[0][6:].split(" ") if len(s) > 0]
records = [int(s) for s in content[1][9:].split(" ") if len(s) > 0]
p1 = 1
for i in range(len(times)):
    counter = 0
    for speed in range(times[i]):
        distance = (times[i] - speed) * speed
        if distance > records[i]:
            counter += 1
    p1 *= counter
print("Part 1:", p1)

with open("input.txt", mode="r") as file:
    content = file.read().splitlines()
time = int("".join([s for s in content[0][6:].split(" ") if len(s) > 0]))
record = int("".join([s for s in content[1][9:].split(" ") if len(s) > 0]))
p2 = 0
for speed in range(time):
    distance = (time - speed) * speed
    if distance > record:
        p2 += 1
print("Part 2:", p2)
