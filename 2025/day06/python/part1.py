
def prod(nums: list[int]) -> int:
    result = 1
    for n in nums:
        result *= n
    return result

def main():
    with open("day06/python/input.txt", "r") as f:
        data = f.read().splitlines()

    lines = [line.split() for line in data]
    pos = 0
    result = 0
    while pos < len(lines[0]):
        numbers = []
        for line in lines:
            value = line[pos]

            if value in "+*":
                if value == "+":
                    result += sum(numbers)
                else:
                    result += prod(numbers)
                pos += 1
            else:
                numbers.append(int(value))
    
    print(result)

main()
