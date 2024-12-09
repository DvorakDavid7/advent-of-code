
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

blanks = [i for i, x in enumerate(disc) if x == -1]

for i in blanks:
    while disc[-1] == -1: disc.pop()
    if len(disc) <= i: break
    disc[i] = disc.pop()

print(sum([i * x for i, x in enumerate(disc)]))
