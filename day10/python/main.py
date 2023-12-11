
def polygonArea(vertices: list[tuple[int]]):
    x, y = zip(*vertices)
    return 0.5 * abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(vertices))))

def pick_theorem(area: float, loop_size: int) -> int:
    return int(area - 0.5 * loop_size + 1)

def get_char(grid: list[str], x: int, y: int) -> str:
    return grid[y][x]

def get_starting_point(grid: list[str]) -> tuple[int]:
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "S":
                return (j, i)
    return (0, 0)

def get_poits_connected_to_start(grid: list[str], start_coords: tuple[int]) -> list[tuple[int]]:
    result = []
    # left
    if start_coords[0] - 1 >= 0:
        char = get_char(grid, start_coords[0] - 1, start_coords[1])
        if char in "LF-":
            result.append((start_coords[0] - 1, start_coords[1]))

    # right
    if start_coords[0] + 1 < len(grid[0]):
        char = get_char(grid, start_coords[0] + 1, start_coords[1])
        if char in "J7-":
            result.append((start_coords[0] + 1, start_coords[1]))
    
    # top
    if start_coords[1] - 1 >= 0:
        char = get_char(grid, start_coords[0], start_coords[1] - 1)
        if char in "|7F":
            result.append((start_coords[0], start_coords[1] - 1))

    # bottom
    if start_coords[1] + 1 < len(grid):
        char = get_char(grid, start_coords[0], start_coords[1] + 1)
        if char in "|JL":
            result.append((start_coords[0], start_coords[1] + 1))
    return result

def get_connected_points(grid: list[str], coord: tuple[int]) -> list[tuple[int]]:
    symbol = get_char(grid, coord[0], coord[1])
    
    if symbol == "|":
        return [(coord[0], coord[1] + 1), (coord[0], coord[1] - 1)]
    if symbol == "-":
        return [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])]

    if symbol == "L":
        return [(coord[0], coord[1] - 1), (coord[0] + 1, coord[1])]
    if symbol == "J":
        return [(coord[0], coord[1] - 1), (coord[0] - 1, coord[1])]

    if symbol == "7":
        return [(coord[0] - 1, coord[1]), (coord[0], coord[1] + 1)]
    if symbol == "F":
        return [(coord[0] + 1, coord[1]), (coord[0], coord[1] + 1)]

    return []

def get_next(grid, current: tuple[int], visited: set[tuple[int]]) -> tuple[int]:
    connected_points = get_connected_points(grid, current)
    return connected_points[0] if connected_points[0] not in visited else connected_points[1]

def main():
    grid = open("./input.txt").read().splitlines()
    start = get_starting_point(grid)

    starting_points = get_poits_connected_to_start(grid, start)

    visited = list()
    visited.append(start)
    visited.append(starting_points[0])

    next = starting_points[0]
    while next != starting_points[1]:
        next = get_next(grid, next, visited)
        visited.append(next)
    
    visited.append(starting_points[1])

    print(len(visited) // 2)

    area = polygonArea(visited)
    print(pick_theorem(area, len(set(visited))))


if __name__ == "__main__":
    main()
