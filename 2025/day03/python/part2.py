

def get_max_digit(line: str, number_of_digits: int):
    max_, index = 0, 0
    for i in range(len(line)):
        if len(line) - i < number_of_digits:
            break
        dig = int(line[i])
        if dig > max_:
            max_ = dig
            index = i
    return max_, line[index + 1:]

def get_largest_num(line):
    result = []
    number_of_digits = 12
    for i in range(number_of_digits):
        dig, line = get_max_digit(line, number_of_digits - i)
        result.append(str(dig))
    return int("".join(result))

def main():
    with open("day03/python/input.txt", "r") as f:
        data = f.read().splitlines()

    result = 0
    for line in data:
        result += get_largest_num(line)

    print(result)

main()
