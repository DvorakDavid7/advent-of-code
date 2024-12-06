with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# guard starting location
gx, gy = 0, 0

# guard starting direction
gd = 0

rows, cols = len(grid), len(grid[0])

for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "^":
            gx, gy = x, y


def get_path(gx, gy, gd):
    visited = set()
    while True:
        visited.add((gx, gy))

        x, y = gx + directions[gd][0], gy + directions[gd][1]

        if not (0 <= x < cols and 0 <= y < rows):
            break  # out of bouds

        if grid[y][x] == "#":
            gd = (gd + 1) % len(directions)
        else:
            gx, gy = x, y

    return visited

    
def is_loop(grid, gx, gy, gd):
    visited = set()
    while True:
        if (gx, gy, gd) in visited:
            return True

        visited.add((gx, gy, gd))

        x, y = gx + directions[gd][0], gy + directions[gd][1]

        if not (0 <= x < cols and 0 <= y < rows):
            return False  # out of bouds

        if grid[y][x] == "#":
            gd = (gd + 1) % len(directions)
        else:
            gx, gy = x, y


cycle_counter = 0

visited = get_path(gx, gy, gd)
visited.remove((gx, gy))  # remove starting position

for x, y in visited:
    grid[y][x] = "#"
    if is_loop(grid, gx, gy, gd):
        cycle_counter += 1
    grid[y][x] = "."

print(cycle_counter)
