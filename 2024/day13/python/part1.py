import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def parse_line(line):
    x, y = line.split(",")
    return int("".join(re.findall(r"\d+", x))), int("".join(re.findall(r"\d+", y)))

def solve(a, b, c, d, u, v) -> tuple[int, int]:
    if a == 0 or (a*d - c*b == 0):
        raise ValueError("possible division by zero")
    y = (a*v - c*u) / (a*d - c*b)
    x = (u - b*y) / a
    if not x.is_integer() or not y.is_integer():
        raise ValueError("not an integer solution")
    return int(x), int(y)

result = 0
while data:
    buff = data[:3]
    data = data[4:]
    ax, ay = parse_line(buff[0])
    bx, by = parse_line(buff[1])
    px, py = parse_line(buff[2])
    try:
        a, b = solve(ax, bx, ay, by, px, py)
        result += a * 3 + b * 1
    except:
        pass

print(result)
