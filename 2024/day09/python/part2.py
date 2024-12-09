with open("input.txt", "r") as f:
    data = f.read()

disc = []
fid = 0

for i, char in enumerate(data):
    x = int(char)
    if i % 2 == 0:
        disc += [fid] * x
        fid += 1
    else:
        disc += [-1] * x

def find_leftmost_free_space(size):
    i = 0
    while i <= len(disc) - size:
        if all(disc[i + j] == -1 for j in range(size)):
            return i
        i += 1
    return -1

def move_file(file_id):
    indices = [i for i, x in enumerate(disc) if x == file_id]
    if not indices:
        return

    size = len(indices)
    fstart = indices[0]

    free_start = find_leftmost_free_space(size)
    if free_start == -1 or free_start >= fstart:
        return

    for i in range(size):
        disc[free_start + i] = file_id
        disc[fstart + i] = -1

fids = sorted(list({fid for fid in disc if fid != -1}), reverse=True)

for fid in fids:
    move_file(fid)

print(sum([i * x for i, x in enumerate(disc) if x != -1]))
