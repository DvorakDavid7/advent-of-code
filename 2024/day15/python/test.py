from part2 import Box, Grid

rows, cols = 10, 10

def test_case1():
    grid_data = [["." for _ in range(cols)] for _ in range(rows)]
    grid = Grid(grid_data)
    grid.set_symbol((2,2), "[")
    grid.set_symbol((3,2), "]")
    grid.set_symbol((3,1), "[")
    grid.set_symbol((4,1), "]")
    grid.set_symbol((1,1), "[")
    grid.set_symbol((2,1), "]")
    grid.set_symbol((3,0), "[")
    grid.set_symbol((4,0), "]")
    grid.init_boxes()
    boxes = grid.attached_boxes((2,2), (0, -1))
    assert len(boxes) == 4

def test_case2():
    grid_data = [["." for _ in range(cols)] for _ in range(rows)]
    grid = Grid(grid_data)
    grid.set_symbol((2,2), "[")
    grid.set_symbol((3,2), "]")
    grid.set_symbol((4,2), "[")
    grid.set_symbol((5,2), "]")
    grid.init_boxes()
    boxes = grid.attached_boxes((2,2), (1,0))
    assert len(boxes) == 2

    boxes = grid.attached_boxes((3,2), (1,0))
    assert len(boxes) == 2

    boxes = grid.attached_boxes((5,2), (-1,0))
    assert len(boxes) == 2

    boxes = grid.attached_boxes((4,2), (-1,0))
    assert len(boxes) == 2

def test_case3():
    grid_data = [["." for _ in range(cols)] for _ in range(rows)]
    grid = Grid(grid_data)

    b = Box((5,5), (4,5), grid)
    grid.boxes.add(Box((2,2), (3,2), grid))
    grid.boxes.add(Box((4,2), (5,2), grid))
    grid.boxes.add(b)

    grid.draw_boxes()
    grid.print()

    grid.erase_boxes()
    grid.boxes.remove(b)
    grid.draw_boxes()
    grid.print()

def test_case4():
    grid_data = [["." for _ in range(cols)] for _ in range(rows)]
    grid = Grid(grid_data)

    grid.boxes.add(Box((2,2), (3,2), grid))
    grid.boxes.add(Box((4,2), (5,2), grid))
    grid.boxes.add(Box((5,5), (4,5), grid))
    grid.draw_boxes()

    boxes = grid.attached_boxes((2,2), (1,0))
    print(boxes)
    grid.print()
    grid.move_boxes(boxes, (1, 0))
    grid.print()
    grid.move_boxes(boxes, (1, 0))
    grid.print()
    grid.move_boxes(boxes, (1, 0))
    grid.print()
    grid.move_boxes(boxes, (1, 0))
    grid.print()

if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
