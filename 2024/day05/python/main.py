
class Rec:
    left: set[int]
    right: set[int]
    def __init__(self):
        self.left = set()
        self.right = set()


def is_valid_line(nums: list[int], cache: dict[int, Rec]):
    for i in range(len(nums)):
        n = nums[i]
        left = set(nums[:i])
        right = set(nums[i + 1:])
        if not left.issubset(cache[n].left) or not right.issubset(cache[n].right):
            return False
    return True


def fix_line(nums: list[int], cache: dict[int, Rec]) -> list[int]:
    result: list[int] = []
    for _ in nums:
        for i in range(len(nums)):
            candidate = nums[i]
            left = set(result)
            right = set(nums) - left - set([candidate])
            if left.issubset(cache[candidate].left) and right.issubset(cache[candidate].right):
                result.append(candidate)
    return result


def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    delim = data.index("")
    rules = data[:delim]
    prints = data[delim + 1:]

    cache: dict[int, Rec] = {}

    for rule in rules:
        l, r = map(int, rule.split("|"))

        if l not in cache:
            cache[l] = Rec()
        if r not in cache:
            cache[r] = Rec()
        cache[l].right.add(r)
        cache[r].left.add(l)

    result1 = 0
    result2 = 0
    for line in prints:
        nums = list(map(int, line.split(",")) )

        if is_valid_line(nums, cache):
            result1 += nums[len(nums) // 2]
        else:
            fixed_line = fix_line(nums, cache)
            result2 += fixed_line[len(fixed_line) // 2]

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
