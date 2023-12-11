
def process_seq(seq: list[int]) -> list[int]:
    last_values = []
    cur = seq
    while cur != [0] * len(cur):
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        last_values.append(cur[-1])
    return last_values

def main():
    with open("./input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    res1 = []
    res2 = []
    for line in lines:
        nums = [int(x) for x in line.split()]
        last_vals = process_seq(nums)
        first_vals = process_seq(nums[::-1])
        res2.append(nums[0] + sum(first_vals))
        res1.append(sum(last_vals) + nums[-1])
    print(sum(res1))
    print(sum(res2))


if __name__ == "__main__":
    main()
