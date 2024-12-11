
with open("input.txt", "r") as f:
    data = list(map(int, f.read().split(" ")))

result = []

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        h = len(str(stone)) // 2
        s = str(stone)
        return [int(s[:h]), int(s[h:])]
    else:
        return [stone * 2024]

for _ in range(25):
    i = 0
    j = 0

    buff = data
    while i < len(buff):
        stone = buff[i]

        res = process_stone(stone)

        if len(res) == 1:
            data[j] = res[0]
            j += 1
        else:
            data = data[:j] + [res[0], res[1]] + data[j + 1:]
            j += 2
        i += 1

print(len(data))
