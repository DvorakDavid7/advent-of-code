
def solution1():
    with open("input.txt", "r") as f:
        data = f.read()

    left_list: list[int] = []
    right_list: list[int] = []
    for pair in data.splitlines():
        n1, n2 = map(int, pair.split())
        left_list.append(n1)
        right_list.append(n2)

    print(sum(list(map(lambda x: abs(x[0] - x[1]), zip(sorted(left_list), sorted(right_list))))))


def solution2():
    with open("input.txt", "r") as f:
        data = f.read()

    left_list: list[int] = []
    right_list_freq: dict[int, int] = {}

    for pair in data.splitlines():
        n1, n2 = map(int, pair.split())
        right_list_freq[n2] = right_list_freq.get(n2, 0) + 1
        left_list.append(n1)
    
    print(sum([num * right_list_freq.get(num, 0) for num in left_list]))

if __name__ == "__main__":
    solution1()
    solution2()
