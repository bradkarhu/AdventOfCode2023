import sys

def solve(line: str):
    boxes = [{} for _ in range(256)] # init
    for s in line.split(','):
        if s[-1] == '-':
            a = s[:-1]
            box = boxes[myhash(a)]
            if a in box: del box[a]
        else:
            a, lens = s.split('=')
            box = boxes[myhash(a)]
            box[a] = int(lens) # python dict is ordered!
    #print(boxes)
    total = 0
    for i in range(len(boxes)):
        j = 1
        for _,v in boxes[i].items():
            total += (i+1) * j * v
            j += 1
    print(total)

def myhash(s: str) -> int:
    value = 0
    for c in iter(s):
        value += ord(c)
        value *= 17
        value %= 256
    return value

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()[0] # all on the first line

solve(f)