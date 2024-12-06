
rotations = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def modify_grid(coords: tuple[int, int], char: str, grid: list[str]):
    x, y = coords
    grid_copy = grid.copy()
    row_as_list = list(grid_copy[y])
    row_as_list[x] = char
    grid_copy[y] = ''.join(row_as_list)
    return grid_copy


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


def is_circle(grid: list[str], start_pos: tuple[int, int, int]) -> bool:
    visited: set[tuple[int, int, int]] = set()

    pos = start_pos

    while True:
        if pos in visited:
            return True

        visited.add(pos)

        next_ch = get_next(grid, pos)
        if next_ch == None:
            return False

        if next_ch == "#":
            pos = rotate(pos)
        pos = move(pos)


def rotate(pos: tuple[int, int, int]) -> tuple[int, int, int]:
    dir = (pos[2] + 1) % len(rotations)
    return (pos[0], pos[1], dir)


def move(pos: tuple[int, int, int]) -> tuple[int, int, int]:
    dx, dy = rotations[pos[2]]
    return (pos[0] + dx, pos[1] + dy, pos[2])


def get_next(grid: list[str], pos: tuple[int, int, int]) -> str | None:
    rows, cols = len(grid), len(grid[0])
    dx, dy = rotations[pos[2]]
    x, y = pos[0], pos[1]
    if (x + dx >= cols or x + dx < 0) or (y + dy >= rows or y + dy < 0):
        return None
    return grid[y + dy][x + dx]


def solve2(grid: list[str], start_x: int, start_y: int):
    pos = (start_x, start_y, 0)

    visited_points: set[tuple[int, int]] = set()
    circle_count = 0

    while True:
        visited_points.add((pos[0], pos[1]))

        next_ch = get_next(grid, pos)

        if next_ch == None:
            break

        if next_ch == "#":
            pos = rotate(pos)

        i, j, _ = move(pos)
        if (i, j) != (start_x, start_y):
            map_cpy = modify_grid((i, j), "#", grid)
            if is_circle(map_cpy, rotate(pos)):
                circle_count += 1

        pos = move(pos)

    print(circle_count-3)
    return visited_points

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
    # solve(grid, start_x, start_y)
    visited = solve2(grid, start_x, start_y)
    print(len(visited))


if __name__ == "__main__":
    main()
