
def parse_interval(x:str):
    l, r = x.split("-")
    return (int(l), int(r))

def is_in_intervals(x: int, intervals: list[tuple[int, int]]) -> bool:
    for i in intervals:
        if i[0] <= x and x <= i[1]:
            return True
    return False

def main():
    with open("day05/python/input.txt", "r") as f:
        intervals, values = list(map(lambda x: x.splitlines(), f.read().split("\n\n")))

    intervals = list(map(parse_interval, intervals))
    values = list(map(int, values))

    result = 0
    for x in values:
        if is_in_intervals(x, intervals):
            result += 1
    
    print(result)

main()
