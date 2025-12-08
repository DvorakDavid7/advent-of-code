
def prod(nums: list[int]) -> int:
    result = 1
    for n in nums:
        result *= n
    return result

def main():
    with open("day06/python/input.txt", "r") as f:
        data = f.read().splitlines()
    
    operations = data[-1].split()
    data = data[:-1]
    pos = 0
    result = 0
    numbers = []
    while len(operations) > 0:
        buffer = []
        for line in data:
            if not (0 <= pos < len(line)):
                continue
            buffer.append(line[pos])

        number_str = "".join(buffer).strip()
        if number_str:
            numbers.append(int(number_str))
        else:
            op = operations.pop(0)
            if op == "+":
                result += sum(numbers)
            else:
                result += prod(numbers)
            numbers = []
        pos += 1
    
    print(result)

main()
