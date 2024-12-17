import heapq

with open("input.txt", "r") as f:
    GRID = f.read().splitlines()

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ROWS, COLS = len(GRID), len(GRID[0])

Pd = tuple[int, int, int]  # Point Direction
P = tuple[int, int]  # Point

def point_add(p1: P, p2: P) -> P:
    return (p1[0] + p2[0], p1[1] + p2[1])

def look_left_right(current_point: Pd) -> tuple[P, P]:
    x, y, di = current_point
    li = (di - 1) % len(DIRECTIONS)
    ri = (di + 1) % len(DIRECTIONS)
    return (*point_add((x, y), DIRECTIONS[li]), li), (*point_add((x, y), DIRECTIONS[ri]), ri)

def dijkstra(start_x: int, start_y: int, direction: int, tartget: str):
    visited = [[False] * COLS for _ in range(ROWS)]
    priority_queue: tuple[int, Pd] = []
    heapq.heappush(priority_queue, (0, (start_x, start_y, direction)))
    visited[start_y][start_x] = True

    def is_valid(p: P):
        return 0 <= p[0] < COLS and 0 <= p[1] < ROWS and GRID[p[1]][p[0]] != "#" and not visited[p[1]][p[0]]

    while priority_queue:
        score, cp = heapq.heappop(priority_queue)

        if GRID[cp[1]][cp[0]] == tartget:
            return score

        node_in_front = (*point_add((cp[0], cp[1]), DIRECTIONS[cp[2]]), cp[2])
        node_in_left, node_in_right = look_left_right(cp)

        if is_valid(node_in_front):
            heapq.heappush(priority_queue, (score + 1, node_in_front))
            visited[node_in_front[1]][node_in_front[0]] = True
        if is_valid(node_in_left):
            heapq.heappush(priority_queue, (score + 1001, node_in_left))
            visited[node_in_left[1]][node_in_left[0]] = True
        if is_valid(node_in_right):
            heapq.heappush(priority_queue, (score + 1001, node_in_right))
            visited[node_in_right[1]][node_in_right[0]] = True

def find_start() -> P:
    for i in range(ROWS):
        for j in range(COLS):
            if GRID[i][j] == "S":
                return j, i

def main():
    sx, sy = find_start()
    score = dijkstra(sx, sy, 2, "E")
    print(score)

if __name__ == "__main__":
    main()
