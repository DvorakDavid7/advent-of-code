from collections import defaultdict

with open("input.txt", "r") as f:
    data = list(map(int, f.read().split(" ")))

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        h = len(str(stone)) // 2
        s = str(stone)
        return [int(s[:h]), int(s[h:])]
    else:
        return [stone * 2024]


# def get_next_layer(stones: dict[int, int]) -> dict[int, int]:
#     result: dict[int, int] = {} 

#     for stone, freq in stones.items():
#         res = process_stone(stone)
#         for k in res:
#             result[k] = (result.get(k, 0) + 1) * freq

#     return result


def get_next_layer(stones: dict[int, int]) -> dict[int, int]:
    result = defaultdict(int)

    for stone, freq in stones.items():
        res = process_stone(stone)
        for k in res:
            result[k] += freq

    return dict(result)


layer = {s: 1 for s in data}
number_of_iterations = 75
for i in range(number_of_iterations):
    res = get_next_layer(layer)
    layer = res
    # print(f"{i} / {number_of_iterations}")

result = 0
for k in layer:
    result += layer[k]
print(result)
