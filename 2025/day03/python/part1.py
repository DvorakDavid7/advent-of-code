
def get_max_digit(line: str):
    result = 0
    for ch in line:
        if int(ch) > result:
            result = int(ch)
    return result

def get_largest_num(line: str):
    max_l, max_r, result = 0, 0, 0
    for i in range(len(line) - 1):
        dig = int(line[i])
        if dig > max_l:
            max_l = dig
            max_r = get_max_digit(line[i + 1:])
            result = int(f"{max_l}{max_r}")
    return result

def main():
    with open("day03/python/input.txt", "r") as f:
        data = f.read().splitlines()

    result = 0
    for line in data:
        result += get_largest_num(line)

    print(result)

main()
