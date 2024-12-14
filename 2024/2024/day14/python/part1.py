file_name = "input.txt"
with open(file_name, "r") as f:
    data = f.read().splitlines()

if file_name == "test.txt":
    cols, rows = 11, 7
else:
    cols, rows = 101, 103

def count_points_in_quadrants(points, cols, rows):
    c_x = int((cols) // 2)
    c_y = int((rows) // 2)
    quadrant_counts = { 1: 0, 2: 0, 3: 0, 4: 0 }
    for x, y in points:
        if x == c_x or y == c_y:
            continue
        if x < c_x and y < c_y:
            quadrant_counts[1] += 1
        elif x > c_x and y < c_y:
            quadrant_counts[2] += 1
        elif x < c_x and y > c_y:
            quadrant_counts[3] += 1
        elif x > c_x and y > c_y:
            quadrant_counts[4] += 1
    return quadrant_counts

robots = []
seconds = 100
result = 1

for line in data:
    p = line.split(" ")[0][2:].split(",")
    v = line.split(" ")[1][2:].split(",")
    x1 = (int(p[0]) + int(v[0]) * seconds) % cols
    x2 = (int(p[1]) + int(v[1]) * seconds) % rows
    robots.append((x1, x2))

quadrants = count_points_in_quadrants(robots, cols, rows)
for k, v in quadrants.items():
    result *= v
print(result)
