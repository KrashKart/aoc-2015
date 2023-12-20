FNAME = "day_2.txt"

ls = []
def calc_wrap(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(h*l, w*h, l*w)

def calc_ribb(l, w, h):
    min_two = [l, w, h]
    min_two.remove(max(min_two))
    one, two = min_two
    return l * w * h + 2 * one + 2 * two

with open(FNAME, "r") as f:
    for line in f:
        dims = line.strip().split("x")
        ls.append(list(map(int, dims)))

def part_1():
    s = 0
    for (l,w,h) in ls:
        s += calc_wrap(l, w, h)
    print(s)

def part_2():
    s = 0
    for (l,w,h) in ls:
        s += calc_ribb(l, w, h)
    print(s)

part_1()
part_2()
