from collections import deque

with open("input.txt", "r") as f:
    data = f.read().splitlines()

data = [list(line) for line in data]

rows, cols = len(data), len(data[0])

def bfs(start_x, start_y):
    s = (start_x, start_y)
    visited = set()
    queue = deque([s])
    visited.add((start_x, start_y))

    path = []

    while queue:
        cx, cy = queue.popleft()

        path.append((cx, cy))
        if data[cy][cx] == "E":
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and data[ny][nx] != "#" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return path

def find_start():
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == "S":
                return (j, i)
    return ()

def get_shortcut(cx, cy):
    shortcuts = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < rows and 0 <= ny < cols and data[ny][nx] != ".":
            nnx, nny = nx + dx, ny + dy
            if 0 <= nnx < rows and 0 <= nny < cols and data[nny][nnx] != "#":
                    shortcuts.append((nnx, nny))
    return shortcuts

def main():
    sx, sy = find_start()
    path = bfs(sx, sy)

    counter = 0
    for cx, cy in path:
        shortcuts = get_shortcut(cx, cy)
        for shortcut in shortcuts:
            a = path.index(shortcut)
            b = path.index((cx, cy))
            if (a - b - 2) >= 100:
                counter += 1
    print(counter)

main()
