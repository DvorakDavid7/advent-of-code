from functools import cache

grid = []

@cache
def dfs_recursive(node: tuple[int, int]):
    x, y = node

    if y == len(grid) - 1:
        return 1

    if grid[y + 1][x] == "^":
        return dfs_recursive((x - 1, y + 1)) + dfs_recursive((x + 1, y + 1))
    
    return dfs_recursive((x, y + 1))

def main():
    global grid
    with open("day07/python/input.txt", "r") as f:
        data = f.read().splitlines()
    grid = [list(line) for line in data]

    s = grid[0].index("S")

    result = dfs_recursive((s, 1))

    print(result)
    
main()
