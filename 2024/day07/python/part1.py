with open("input.txt") as f:
    data = f.read().splitlines()

def solve(acc, op, nums, target):
    if acc == target and len(nums) == 0:
        return True
    if acc > target or len(nums) == 0:
        return False
    acc_new = eval(f"{acc}{op}{nums[0]}")
    return solve(acc_new, "+", nums[1:], target) or solve(acc_new, "*", nums[1:], target)

result = 0
for line in data:
    target, rest = line.split(":")
    nums = list(map(int, rest.strip().split(" ")) )
    target = int(target)
    if solve(0, "+", nums, target):
        result += target

print(result)
