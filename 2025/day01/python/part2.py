
def number_of_zeros(current: int, rotation: int, direction: int):
    result = 0
    for _ in range(rotation):
        current = (current + direction) % 100
        if current == 0:
            result += 1
    return result


def main():
    current = 50
    with open("day01/python/input.txt", "r") as file:
        lines = file.readlines()
    
    result = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())

        if direction == 'L':
            result += number_of_zeros(current, value, -1)
            current = (current - value) % 100

        if direction == 'R':
            result += number_of_zeros(current, value, 1)
            current = (current + value) % 100

    print(result)

main()