from collections import deque

cols, rows = 71, 71
number_of_falling_bytes = 1024

grid = [["."] * cols for _ in range(rows)]

with open("input.txt", "r") as f:
    data = f.read().splitlines()[:number_of_falling_bytes]

def print_grid():
    for line in grid:
        print("".join(line))

def bfs():
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
    for byte in data:
        x, y  = tuple(map(int, byte.split(",")))
        grid[y][x] = "#"
    steps = bfs()
    print(steps)

main()
