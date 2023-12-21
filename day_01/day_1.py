FNAME = "day_1.txt"

with open(FNAME, "r") as f:
    for line in f:
        i = line

def part_1():
    count = 0
    for c in i:
        count += 1 if c == "(" else -1
    print(count)

def part_2():
    count = 0
    nth = 0
    for c in i:
        count += 1 if c == "(" else -1
        nth += 1
        if count < 0:
            print(nth)
            break

part_1()
part_2()