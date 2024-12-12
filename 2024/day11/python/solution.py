from functools import cache

with open("input.txt", "r") as f:
    data = [int(stone) for stone in f.read().split(" ")]

@cache
def count(stone, step):
    s = str(stone)
    if step == 0:
        return 1
    if stone == 0:
        return count(1, step - 1)
    elif len(s) % 2 == 0:
        h = len(s) // 2
        return count(int(s[:h]), step - 1) + count(int(s[h:]), step - 1)
    else:
        return count(stone * 2024, step - 1)

print(sum([count(stone, 25) for stone in data]))
print(sum([count(stone, 75) for stone in data]))
