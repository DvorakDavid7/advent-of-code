

def is_invalid(num):
    num = str(num)
    if len(num) % 2 != 0:
        return False
    l = len(num)
    return num[:l // 2] == num[l // 2:]

def main():
    with open("day02/python/input.txt", "r") as file:
        data = file.read().split(",")

    result = 0
    for interval in data:
        lower, upper = list(map(int, interval.split("-")))
        for i in range(lower, upper + 1):
            if is_invalid(i):
                result += i
    print(result)

main()