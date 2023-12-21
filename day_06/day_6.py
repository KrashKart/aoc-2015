FNAME = "day_6.txt"

instr = []
with open(FNAME, "r") as f:
    for line in f:
        if "turn on" in line:
            i, ins = "on", 1
        elif "turn off" in line:
            i, ins = "off", -1
        else:
            i, ins = "toggle", 2
        _, ran = line.strip().split(i)
        fro, to = ran.split(" through ")
        fro, to = tuple(map(int, fro.split(","))), tuple(map(int, to.split(",")))
        instr.append((ins, fro, to))

def part_1():
    grid = [[-1 for _ in range(1000)] for _ in range(1000)]
    count = 0
    for (ins, fro, to) in instr:
       (i, j), (k, l) = fro, to
       for ii in range(i, k + 1):
           for jj in range(j, l + 1):
               if ins == 2:
                   grid[ii][jj] = -grid[ii][jj]
               else:
                   grid[ii][jj] = ins
    
    for iii in range(1000):
        for jjj in range(1000):
            if grid[iii][jjj] == 1:
                count += 1
    print(count)

def part_2():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    count = 0
    for (ins, fro, to) in instr:
       (i, j), (k, l) = fro, to
       for ii in range(i, k + 1):
           for jj in range(j, l + 1):
                grid[ii][jj] = max(0, grid[ii][jj] + ins)
    
    for iii in range(1000):
        for jjj in range(1000):
            count += grid[iii][jjj]
    print(count)

part_1()
part_2()