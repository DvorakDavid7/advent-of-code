
Interval = tuple[int, int]

def parse_interval(x:str):
    l, r = x.split("-")
    return (int(l), int(r))

def merge_intervals(x: Interval|None, y: Interval):
    if x == None: return y
    if x[1] > y[1]: return x
    return (x[0], y[1])

def are_overlaping(x: Interval|None, y: Interval) -> bool:
    if x == None: return True
    return x[1] >= y[0]

def main():
    with open("day05/python/input.txt", "r") as f:
        intervals, _ = list(map(lambda x: x.splitlines(), f.read().split("\n\n")))

    intervals = sorted(list(map(parse_interval, intervals)), key=lambda x: x[0])
    current = None
    result = 0 
    for i in intervals:
        if are_overlaping(current, i):
            current = merge_intervals(current, i)
        else:
            result += (current[1] - current[0]) + 1
            current = i
    else:
        result += (current[1] - current[0]) + 1

    print(result)

main()

"""
raw:
3-5
10-14
16-20
12-18

sorted:
3-5          ---
10-14               ----   
12-18                 ------               
16-20                    ----------

flatten:
3-5, 10-20
"""
