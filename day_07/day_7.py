from functools import cache

conns = {}

for line in open("day_7.txt", "r"):
    op, key = line.split(" -> ")
    conns[key.strip()] = op

@cache
def prop(key):
    try:
        return int(key)

    except ValueError:
        pass

    get = conns[key].split(" ")

    if "NOT" in get:
        return ~prop(get[1])
    if "AND" in get:
        return prop(get[0]) & prop(get[2])
    elif "OR" in get:
        return prop(get[0]) | prop(get[2])
    elif "LSHIFT" in get:
        return prop(get[0]) << prop(get[2])
    elif "RSHIFT" in get:
        return prop(get[0]) >> prop(get[2])
    else:
        return prop(get[0])

def part_1():
    print((prop("a")))

def part_2():
    conns["b"] = str(prop("a"))
    prop.cache_clear()
    print((prop("a")))

part_1()
part_2()

