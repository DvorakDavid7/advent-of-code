
def is_empty_col(grid: list[str], col_idx: int) -> bool:
    for line in grid:
        if line[col_idx] != ".":
            return False
    return True

def is_empty_row(grid: list[str], row_idx: int) -> bool:
    row = grid[row_idx]
    return row == "." * len(row)

def expand_grid(grid: list[str]) -> tuple[set]:
    empty_cols = set()
    empty_rows = set()
    for i, line in enumerate(grid):
        for j, value in enumerate(line):
            if is_empty_col(grid, i):
                empty_cols.add(i)
            if is_empty_row(grid, j):
                empty_rows.add(j)
    return (empty_cols, empty_rows)

def get_galaxy_coords(grid: list[str]) -> list[tuple]:
    result = []
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "#":
                result.append((j, i))
    return result

def get_distance(a: tuple[int], b: tuple[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_distance_with_expansions(a: tuple[int], b: tuple[int], C: set[int], R: set[int], alpha = 1) -> int:
    t = abs(a[0] - b[0]) + len([i for i in C if min(a[0], b[0]) < i < max(a[0], b[0])]) * alpha
    u = abs(a[1] - b[1]) + len([i for i in R if min(a[1], b[1]) < i < max(a[1], b[1])]) * alpha
    return t + u 

def main():
    grid = open("./input.txt").read().splitlines()
    C, R = expand_grid(grid)
    galaxies = get_galaxy_coords(grid)
    pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    res1 = [get_distance_with_expansions(x[0], x[1], C, R) for x in pairs]
    res2 = [get_distance_with_expansions(x[0], x[1], C, R, 1_000_000 - 1) for x in pairs]
    print(sum(res1))
    print(sum(res2))


if __name__ == "__main__":
    main()
