
def transpose(pattern: list[str]):
    return list(zip(*pattern))


def is_smudged(a: list[str], b: list[str]) -> bool:
    smudge = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                smudge += 1

    return smudge == 1


def find_reflection_index(lines: list[str]) -> int:
    for i in range(1, len(lines)):
        above = lines[:i][::-1]
        below = lines[i:]

        below = below[:len(above)]
        above = above[:len(below)]

        if below == above:
            return i
    return 0


def find_reflection_index_with_smudge(lines: list[str]) -> int:
    for i in range(1, len(lines)):
        above = lines[:i][::-1]
        below = lines[i:]

        below = below[:len(above)]
        above = above[:len(below)]

        if is_smudged(above, below):
            return i
    return 0


def solve1(patterns: list[str]):
    sum = 0
    for pattern in patterns:
        row = find_reflection_index(pattern.split("\n"))
        col = find_reflection_index(transpose(pattern.split("\n")))
        sum += col + 100 * row
    print(sum)


def solve2(patterns: list[str]):
    sum = 0
    for pattern in patterns:
        row = find_reflection_index_with_smudge(pattern.split("\n"))
        col = find_reflection_index_with_smudge(transpose(pattern.split("\n")))
        sum += col + 100 * row
    print(sum)


def main():
    with open("input.txt") as f:
        data = f.read()

    patterns = data.split("\n\n")
    solve1(patterns)
    solve2(patterns)


if __name__ == "__main__":
    main()
