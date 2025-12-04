
directios = [(1, 0), (0, 1), (-1, 0),(0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def main():
    with open("day04/python/input.txt", "r") as f:
        grid = f.read().splitlines()

    rows, cols = len(grid), len(grid[0])
    result = 0
    for gy in range(len(grid)):
        for gx in range(len(grid[gy])):
            counter = 0
            if grid[gy][gx] != "@":
                continue
            for d in directios:
                x, y = gx + d[0], gy + d[1]
                if not (0 <= x < cols and 0 <= y < rows):
                    continue
                if grid[y][x] == "@":
                    counter += 1
            if counter < 4:
                result += 1
    print(result)

main()
