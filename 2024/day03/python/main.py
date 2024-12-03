import re


def mul(m: str):
    n1, n2 = map(int, m[4:-1].split(",")) 
    return n1 * n2


def main():
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


if __name__ == "__main__":
    main()
