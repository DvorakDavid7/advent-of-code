from functools import cache


with open("input.txt", "r") as f:
    data = f.read().splitlines()

delim = data.index("")
patterns = list(map(lambda x : x.strip(), data[:delim][0].split(",")))
designs = data[delim + 1:]

@cache
def is_possible(design, pattern=""):
    l = len(pattern)
    if design == "": return True
    if design[:l] != pattern: return False
    return any([is_possible(design[l:], pattern) for pattern in patterns])

def main():
    result = 0
    for design in designs:
        if is_possible(design): result += 1
    print(result)

main()
