from collections import deque
from collections import defaultdict

with open("input.txt", "r") as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(grid[0])
visited = [[False] * cols for _ in range(rows)]
fences = defaultdict(int)
areas = defaultdict(list)

def bfs(x, y, plot):
    queue = deque([(x, y)])
    area = []
    visited[x][y] = True

    fences[(x, y)] = 0

    while queue:
        cx, cy = queue.popleft()
        area.append((cx, cy))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != plot:
                fences[(cx, cy)] += 1

            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == plot:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area

for i in range(rows):
    for j in range(cols):
        plot = grid[i][j]
        if not visited[i][j]:
            areas[plot].append(bfs(i, j, plot))

result = 0
for plot, areas in areas.items():
    for area in areas:
        result += len(area) * sum([fences[a] for a in area])

print(result)