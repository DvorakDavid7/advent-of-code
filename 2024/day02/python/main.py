

def is_in_range(a: int, b: int) -> bool:
    return 1 <= abs(a - b) <= 3


def is_safe(l: list[int]) -> bool:
    is_inreasing = l[0] > l[1]

    for i in range(len(l) - 1):
        a, b = l[i], l[i + 1]

        if is_inreasing:
            if a < b or not is_in_range(a, b):
                return False
        else:
            if a > b or not is_in_range(a, b):
                return False
    return True


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        l = list(map(int, [n for n in line.split()]))
        if is_safe(l):
            result += 1

    print(result)

if __name__ == "__main__":
    main()
