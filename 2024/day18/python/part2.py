
from collections import deque

cols, rows = 71, 71

grid = [["."] * cols for _ in range(rows)]

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def print_grid():
    for line in grid:
        print("".join(line))

def bfs(grid: list[list[str]]):
    s = (0, 0, 0)
    visited = [[False] * cols for _ in range(rows)]

    queue = deque([s])

    visited[0][0] = True

    while queue:
        cx, cy, steps = queue.popleft()

        if (cx, cy) == (cols - 1, rows - 1):
            return steps

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            if not visited[nx][ny] and grid[ny][nx] == ".":
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    return -1

def main():
    for i in range(1024, len(data)):
        for byte in data[:i]:
            x, y  = tuple(map(int, byte.split(",")))
            grid[y][x] = "#"
        if bfs(grid) == -1:
            print(f"{x},{y}")
            return

main()
