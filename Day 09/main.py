with open("input.txt") as file:
    sequences = [[int(num) for num in line.split(" ")] for line in file.read().splitlines()]

p1 = 0
p2 = 0
for sequence in sequences:
    depth = 0
    while any(sequence):
        p1 += sequence[-1]
        p2 += (-1) ** depth * sequence[0]
        sequence = [q - p for p, q in zip(sequence[:-1], sequence[1:])]
        depth += 1
print("Last values:", p1)
print("First values:", p2)
