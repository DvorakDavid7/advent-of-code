
def print_grid(grid: list[list[str]]):
    print("\n".join("".join(x) for x in grid))

def main():
    with open("day07/python/input.txt", "r") as f:
        data = f.read().splitlines()
    grid = [list(line) for line in data]
    s = grid[0].index("S")
    grid[1][s] = "|"

    result = 0
    for i in range(2, len(grid)):
        beans = [i for i, ch in enumerate(grid[i - 1]) if ch == "|"]
        for bean in beans:
            if grid[i][bean] == "^":
                if bean + 1 < len(grid[i]): 
                    grid[i][bean + 1] = "|"
                if bean - 1 >= 0:
                    grid[i][bean - 1] = "|"
                result += 1
            else:
                grid[i][bean] = "|"

    print_grid(grid)
    print(result)
    
main()
