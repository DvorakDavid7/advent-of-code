from math import sqrt

# x, y, z, circuit_id
P = list[int, int, int]

def distance(a: P, b: P) -> float:
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

def find_closest_box(b: P, points: list[P]) -> P:
    result = None
    min = float("inf")
    index = 0
    for i, p in enumerate(points):
        if p == b: continue
        d = distance(b, p)
        if d < min:
            min = d
            result = p
            index = i
    return result, index


def solve(m: dict[P, P], p: P, circuit=None) -> set[P]:
    if circuit is None:
        circuit = set()
    if p in circuit:
        return circuit
    circuit.add(p)
    return solve(m, m[p], circuit)



def main():
    with open("day08/python/test.txt", "r") as f:
        data = f.read().splitlines()
    points = [line.split(",") for line in data]
    points = [(int(p[0]), int(p[1]), int(p[2])) for i, p in enumerate(points)]

    # c_ids = set()
    # for i in range(len(points)):
    #     c, c_index = find_closest_box(points[i], points)

    #     if c[3] in c_ids:
    #         points[i][3] = c[3]
    #     if points[i][3] in c_ids:
    #         points[c_index][3] = points[i][3]
    #     else:
    #         c_id = min(points[c_index][3], c[3])
    #         c_ids.add(c_id)
    #         points[i][3] = c_id
    #         points[c_index][3] = c_id
    
    m = {}
    for p_index in range(len(points)):
        p = points[p_index]
        c, c_index = find_closest_box(points[p_index], points)

        m[p] = c

    for p in points:
        print(solve(m, p))
    return

    buffer = set()
    for p in m:
        if p in buffer:
            break
        
        buffer.add(p)


    # m = {}
    # for p in points:
    #     if p[3] not in m:
    #         m[p[3]] = []
    #     m[p[3]].append(p)
    
    # for k in m:
    #     print(m[k])
    
    print(m.keys())
main()
