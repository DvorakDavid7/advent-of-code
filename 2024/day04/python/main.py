
def part1():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows, cols = len(grid), len(grid[0])

    def search(word: str, index: int, x: int, y: int, dx: int, dy: int) -> int:
        if index == len(word) - 1:
            return 1

        if (x < 0 or x >= cols) or (y < 0 or y >= rows) or word[index] != grid[x][y]:
            return 0

        return search(word, index + 1, x + dx, y + dy, dx ,dy)

    result = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                result += search("XMASS", 0, j, i, dx, dy)

    print(result)


def part2():
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    rows, cols = len(grid), len(grid[0])

    counter = 0
    for i in range(rows):
        if i == 0 or i == rows - 1:
            continue
        for j in range(cols):
            if j == 0 or j == cols - 1:
                continue
            
            if grid[i][j] == "A":
                w = grid[i+1][j+1] + grid[i-1][j-1]
                v = grid[i-1][j+1] + grid[i+1][j-1]

                if (w == "SM" or w == "MS") and (v == "SM" or v == "MS"):
                    counter += 1
    print(counter)


if __name__ == "__main__":
    part1()
    part2()
