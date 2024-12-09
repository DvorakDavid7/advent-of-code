import turtle 

with open("test.txt") as f:
    grid = f.read().splitlines()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# guard starting location
gx, gy = 0, 0

# guard starting direction
gd = 0

size = 30
speed = 1

rows, cols = len(grid), len(grid[0])

for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "^":
            gx, gy = x, y

turtle.speed(speed)
turtle.shape("turtle")
turtle.penup()
turtle.goto(gx, gy)
turtle.setheading(90)
turtle.pendown()

visited = set()
while True:
    visited.add((gx, gy))

    x, y = gx + directions[gd][0], gy + directions[gd][1]

    if not (0 <= x < cols and 0 <= y < rows):
        break  # out of bouds

    if grid[y][x] == "#":
        gd = (gd + 1) % len(directions)
        turtle.right(90)
    else:
        gx, gy = x, y
        turtle.forward(size)
    
print(len(visited))
input()
