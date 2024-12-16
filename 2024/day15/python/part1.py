
with open("input.txt", "r") as f:
    data = f.read().splitlines()

delim = data.index("")
grid = [list(row) for row in data[:delim]]
rows, cols = len(grid), len(grid[0])
instructions = "".join(data[delim + 1:])
directions = { "<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

for sx in range(cols):
    for sy in range(rows):
        if grid[sy][sx] == "@":
            break
    else:
        continue
    break

def print_grid():
    for line in grid:
        print("".join(line))

def swap(p1: tuple[int, int], p2: tuple[int, int]):
    tmp = grid[p1[1]][p1[0]]
    grid[p1[1]][p1[0]] = grid[p2[1]][p2[0]]
    grid[p2[1]][p2[0]] = tmp


def move_points(points: list[tuple[int, int]], direction: tuple[int, int]):
    for point in reversed(points):
        swap(point, (point[0] + direction[0], point[1] + direction[1]))

cx, cy = sx, sy
for instruction in instructions:
    d = directions[instruction]
    nx, ny = cx + d[0], cy + d[1]
    if grid[ny][nx] == ".":
        swap((cx, cy), (nx, ny))
        cx, cy = nx, ny
    elif grid[ny][nx] == "O":
        points_to_move = []
        possible_nx, possible_ny = nx, ny
        while grid[ny][nx] == "O":
            points_to_move.append((nx, ny))
            nx, ny = nx + d[0], ny + d[1]
        if grid[ny][nx] == ".":
            move_points(points_to_move, d)
            swap((cx, cy), (possible_nx, possible_ny))
            cx, cy = possible_nx, possible_ny
print_grid()

boxes = set()
for x in range(cols):
    for y in range(rows):
        if grid[y][x] == "O":
            boxes.add((x, y))

print(sum([100 * box[1] + box[0] for box in boxes]))
