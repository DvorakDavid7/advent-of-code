file_name = "input.txt"
with open(file_name, "r") as f:
    data = f.read().splitlines()

if file_name == "test.txt":
    cols, rows = 11, 7
else:
    cols, rows = 101, 103

def move_robots(seconds):
    robots = []
    for line in data:
        p = line.split(" ")[0][2:].split(",")
        v = line.split(" ")[1][2:].split(",")
        x1 = (int(p[0]) + int(v[0]) * seconds) % cols
        x2 = (int(p[1]) + int(v[1]) * seconds) % rows
        robots.append((x1, x2))
    return robots

def display_robots(robots):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    for r in robots:
        grid[r[1]][r[0]] = "#"
    for line in grid:
        print("".join(line))

for i in range(10000):
    robots = move_robots(i)
    if len(data) == len(set(robots)):
        display_robots(robots)
        print("second:", i)
        break
