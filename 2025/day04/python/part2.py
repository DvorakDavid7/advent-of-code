
directios = [(1, 0), (0, 1), (-1, 0),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def remove(grid: list[list[str]]):
    rows, cols = len(grid), len(grid[0])
    to_remove = []
    for gy in range(len(grid)):
        for gx in range(len(grid[gy])):
            if grid[gy][gx] != "@":
                continue
            counter = 0
            for d in directios:
                x, y = gx + d[0], gy + d[1]
                if not (0 <= x < cols and 0 <= y < rows):
                    continue
                if grid[y][x] == "@":
                    counter += 1
            if counter < 4:
                to_remove.append((gx, gy))
    for r in to_remove:
        grid[r[1]][r[0]] = "."
    return grid, len(to_remove)

def main():
    with open("day04/python/input.txt", "r") as f:
        lines = f.read().splitlines()

    grid = [list(line) for line in lines]
    result = 0
    while True:
        grid, removed = remove(grid)
        if removed == 0:
            break
        result += removed

    print(result)

main()
