CONNECTIONS = {
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "|": {(-1, 0): (-1, 0), (1, 0): (1, 0)},
    "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
    "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
    "7": {(-1, 0): (0, -1), (0, 1): (1, 0)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
    ".": {}
}

with open("input.txt") as file:
    pipes = file.read().splitlines()

# find start
location = None
for i in range(len(pipes)):
    for j in range(len(pipes[0])):
        if pipes[i][j] == "S":
            location = (i, j)
            break

# derive first two connecting pipes
steps = []
for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
    pipe = pipes[location[0] + direction[0]][location[1] + direction[1]]
    if direction in CONNECTIONS[pipe]:
        steps.append((location, direction))

# descend from start in two pipes simultaneously
counter = 0
while True:
    for i in [0, 1]:
        location, direction = steps.pop(i)
        location = (location[0] + direction[0], location[1] + direction[1])
        direction = CONNECTIONS[pipes[location[0]][location[1]]][direction]
        steps.append((location, direction))
    counter += 1
    if steps[0][0] == steps[1][0]:
        print("Meeting at", steps[0][0], "after", counter, "steps")
        break
