


def solve(grid: list[str], start_x: int, start_y: int):
    rotations = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    rot_counter = 0

    rows, cols = len(grid), len(grid[0])
    x, y = start_x, start_y
    visited: set[tuple[int, int]] = set()
    while True:
        dx, dy = rotations[rot_counter]
        visited.add((x, y))

        if (x + dx >= cols or x + dx < 0) or (y + dy >= rows or y + dy < 0):
            break

        if grid[y + dy][x + dx] == "#":
            rot_counter = (rot_counter + 1) % len(rotations)
            dx, dy = rotations[rot_counter]

        x += dx
        y += dy

    print(len(visited))


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

if __name__ == "__main__":
    main()
