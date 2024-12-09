
from itertools import product

with open("input.txt", "r") as f:
    grid = [list(l) for l in f.read().splitlines()]

antenas: dict[str, set[tuple[int, int]]] = {}
rows, cols = len(grid), len(grid[0])

for y in range(rows):
    for x in range(cols):
        s = grid[y][x]
        if s != ".":
            if s not in antenas:
                antenas[s] = set()
            antenas[s].add((x, y))

antinodes = set()
def place_antinodes(points: list[tuple[int, int]]):
    if len(points) < 2:
        return 0
    pairs = product(points, points)
    for p1, p2 in pairs:
        if p1 == p2:
            continue
        antinodes.add(p2)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        a = (p2[0] + dx, p2[1] + dy)
        while 0 <= a[0] < rows and 0 <= a[1] < cols:
            antinodes.add(a)
            a = (a[0] + dx, a[1] + dy)

for a in antenas:
    place_antinodes(antenas[a])

print(len(antinodes))
