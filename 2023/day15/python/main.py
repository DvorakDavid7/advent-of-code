
def hash(s: str):
    result = 0
    for ch in s:
        result += ord(ch)
        result *= 17
        result %= 256
    return result


def main():
    with open("input.txt") as f:
        data = f.read()

    instructions = data.split(",")

    sum = 0
    for instruction in instructions:
        sum += hash(instruction)
    print(sum)


if __name__ == "__main__":
    main()
