
rotations = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solve(grid: list[str], start_x: int, start_y: int):
    rot_counter = 0
    rows, cols = len(grid), len(grid[0])
    x, y = start_x, start_y
    path: set[tuple[int, int]] = set()
    while True:
        dx, dy = rotations[rot_counter]
        path.add((x, y))

        if (x + dx >= cols or x + dx < 0) or (y + dy >= rows or y + dy < 0):
            break

        if grid[y + dy][x + dx] == "#":
            rot_counter = (rot_counter + 1) % len(rotations)
            dx, dy = rotations[rot_counter]

        x += dx
        y += dy

    print(len(path))


def is_circle(grid: list[str], start_x: int, start_y: int, rot_counter: int):
    rows, cols = len(grid), len(grid[0])
    x, y = start_x, start_y

    visited: set[tuple[int, int, int]] = set()

    while True:
        dx, dy = rotations[rot_counter]

        if (x, y) == (start_x, start_y) and len(visited) > 0:
            return True

        if (x, y, rot_counter) in visited:
            return False

        if (x + dx >= cols or x + dx < 0) or (y + dy >= rows or y + dy < 0):
            return False

        if grid[y + dy][x + dx] == "#":
            rot_counter = (rot_counter + 1) % len(rotations)
            dx, dy = rotations[rot_counter]

        visited.add((x, y, rot_counter))
        x += dx
        y += dy


def solve2(grid: list[str], start_x: int, start_y: int):
    rot_counter = 0
    rows, cols = len(grid), len(grid[0])
    x, y = start_x, start_y

    circle_counter = 0

    while True:
        dx, dy = rotations[rot_counter]
        if (x + dx >= cols or x + dx < 0) or (y + dy >= rows or y + dy < 0):
            break

        if grid[y + dy][x + dx] == "#":
            rot_counter = (rot_counter + 1) % len(rotations)
            dx, dy = rotations[rot_counter]

        if is_circle(grid, x, y, (rot_counter + 1) % len(rotations)):
            circle_counter += 1

        x += dx
        y += dy
    print(circle_counter)


def main():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    rows, cols = len(grid), len(grid[0])

    start_x = 0
    start_y = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "^":
                start_x = x
                start_y = y
                break

    solve(grid, start_x, start_y)
    solve2(grid, start_x, start_y)


if __name__ == "__main__":
    main()
