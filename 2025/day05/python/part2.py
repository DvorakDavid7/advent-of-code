
def parse_interval(x:str):
    l, r = x.split("-")
    return (int(l), int(r))

def is_in_intervals(x: int, intervals: list[tuple[int, int]]) -> bool:
    for i in intervals:
        if i[0] <= x and x <= i[1]:
            return True
    return False

def merge_intervals(x: tuple[int, int], y: tuple[int, int]):
    return (x[0], y[1])

def main():
    with open("day05/python/test.txt", "r") as f:
        intervals, values = list(map(lambda x: x.splitlines(), f.read().split("\n\n")))

    values = list(map(int, values))
    intervals = list(map(parse_interval, intervals))

    intervals = sorted(intervals, key=lambda x: x[0])


    for interval in intervals:
        to_merge = []

main()

