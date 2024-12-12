from collections import deque
from collections import defaultdict

with open("input.txt", "r") as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(grid[0])
visited = [[False] * cols for _ in range(rows)]
fences = defaultdict(int)
areas = defaultdict(list)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y, plot):
    queue = deque([(x, y)])
    area = []
    visited[x][y] = True
    fences = 0
    sides = 0

    def is_in_area(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == plot

    def count_corners(x, y):
        result = 0
        for i in range(len(directions)):
            d1 = directions[i]
            d2 = directions[(i + 1) % len(directions)]
            d = d1[0] + d2[0], d1[1] + d2[1]

            # convex angle
            if not is_in_area(x + d1[0], y + d1[1]) and not is_in_area(x + d2[0], y + d2[1]):
                result += 1  

            # this is a concave angle
            if not is_in_area(x + d[0], y + d[1]) and is_in_area(x + d1[0], y + d1[1]) and is_in_area(x + d2[0], y + d2[1]):
                result += 1 

        return result

    while queue:
        cx, cy = queue.popleft()
        area.append((cx, cy))

        sides += count_corners(cx, cy)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if not is_in_area(nx, ny):
                fences += 1

            if is_in_area(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return area, fences, sides

result = 0
for i in range(rows):
    for j in range(cols):
        plot = grid[i][j]
        if not visited[i][j]:
            area, fences, sides = bfs(i, j, plot)
            result += len(area) * sides

print(result)
