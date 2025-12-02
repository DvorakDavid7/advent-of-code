

def is_invalid(num):
    num = str(num)
    for i in range(1, len(num) // 2 + 1):
        sub = num[:i]
        if num.count(sub) * len(sub) == len(num):
            return True
    return False

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
