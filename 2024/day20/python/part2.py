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

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)

def main():
    sx, sy = find_start()
    path = bfs(sx, sy)

    counter = 0
    for point in path:
        cuts = {p for p in path if 0 < distance(point, p) <= 20}
        for cut in cuts:
            d1 = path.index(cut)
            d2 = path.index(point)
            if d1 - d2 - distance(cut, point) >= 100:
                counter += 1
    print(counter)

main()
