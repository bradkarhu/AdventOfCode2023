import sys

def solve(line: str):
    ans = sum(myhash(s) for s in line.split(','))
    print(ans)

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