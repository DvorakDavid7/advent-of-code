
def main():
    current = 50
    with open("day01/python/input.txt", "r") as file:
        lines = file.readlines()
    
    result = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())

        if direction == 'L':
            current = (current - value) % 100
        if direction == 'R':
            current = (current + value) % 100
        
        if current == 0:
            result += 1
            
    print(result)

main()