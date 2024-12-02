def str_replace(s: str, new_char: str, index: int) -> str:
    return s[:index] + new_char + s[index + 1:]


def move_north(grid: list[str]) -> list[str]:
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":

                dest = 0
                k = i - 1
                while k >= 0 and grid[k][j] == ".":
                    dest += 1
                    k -= 1

                grid[i] = str_replace(grid[i], ".", j)
                grid[i - dest] = str_replace(grid[i - dest], "O", j)
    # print("\n".join(grid))
    return grid

def count_score(grid: list[str]) -> int:
    score = 0
    row_score = len(grid)
    for line in grid:
        for ch in line:
            if ch == "O":
                score += row_score
        row_score -= 1
    return score

def main():
    with open("input.txt") as f:
        data = f.read()
    
    for i in range(1000000000):
        moved_grid = move_north(data.split())
    score = count_score(moved_grid)
    print(score)

if __name__ == "__main__":
    main()
