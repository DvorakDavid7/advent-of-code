import re


def mul(m: str):
    n1, n2 = map(int, m[4:-1].split(",")) 
    return n1 * n2


def part1():
    pattern = r"mul\(\d+,\d+\)"
    with open("input.txt", "r") as f:
        data = f.read()

    buffer: str = ""

    result = 0
    for ch in data:
        buffer += ch

        match = re.search(pattern, buffer)

        if match:
            m = buffer[match.start():match.end()]
            result += mul(m)
            buffer = ""
    
    print(result)

def part2():
    mul_pattern = r"mul\(\d+,\d+\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    with open("input.txt", "r") as f:
        data = f.read()

    buffer: str = ""

    result = 0
    enabled = True

    for ch in data:
        buffer += ch

        mul_match = re.search(mul_pattern, buffer)
        do_match = re.search(do_pattern, buffer)
        dont_match = re.search(dont_pattern, buffer)

        if dont_match:
            enabled = False
            buffer = ""

        if do_match:
            enabled = True
            buffer = ""

        if mul_match:
            m = buffer[mul_match.start():mul_match.end()]
            if enabled:
                result += mul(m)
            buffer = ""

    print(result)


if __name__ == "__main__":
    part1()
    part2()
