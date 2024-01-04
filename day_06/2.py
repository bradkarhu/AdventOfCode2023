from math import sqrt
import sys

def solve(lines: list[str]):
    tt_s = lines[0].replace(" ", "").split(":")[1]
    dd_s = lines[1].replace(" ", "").split(":")[1]
    tt = int(tt_s)
    dd = int(dd_s)
    factor = pow(10, len(tt_s))
    mid = int(tt / 2)
    min = mid
    max = mid
    while factor >= 1:
        for t in range(min, min - (factor * 10), factor * -1):
            if t * (tt - t) > dd and min > t: min = t
        for t in range(max, max + (factor * 10), factor):
            if t * (tt - t) > dd and max < t: max = t
        factor = int(factor / 10)
    print(max - min + 1)

with open(sys.argv[1], "r") as file:
    f = file.read().splitlines()

solve(f)