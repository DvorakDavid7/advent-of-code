from functools import cache


with open("input.txt", "r") as f:
    data = f.read().splitlines()

delim = data.index("")
patterns = list(map(lambda x : x.strip(), data[:delim][0].split(",")))
designs = data[delim + 1:]

@cache
def num_of_possibilities(design):
    count = 0
    if design == "": return 1
    for pattern in patterns:
        l = len(pattern)
        if design[:l] == pattern:
            count += num_of_possibilities(design[l:])
    return count

def main():
    result = 0
    for design in designs:
        result += num_of_possibilities(design)
    print(result)

main()
