from hashlib import md5 as m

def md(s):
    s = str(s)
    key = "ckczppom"
    s = (key + s).encode()
    return str(m(s).hexdigest())

def part_1():
    curr = 0
    fin = md(curr)
    while fin[:5] != "00000":
        curr += 1
        fin = md(curr)
    print(curr)

def part_2():
    curr = 0
    fin = md(curr)
    while fin[:6] != "000000":
        curr += 1
        fin = md(curr)
    print(curr)

part_1()
part_2()