import regex as re
FNAME = "day_5.txt"

words = []
with open(FNAME, "r") as f:
    for line in f:
        words.append(line.strip())

def part_1():
    count = 0
    for word in words:
        vows = re.findall(r"(a|e|i|o|u)", word)
        forbiddens = re.findall(r"(ab|cd|pq|xy)", word)
        consecs = re.findall(r"(.)\1{1}", word)
        if len(vows) >= 3 and consecs and not forbiddens:
            count += 1
    print(count)

def part_2():
    count = 0
    for word in words:
        alts = re.findall(r"(.).\1{1}", word)
        consecs = re.findall(r"(..).*\1{1}", word)
        if alts and consecs:
            count += 1
    print(count)

part_1()
part_2()