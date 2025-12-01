

def main():
    with open("test.txt", "r") as f:
        data = f.read().split("\n\n")
        inputs = data[0]
        gates = data[1]

    values = {}
    result = {}

    for input_line in inputs.splitlines():
        var, val = input_line.split(":")
        values[var.strip()] = int(val.strip())
    
    for gate in gates.splitlines():
        wires, res = gate.split(" -> ")
        result[res] = -1
        w1, g, w2 = wires.split(" ")

        if w1 not in values or w2 not in values:
            continue

        if g == "AND":
            values[res] = 1 if values[w1] == 1 and values[w2] == 1 else 0
        elif g == "OR":
            values[res] = 1 if values[w1] == 1 or values[w2] == 1 else 0
        elif g == "XOR":
            values[res] = 1 if values[w1] != values[w2] else 0
    
    print(values)

if __name__ == "__main__":
    main()