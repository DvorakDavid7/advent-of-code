
with open("input.txt", "r") as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(list(grid[0]))

def rec(x, y, start, visited):
    if not (0 <= x < cols and 0 <= y < rows):
        return 0
    
    current = int(grid[y][x])

    if current == 9 and current == start + 1 and (x, y) not in visited:
        visited.add((x, y))
        return 1
    
    if current == start + 1:
        return solve(x, y, current, visited)
    else:
        return 0

def solve(x, y, start, visited):
    return rec(x+1, y, start, visited) + \
        rec(x-1, y, start, visited) + \
        rec(x, y-1, start, visited) + \
        rec(x, y+1, start, visited)

result = 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "0":
            result += solve(x, y, 0, set())

print(result)
