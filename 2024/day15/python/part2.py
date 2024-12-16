P = tuple[int, int]
DIRECTIONS = { "<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

def point_to_str(p: P) -> str:
    return f"({p[0]}, {p[1]})"

def point_add(p1: P, p2: P) -> P:
    return (p1[0] + p2[0], p1[1] + p2[1])

class Box:
    p1: P
    p2: P
    def __init__(self, p1: P, p2: P):
        if p1[0] < p2[0]:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1
    
    def has_point(self, p: P):
        return p == self.p1 or p == self.p2

    def move(self, direction: P):
        self.p1 = point_add(self.p1, direction)
        self.p2 = point_add(self.p2, direction)

class Grid:
    cols: int
    rows: int
    grid: list[list[str]]
    boxes: set[Box]

    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.boxes = set()

    def get_symbol(self, p: P) -> str:
        if not self.is_in_grid(p):
            raise ValueError(f"trying to get a point {point_to_str(p)} value that is out of grid range")
        return self.grid[p[1]][p[0]]

    def set_symbol(self, p: P, symbol: str):
        if not self.is_in_grid(p):
            raise ValueError(f"trying to set a point {point_to_str(p)} to a value {symbol} that is out of grid range")
        self.grid[p[1]][p[0]] = symbol
    
    def is_in_grid(self, p: P) -> bool:
        return 0 <= p[0] < self.cols and 0 <= p[1] < self.rows

    def swap(self, p1: P, p2: P):
        if not self.is_in_grid(p1) or not self.is_in_grid(p2):
            raise ValueError(f"trying to swat points {point_to_str(p1)} and {point_to_str(p2)} but one of them is out of range")
        tmp = self.get_symbol(p1)
        self.set_symbol(p1, self.get_symbol(p2))
        self.set_symbol(p2, tmp)

    def print(self):
        for line in self.grid:
            print("".join(line))
        print()

    def get_start_point(self) -> P:
        for sx in range(self.cols):
            for sy in range(self.rows):
                if self.get_symbol((sx, sy)) == "@":
                    return (sx, sy)
        raise ValueError("no starting point found")
    
    def get_box(self, p: P):
        for box in self.boxes:
            if box.has_point(p):
                return box
        return None

    def init_boxes(self):
        for y in range(self.rows):
            for x in range(self.cols - 1):
                if self.get_symbol((x, y)) == "[" and self.get_symbol((x + 1, y)) == "]":
                    self.boxes.add(Box((x, y), (x + 1, y)))

    def resize(self):
        resized_grid = [["." for _ in range(self.rows)] for _ in range(self.cols)]
        for y in range(self.cols):
            for x in range(self.rows):
                if self.get_symbol((x, y)) == "#":
                    resized_grid[y][x] = "##"
                elif self.get_symbol((x, y)) == "O":
                    resized_grid[y][x] = "[]"
                elif self.get_symbol((x, y)) == ".":
                    resized_grid[y][x] = ".."
                elif self.get_symbol((x, y)) == "@":
                    resized_grid[y][x] = "@."
        self.grid = [list(row) for row in ["".join(row) for row in resized_grid]]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def attached_boxes(self, p: P, direction: P) -> list[Box]:
        boxes = set()
        def rec(p: P):
            if not self.is_in_grid(p):
                return
            box = self.get_box(p)
            if box == None:
                return 
            if box not in boxes:
                boxes.add(box)
            next_box_1 = point_add(box.p1, direction)
            next_box_2 = point_add(box.p2, direction)
            if self.get_box(next_box_1) != box:
                rec(point_add(box.p1, direction))
            if self.get_box(next_box_2) != box:
                rec(point_add(box.p2, direction))
        rec(p)
        return list(boxes)

    def can_move_boxes(self, boxes: list[Box], direction: P) -> bool:
        for box in boxes:
            a = point_add(box.p1, direction)
            b = point_add(box.p2, direction)
            if self.get_symbol(a) == "#" or self.get_symbol(b) == "#":
                return False
        return True
    
    def erase_boxes(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.get_symbol((i, j)) == "]": self.set_symbol((i, j), ".")
                if self.get_symbol((i, j)) == "[": self.set_symbol((i, j), ".")
    
    def draw_boxes(self):
        for box in self.boxes:
            self.set_symbol(box.p1, "[")
            self.set_symbol(box.p2, "]")

    def move_boxes(self, boxes_to_move: list[Box], direction):
        self.erase_boxes()
        for box in boxes_to_move:
            self.boxes.remove(box)
            box.move(direction)
            self.boxes.add(box)
        self.draw_boxes()

def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    delim = data.index("")
    instructions = "".join(data[delim + 1:])
    grid_data = [list(row) for row in data[:delim]]
    grid = Grid(grid_data)
    grid.resize()
    grid.init_boxes()
    # grid.print()
    sx, sy = grid.get_start_point()

    current = (sx, sy)
    for instruction in instructions:
        direction = DIRECTIONS[instruction]
        next_point = point_add(current, direction)

        if grid.get_symbol(next_point) == ".":
            grid.swap(current, next_point)
            current = next_point
        else:
            box = grid.get_box(next_point)
            if box:
                boxes_to_move = grid.attached_boxes(next_point, direction)
                can_move = grid.can_move_boxes(boxes_to_move, direction)
                if can_move:
                    grid.move_boxes(boxes_to_move, direction)
                    grid.swap(current, next_point)
                    current = next_point
    # grid.print()
    print(sum(100 * box.p1[1] + box.p1[0] for box in grid.boxes))

if __name__ == "__main__":
    main()
