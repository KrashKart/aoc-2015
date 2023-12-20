FNAME = "day_3.txt"

with open(FNAME, "r") as f:
    for line in f:
        dirs = line

d = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

def part_1():
    visited = [(0, 0)]
    i, j = 0, 0
    for dd in dirs:
        di, dj = d[dd]
        i, j = i + di, j + dj
        if (i, j) not in visited:
            visited.append((i, j))
    print(len(visited))

def part_2():
    visited = [(0, 0)]
    i, j, k, l = 0, 0, 0, 0
    for ii in range(0, len(dirs), 2):
        di, dj = d[dirs[ii]]
        dk, dl = d[dirs[ii + 1]]
        i, j, k, l = i + di, j + dj, k + dk, l + dl
        if (i, j) not in visited:
            visited.append((i, j))
        if (k, l) not in visited:
            visited.append((k, l))
    print(len(visited))

part_1()
part_2()