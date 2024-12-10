
with open("input.txt", "r") as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(list(grid[0]))

def rec(x, y, start):
    if not (0 <= x < cols and 0 <= y < rows):
        return 0
    
    current = int(grid[y][x])

    if current == 9 and current == start + 1:
        return 1
    
    if current == start + 1:
        return solve(x, y, current)
    else:
        return 0

def solve(x, y, start):
    return rec(x+1, y, start) + rec(x-1, y, start) + rec(x, y-1, start) + rec(x, y+1, start)

result = 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "0":
            result += solve(x, y, 0)

print(result)
