
def main():
    with open("input.txt") as f:
        blocks = f.read().strip().split("\n\n")

    lock_pins = []
    key_pins = []

    for block in blocks:
        rows = block.splitlines()

        pins = [0] * len(rows[0])
        for row in rows:
            for i, char in enumerate(row):
                if char == "#":
                    pins[i] += 1
        pins = list(map(lambda x: x - 1, pins))

        if "#" * len(rows[0]) in rows[0]:
            lock_pins.append(pins)
        if "." * len(rows[0]) in rows[0]:
            key_pins.append(pins)

    result = 0
    for key in key_pins:
        for lock in lock_pins:
            if all(k + l <= 5 for k, l in zip(key, lock)): 
                result += 1
    print(result)

main()